"""Base class for all fluids"""
from Items import BaseStackable
from Objects import RawFactoryObject


class BaseFluid(BaseStackable, raw={}, amount=1): #type: ignore
    """Any fluid"""
    def __init_subclass__(cls, raw: RawFactoryObject, /,*,  amount: int=1) -> None:
        return super().__init_subclass__(raw, amount=amount)
