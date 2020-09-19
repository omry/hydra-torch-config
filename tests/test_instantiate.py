import pytest
from hydra.utils import get_class, instantiate
from omegaconf import OmegaConf
from typing import List
from torch import Tensor

from torch.optim import *
from config.torch.optim import *

class Parameters:
    def __init__(self, params: Tensor):
        self.params = params
    def __iter__(self):
        return iter(self.params)
             

@pytest.mark.parametrize(
    "classname, params, args, kwargs, expected",
    [
        pytest.param("Adam", {}, [], {"params": Parameters(Tensor([1]))}, Adam, id="AdamConf"),
        pytest.param("AdamW", {"params": Parameters(Tensor([1]))}, [], {}, AdamW, id="AdamWConf"),
    ]
)

def test_instantiate_classes(
    classname: str, params: Any, args: Any, kwargs: Any, expected: Any
) -> None:
    full_class = f"config.torch.optim.{classname}Conf"
    schema = OmegaConf.structured(get_class(full_class))
    cfg = OmegaConf.merge(schema, params)
    obj = instantiate(config=cfg, *args, **kwargs)
    assert type(obj) == expected 
