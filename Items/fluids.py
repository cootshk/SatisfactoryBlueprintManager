"""Base class for all fluids"""
from Items import BaseItem
from Objects import RawFactoryObject


class BaseFluid(BaseItem, raw={}):
    """Any fluid"""
    def __init_subclass__(cls, raw: RawFactoryObject) -> None:
        return super().__init_subclass__(raw)