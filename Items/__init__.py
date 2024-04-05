"""Base class for items"""
# See https://i.redd.it/txaw0muisfr61.jpg

from Objects import RawFactoryObject


class BaseStackable:
    """Any item or fluid"""
    def __init_subclass__(cls, raw: RawFactoryObject, /,*, amount: int = 1) -> None:
        cls.raw = raw #type: ignore
        cls.amount = amount #type: ignore
class BaseItem(BaseStackable, raw={}, amount=1): #type: ignore
    """Any item"""
    def __init_subclass__(cls,
                          raw: RawFactoryObject,
                          /,*,
                          MaxStackSize: int,
                          amount: int=1,
                          SinkTickets: int | None = None,
                          Radioactive: bool = False
                        ) -> None:
        cls.MaxStackSize = MaxStackSize #type: ignore
        cls.SinkTickets = SinkTickets #type: ignore
        cls.Radioactive = Radioactive #type: ignore
        return super().__init_subclass__(raw, amount=amount)

class BaseFluid(BaseStackable, raw={}, amount=1): #type: ignore
    """Any fluid"""
    def __init_subclass__(cls,
                          raw: RawFactoryObject,
                          /,*,
                          amount: int=1,
                          packaged: BaseItem
                        ) -> None:
        cls.packaged = packaged #type: ignore
        return super().__init_subclass__(raw, amount=amount)
