from dataclasses import dataclass
from pathlib import Path

import inspect
import logging
from jinja2 import Environment, PackageLoader
from typing import List, Optional, Any

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import MISSING, SI
from omegaconf._utils import type_str

log = logging.getLogger(__name__)

jinja_env = Environment(loader=PackageLoader("main", "../templates"), trim_blocks=True)
jinja_env.tests["empty"] = lambda x: x == inspect.Signature.empty


@dataclass
class Module:
    name: str = MISSING
    classes: List[str] = MISSING


@dataclass
class Config:
    output: str = MISSING
    modules: List[Module] = MISSING


@dataclass
class Parameter:
    name: str
    type_str: str
    default: Optional[str]


config_store = ConfigStore.instance()
config_store.store(name="config", node=Config)


@hydra.main(config_path="../conf", config_name="config")
def main(cfg: Config):
    for module in cfg.modules:
        for classname in module.classes:
            code = generate(jinja_env, module.name, classname)
            save(cfg=cfg, module=module.name, classname=classname, code=code)


def save(cfg: Config, module: str, classname: str, code: str) -> None:
    path = Path(cfg.output) / module.replace(".", "/") / "conf"
    path.mkdir(parents=True, exist_ok=True)
    file = path / (classname + ".py")
    file.unlink(missing_ok=True)
    file.write_text(code)


def generate(env: Environment, module: str, class_name: str) -> None:
    full_name = f"{module}.{class_name}"
    cls = hydra.utils.get_class(full_name)
    sig = inspect.signature(cls)
    template = env.get_template("dataclass.j2")
    params: List[Parameter] = []
    for name, p in sig.parameters.items():
        type_ = p.annotation
        if type_ == sig.empty:
            type_ = Any
        params.append(Parameter(name=name, type_str=type_str(type_), default=p.default))
    return template.render(target=full_name, class_name=class_name, params=params)


if __name__ == "__main__":
    main()
