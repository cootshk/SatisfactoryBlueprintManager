"""Base class for all Vehicles"""
from Objects import BaseFactoryObject


class BaseVehicle(BaseFactoryObject, raw={}):
    """Base class for all vehicles"""
    def __init_subclass__(cls, raw: dict) -> None:
        return super().__init_subclass__(raw)
