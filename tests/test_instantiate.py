import pytest
from hydra.utils import get_class, instantiate
from omegaconf import OmegaConf
from typing import List
from torch import Tensor

from torch.optim import *
from config.torch.optim import *

from torch import nn
model = nn.Linear(20, 30)

@pytest.mark.parametrize(
    "classname, toadd, args, kwargs, expected",
    [
        pytest.param("Adam", {}, [], {}, Adam, id="AdamConf"),
        pytest.param("AdamW", {}, [], {}, AdamW, id="AdamWConf"),
    ]
)

def test_instantiate_classes(
    classname: str, toadd: Any, args: Any, kwargs: Any, expected: Any
) -> None:
    full_class = f"config.torch.optim.{classname}Conf"
    schema = OmegaConf.structured(get_class(full_class))
    cfg = OmegaConf.merge(schema, {})
    obj = instantiate(cfg, params=model.parameters())
    assert type(obj) == expected 
