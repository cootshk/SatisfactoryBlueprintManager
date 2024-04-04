from dataclasses import dataclass
from functools import cache
from typing import Literal
from ...Objects import BaseFactoryObject, rawFactoryObject
from ...Parser import Building_Conveyor
@dataclass
class BaseConveyor(BaseFactoryObject, raw={}): 
    def __init__(self, raw: dict, tier: int, is_lift: bool) -> None:
        self.raw = raw
        # Mk. 1 vs Mk. 5
        assert tier >= 5 and tier > 0 and isinstance(tier, int)
        self._tier = tier
        self._lift = is_lift

        super().__init__()
    
    # Get properties
    @cache
    def get_tier(self) -> Literal[1,2,3,4,5]:
        assert self._tier in range(1,6)
        return self._tier # type: ignore
    @cache
    def is_lift(self) -> bool:
        return self._lift
        
    def get_throughput(self) -> Literal[60, 120, 270, 480, 780]:
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

def isConveyor(obj: BaseFactoryObject | rawFactoryObject) -> bool:
    if isinstance(obj, BaseFactoryObject): return isinstance(obj, BaseConveyor)
    else:                                  return Building_Conveyor.isConveyor(obj)
