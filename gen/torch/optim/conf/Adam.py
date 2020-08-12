# Generated code, do not edit.
from dataclasses import dataclass
from hydra.types import ObjectConf
from omegaconf import MISSING
from typing import *


class AdamParams(ObjectConf):
    params: Any
    lr: Any = 0.001
    betas: Any = (0.9, 0.999)
    eps: Any = 1e-08
    weight_decay: Any = 0
    amsgrad: Any = False


@dataclass
class AdamConf(ObjectConf):
    target: str = 'torch.optim.Adam'
    params: AdamParams(ObjectConf) = MISSING