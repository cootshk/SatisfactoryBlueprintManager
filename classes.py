from Objects.Splitters.splitter import Splitter
from Objects import BaseFactoryObject, rawFactoryObject
from Objects.Conveyors import BaseConveyor
from Objects.Conveyors.mk1 import ConveyorMk1, ConveyorLiftMk1
from Objects.Conveyors.mk2 import ConveyorMk2
from Objects.Conveyors.mk3 import ConveyorMk3
from Objects.Conveyors.mk4 import ConveyorMk4
from Objects.Conveyors.mk5 import ConveyorMk5

def get_class(obj: rawFactoryObject):
    classname = list(obj.values())[0]["className"]
    currentitem = dict(objects)
    for path in classname:
        try:
            currentitem = currentitem[path] #type: ignore
        except KeyError:
            print(classname)
            input()
            break



objects = {
    "Game": {
        "FactoryGame": {
            "Buildable": {
                "Factory": {
                    # Splitters
                    "CA_Splitter": Splitter,
                    "CA_SplitterSmart": object,
                    # Belts
                    "ConveyorBeltMk1": ConveyorMk1,
                    "ConveyorBeltMk2": ConveyorMk2,
                    "ConveyorBeltMk3": ConveyorMk3,
                    "ConveyorBeltMk4": ConveyorMk4,
                    "ConveyorBeltMk5": ConveyorMk5,
                }
            }
        }
    }
}