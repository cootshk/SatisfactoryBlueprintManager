"""Mk. 1 Conveyors"""
from dataclasses import dataclass

from . import BaseConveyor
from .. import RawFactoryObject

@dataclass
class BaseConveyorMk1(BaseConveyor, raw={}, tier=1, is_lift=False):
    """A base conveyor (mk. 1)

    Args:
        raw (rawFactoryData): Raw JSON Data.
        is_lift (bool): If the conveyor is a conveyor lift or conveyor belt
    Properties:
        See #BaseConveyor 
    """
    def __init_subclass__(cls, raw: RawFactoryObject, is_lift: bool) -> None:
        return super().__init_subclass__(raw, 1, is_lift)

@dataclass
class ConveyorMk1(BaseConveyorMk1, raw={}, is_lift=False):
    """A Mk. 1 Conveyor Belt

    Args:
        raw (RawFactoryObject): Raw JSON Data.
    Properties:
        See #BaseConveyor
    """
    def __init__(self, raw: RawFactoryObject):
        super().__init_subclass__(raw,is_lift=False)

@dataclass
class ConveyorLiftMk1(BaseConveyorMk1, raw={}, is_lift=True):
    """A Mk. 1 Conveyor Lift
    
    Args:
        raw (RawFactoryObject): Raw JSON Data.
    Properties:
        See #BaseConveyor
    """
    def __init__(self, raw: RawFactoryObject):
        super().__init_subclass__(raw,is_lift=False)
