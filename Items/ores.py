from Items import BaseItem
from Objects import RawFactoryObject


class IronOreItem(BaseItem, raw={}, #type: ignore
                MaxStackSize=100, SinkTickets=1, Radioactive=False):
    """Iron Ore"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=1, Radioactive=False)
class CopperOreItem(BaseItem, raw={}, #type: ignore
                MaxStackSize=100, SinkTickets=8, Radioactive=False):
    """Copper Ore"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=8, Radioactive=False)
class CoalItem(BaseItem, raw={}, #type: ignore
                MaxStackSize=100, SinkTickets=3, Radioactive=False):
    """Coal Ore"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=3, Radioactive=False)
class CateriumOreItem(BaseItem, raw={}, #type: ignore
                MaxStackSize=100, SinkTickets=7, Radioactive=False):
    """Caterium Ore"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=7, Radioactive=False)
class QuartzItem(BaseItem, raw={}, #type: ignore
                MaxStackSize=100, SinkTickets=15, Radioactive=False):
    """Raw Quartz"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=15, Radioactive=False)
class SulfurItem(BaseItem, raw={}, #type: ignore
                MaxStackSize=100, SinkTickets=11, Radioactive=False):
    """Sulfur"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=11, Radioactive=False)
class UraniumItem(BaseItem, raw={}, #type: ignore
                MaxStackSize=100, SinkTickets=35, Radioactive=False):
    """Uranium"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=35, Radioactive=False)
class BauxiteItem(BaseItem, raw={}, #type: ignore
                MaxStackSize=100, SinkTickets=8, Radioactive=False):
    """Bauxite"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=8, Radioactive=False)
class LimestoneItem(BaseItem, raw={}, #type: ignore
                MaxStackSize=100, SinkTickets=2, Radioactive=False):
    """Limestone"""
    def __init__(self, raw: RawFactoryObject, /, *, amount: int = 1)-> None:
        super().__init_subclass__(
            raw, MaxStackSize=100, amount=amount, SinkTickets=2, Radioactive=False)
