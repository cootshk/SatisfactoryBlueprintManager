"""Mk. 3 Conveyors"""
from dataclasses import dataclass

from . import BaseConveyor
from .. import RawFactoryObject

@dataclass
class BaseConveyorMk3(BaseConveyor, raw={}, tier=3, is_lift=False, throughput=270): #type: ignore
    """A base conveyor (mk. 3)

    Args:
        raw (rawFactoryData): Raw JSON Data.
        is_lift (bool): If the conveyor is a conveyor lift or conveyor belt
    Properties:
        See #BaseConveyor 
    """
    def __init_subclass__(cls, raw: RawFactoryObject, is_lift: bool) -> None:
        return super().__init_subclass__(raw, tier=3, is_lift=is_lift, throughput=270)

@dataclass
class ConveyorMk3(BaseConveyorMk3, raw={}, is_lift=False):
    """A Mk. 3 Conveyor Belt

    Args:
        raw (rawFactoryObject): Raw JSON Data.
    Properties:
        See #BaseConveyor
    """
    def __init__(self, raw: RawFactoryObject):
        super().__init_subclass__(raw,is_lift=False)

@dataclass
class ConveyorLiftMk3(BaseConveyorMk3, raw={}, is_lift=True):
    """A Mk. 3 Conveyor Lift
    
    Args:
        raw (rawFactoryObject): Raw JSON Data.
    Properties:
        See #BaseConveyor
    """
    def __init__(self, raw: RawFactoryObject):
        super().__init_subclass__(raw,is_lift=False)
