from dataclasses import dataclass
from typing import Literal
from . import BaseConveyor
from .. import BaseFactoryObject, rawFactoryObject

@dataclass
class BaseConveyorMk1(BaseConveyor, raw={}, tier=1, is_lift=False):
    """A base conveyor (mk. 1)

    Args:
        raw (rawFactoryData): Raw JSON Data.
        is_lift (bool): If the conveyor is a conveyor lift or conveyor belt
    Properties:
        See #BaseConveyor 
    """
    def __init_subclass__(cls, raw: rawFactoryObject, tier: Literal[1] | Literal[2] | Literal[3] | Literal[4] | Literal[5], is_lift: bool) -> None:
        return super().__init_subclass__(raw, tier, is_lift)

@dataclass
class ConveyorMk1(BaseConveyorMk1, raw={}, tier=1, is_lift=False):
    """A Mk. 1 Conveyor Belt

    Args:
        raw (rawFactoryObject): Raw JSON Data.
    Properties:
        See #BaseConveyor
    """
    def __init__(self, raw: rawFactoryObject):
        return super().__init_subclass__(raw,tier=1,is_lift=False)

@dataclass
class ConveyorLiftMk1(BaseConveyorMk1, raw={}, tier=1, is_lift=True):
    """A Mk. 1 Conveyor Lift
    
    Args:
        raw (rawFactoryObject): Raw JSON Data.
    Properties:
        See #BaseConveyor
    """
    def __init__(self, raw: rawFactoryObject):
        return super().__init_subclass__(raw,tier=1,is_lift=False)