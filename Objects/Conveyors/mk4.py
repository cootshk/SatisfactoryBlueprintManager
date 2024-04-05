"""Mk. 4 Conveyors"""
from dataclasses import dataclass

from . import BaseConveyor
from .. import rawFactoryObject

@dataclass
class BaseConveyorMk4(BaseConveyor, raw={}, tier=4, is_lift=False):
    """A base conveyor (mk. 4)

    Args:
        raw (rawFactoryData): Raw JSON Data.
        is_lift (bool): If the conveyor is a conveyor lift or conveyor belt
    Properties:
        See #BaseConveyor 
    """
    def __init_subclass__(cls, raw: rawFactoryObject, is_lift: bool) -> None:
        return super().__init_subclass__(raw, 4, is_lift)

@dataclass
class ConveyorMk4(BaseConveyorMk4, raw={}, is_lift=False):
    """A Mk. 4 Conveyor Belt

    Args:
        raw (rawFactoryObject): Raw JSON Data.
    Properties:
        See #BaseConveyor
    """
    def __init__(self, raw: rawFactoryObject):
        super().__init_subclass__(raw,is_lift=False)

@dataclass
class ConveyorLiftMk4(BaseConveyorMk4, raw={}, is_lift=True):
    """A Mk. 4 Conveyor Lift
    
    Args:
        raw (rawFactoryObject): Raw JSON Data.
    Properties:
        See #BaseConveyor
    """
    def __init__(self, raw: rawFactoryObject):
        super().__init_subclass__(raw,is_lift=False)
