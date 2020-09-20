import pytest
from hydra.utils import get_class, instantiate
from omegaconf import OmegaConf

from torch.optim import *
from config.torch.optim import *

import torch
from torch import Tensor
from torch import nn
model = nn.Linear(1, 2)

@pytest.mark.parametrize(
    "classname, cfg, passthrough_kwargs, expected",
    [
        pytest.param("Adam", {"lr": 0.1}, {"params":model.parameters()}, Adam(lr=0.1, params=model.parameters()), id="AdamConf"),
        pytest.param("AdamW", {"lr": 0.1}, {"params":model.parameters()}, AdamW(lr=0.1, params=model.parameters()), id="AdamWConf"),
    ]
)

def test_instantiate_classes(
    classname: str, cfg: Any, passthrough_kwargs: Any, expected: Any
) -> None:
    full_class = f"config.torch.optim.{classname}Conf"
    schema = OmegaConf.structured(get_class(full_class))
    cfg = OmegaConf.merge(schema, cfg)
    obj = instantiate(cfg, **passthrough_kwargs)

    def closure():
        return model(Tensor([10]))
    assert torch.all(torch.eq(obj.step(closure), expected.step(closure)))

