"""Base class & methods for all conveyors"""
from dataclasses import dataclass
from typing import Literal, overload

from Objects import BaseConnector, BaseFactoryObject, RawFactoryObject
from _Parser import Building_Conveyor

@dataclass
class BaseConveyor(BaseFactoryObject, raw={}):
    """BaseConveyor
    The base conveyor object, for all conveyors and lifts

    Properties:
        - raw (dict): the raw JSON data
    Fucntions:
        - get_tier => int: gets the tier of the conveyor/lift
        - is_lift => bool: gets if this conveyor is a conveyor lift
        - get_throughput => int: gets the number of items per minute that this conveyor can handle 
    """
    def __init_subclass__(
            cls,
            raw: RawFactoryObject, *,
            tier: Literal[1,2,3,4,5],
            is_lift: bool,
            throughput: Literal[60,120,270,480,780]
            ) -> None:
        cls.raw = raw # type: ignore
        # Mk. 1 vs Mk. 5
        assert tier <= 5 and tier > 0 and isinstance(tier, int), f"Tier {tier} is out of bounds!"
        cls.tier = tier #type: ignore
        #conveyor lift
        cls.lift = is_lift #type: ignore
        cls.throughput = throughput #type: ignore
        return super().__init_subclass__(raw)


@overload
def is_conveyor(obj: BaseFactoryObject) -> bool: ...
@overload
def is_conveyor(obj: RawFactoryObject) -> bool: ...

def is_conveyor(obj: BaseFactoryObject | RawFactoryObject) -> bool:
    """Tells if this object is a conveyor or a conveyor lift.

    Args:
        obj (BaseFactoryObject | RawFactoryObject): The object to check

    Returns:
        bool: True if the object is a conveyor or lift.
    """
    if isinstance(obj, BaseFactoryObject):
        return isinstance(obj, BaseConveyor)
    else:
        return Building_Conveyor.isConveyor(obj)


class ConveyorPole(BaseConnector, raw={}):
    """A conveyor pole. Connects two conveyors together."""
    def __init__(self, raw: RawFactoryObject, left: BaseConveyor, right: BaseConveyor) -> None:
        super().__init_subclass__(raw, left, right)
