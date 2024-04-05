"""Base class for items"""
# See https://i.redd.it/txaw0muisfr61.jpg

from Objects import RawFactoryObject


class BaseStackable:
    """Any item or fluid"""
    def __init_subclass__(cls, raw: RawFactoryObject, /,*, amount: int = 1) -> None:
        cls.raw = raw #type: ignore
        cls.amount = amount #type: ignore
class BaseItem(BaseStackable, raw={}):
    """Any item"""
    def __init_subclass__(cls, raw: RawFactoryObject, MaxStackSize: int, amount: int=1) -> None:
        cls.MaxStackSize = MaxStackSize #type: ignore
        return super().__init_subclass__(raw, amount)
