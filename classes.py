from .Objects import BaseFactoryObject
from .Objects.Conveyors import BaseConveyor
from .Objects.Conveyors.mk1 import ConveyorMk1, ConveyorLiftMk1

def get_class(obj: str):
    match obj:
        case _:
            pass


objects = {
    "Game": {
        "FactoryGame": {
            "Buildable": {
                "Factory": {
                    "CA_SplitterSmart": object,
                    "ConveyorBeltMk1": ConveyorMk1
                }
            }
        }
    }
}