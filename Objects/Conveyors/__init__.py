"""Base class & methods for all conveyors"""
from dataclasses import dataclass
from typing import Literal

from Objects import BaseFactoryObject, RawFactoryObject
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
            raw: RawFactoryObject,
            tier: Literal[1,2,3,4,5],
            is_lift: bool
            ) -> None:
        cls.raw = raw # type: ignore
        # Mk. 1 vs Mk. 5
        assert tier <= 5 and tier > 0 and isinstance(tier, int), f"Tier {tier} is out of bounds!"
        cls._tier = tier #type: ignore
        #conveyor lift
        cls._lift = is_lift #type: ignore
        return super().__init_subclass__(raw)

    # Get properties
    def get_tier(self) -> Literal[1,2,3,4,5]:
        """Gets the current tier of the conveyor

        Returns:
            int: 1, 2, 3, 4, or 5 - the current conveyor tier
        """
        assert self._tier in range(1,6)
        return self._tier # type: ignore
    def is_lift(self) -> bool:
        """Gets if the conveyor is a conveyor lift

        Returns:
            bool: True if this is a conveyor lift, False otherwise.
        """
        return self._lift
    def get_throughput(self) -> Literal[60, 120, 270, 480, 780]:
        """Gets the throughput of this tier of conveyor. 
        See https://satisfactory.wiki.gg/wiki/Conveyor_Belts#Item_transportation for more info.

        Returns:
            int: The amount of items per minute that this conveyor can handle 
        """
        match self.get_tier():
            case 1:
                return 60
            case 2:
                return 120
            case 3:
                return 270
            case 4:
                return 480
            case 5:
                return 780
            case _:
                raise ValueError("Invalid conveyor tier!")

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
