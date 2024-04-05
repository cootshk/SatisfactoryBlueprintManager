"""All of the ingot items"""
from Items import BaseItem
from Objects import RawFactoryObject


class IronIngotItem(BaseItem, raw={}, MaxStackSize=100, SinkTickets=2, Radioactive=False):
    """Iron Ingot"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=2, Radioactive=False)
class CopperIngotItem(BaseItem, raw={}, MaxStackSize=100, SinkTickets=6, Radioactive=False):
    """Copper Ingot"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=6, Radioactive=False)
class SteelIngotItem(BaseItem, raw={}, MaxStackSize=100, SinkTickets=8, Radioactive=False):
    """Steel Ingot"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=8, Radioactive=False)
class CateriumIngotItem(BaseItem, raw={}, MaxStackSize=100, SinkTickets=42, Radioactive=False):
    """Caterium Ingot"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=42, Radioactive=False)
class AluminumIngotItem(BaseItem, raw={}, MaxStackSize=100, SinkTickets=131, Radioactive=False):
    """Aluminum Ingot"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=131, Radioactive=False)
