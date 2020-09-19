# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import Any


@dataclass
class AdadeltaConf:
    _target_: str = "torch.optim.Adadelta"
    params: Any = MISSING
    lr: Any = 1.0
    rho: Any = 0.9
    eps: Any = 1e-06
    weight_decay: Any = 0


@dataclass
class AdagradConf:
    _target_: str = "torch.optim.Adagrad"
    params: Any = MISSING
    lr: Any = 0.01
    lr_decay: Any = 0
    weight_decay: Any = 0
    initial_accumulator_value: Any = 0
    eps: Any = 1e-10


@dataclass
class AdamConf:
    _target_: str = "torch.optim.Adam"
    lr: Any = 0.001
    betas: Any = (0.9, 0.999)
    eps: Any = 1e-08
    weight_decay: Any = 0
    amsgrad: Any = False


@dataclass
class AdamaxConf:
    _target_: str = "torch.optim.Adamax"
    params: Any = MISSING
    lr: Any = 0.002
    betas: Any = (0.9, 0.999)
    eps: Any = 1e-08
    weight_decay: Any = 0


@dataclass
class AdamWConf:
    _target_: str = "torch.optim.AdamW"
    params: Any = MISSING
    lr: Any = 0.001
    betas: Any = (0.9, 0.999)
    eps: Any = 1e-08
    weight_decay: Any = 0.01
    amsgrad: Any = False


@dataclass
class ASGDConf:
    _target_: str = "torch.optim.ASGD"
    params: Any = MISSING
    lr: Any = 0.01
    lambd: Any = 0.0001
    alpha: Any = 0.75
    t0: Any = 1000000.0
    weight_decay: Any = 0


@dataclass
class LBFGSConf:
    _target_: str = "torch.optim.LBFGS"
    params: Any = MISSING
    lr: Any = 1
    max_iter: Any = 20
    max_eval: Any = None
    tolerance_grad: Any = 1e-07
    tolerance_change: Any = 1e-09
    history_size: Any = 100
    line_search_fn: Any = None


@dataclass
class RMSpropConf:
    _target_: str = "torch.optim.RMSprop"
    params: Any = MISSING
    lr: Any = 0.01
    alpha: Any = 0.99
    eps: Any = 1e-08
    weight_decay: Any = 0
    momentum: Any = 0
    centered: Any = False


@dataclass
class RpropConf:
    _target_: str = "torch.optim.Rprop"
    params: Any = MISSING
    lr: Any = 0.01
    etas: Any = (0.5, 1.2)
    step_sizes: Any = (1e-06, 50)


@dataclass
class SGDConf:
    _target_: str = "torch.optim.SGD"
    params: Any = MISSING
    lr: Any = MISSING  # _RequiredParameter
    momentum: Any = 0
    dampening: Any = 0
    weight_decay: Any = 0
    nesterov: Any = False


@dataclass
class SparseAdamConf:
    _target_: str = "torch.optim.SparseAdam"
    params: Any = MISSING
    lr: Any = 0.001
    betas: Any = (0.9, 0.999)
    eps: Any = 1e-08
