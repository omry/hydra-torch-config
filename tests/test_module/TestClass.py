from typing import Union


class Empty:
    def __init__(self):
        ...


class Param_Untyped:
    def __init__(self, param):
        ...


class Param_typed:
    def __init__(self, param: int):
        ...


class Param_union:
    # Union is not currently supported by OmegaConf, it will be typed as Any
    def __init__(self, param: Union[int, float]):
        ...
