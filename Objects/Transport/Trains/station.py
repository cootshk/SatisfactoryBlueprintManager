from Objects import BaseFactoryObject


class BaseTrainPlatform(BaseFactoryObject, raw={}):
    pass


class TrainStation(BaseTrainPlatform, raw={}):
    pass
class FreightCar(BaseTrainPlatform, raw={}):
    pass
class FluidCar(BaseTrainPlatform, raw={}):
    pass
class EmptyPlatform(BaseTrainPlatform, raw={}):
    pass
class CatwalkPlatform(BaseTrainPlatform, raw={}):
    pass
