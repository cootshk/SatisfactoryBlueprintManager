from dataclasses import dataclass
from . import BaseConveyor
from .. import BaseFactoryObject, rawFactoryObject

@dataclass
class ConveyorMk1(BaseConveyor, raw={}, tier=1, is_lift=False):
    pass