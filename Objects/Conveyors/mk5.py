"""Mk. 5 Conveyors"""
from dataclasses import dataclass

from . import BaseConveyor
from .. import rawFactoryObject

@dataclass
class BaseConveyorMk5(BaseConveyor, raw={}, tier=5, is_lift=False):
    """A base conveyor (mk. 5)

    Args:
        raw (rawFactoryData): Raw JSON Data.
        is_lift (bool): If the conveyor is a conveyor lift or conveyor belt
    Properties:
        See #BaseConveyor 
    """
    def __init_subclass__(cls, raw: rawFactoryObject, is_lift: bool) -> None:
        return super().__init_subclass__(raw, 5, is_lift)

@dataclass
class ConveyorMk5(BaseConveyorMk5, raw={}, is_lift=False):
    """A Mk. 5 Conveyor Belt

    Args:
        raw (rawFactoryObject): Raw JSON Data.
    Properties:
        See #BaseConveyor
    """
    def __init__(self, raw: rawFactoryObject):
        super().__init_subclass__(raw,is_lift=False)

@dataclass
class ConveyorLiftMk5(BaseConveyorMk5, raw={}, is_lift=True):
    """A Mk. 5 Conveyor Lift
    
    Args:
        raw (rawFactoryObject): Raw JSON Data.
    Properties:
        See #BaseConveyor
    """
    def __init__(self, raw: rawFactoryObject):
        super().__init_subclass__(raw,is_lift=False)
