from ...Transport import BaseVehicle
from Objects import RawFactoryObject

class BaseTrainCar(BaseVehicle, raw={}):
    def __init__(self, raw: RawFactoryObject):
        pass