from Objects.Splitters.splitter import Splitter
from Objects import BaseFactoryObject, rawFactoryObject
from Objects.Conveyors import BaseConveyor
from Objects.Conveyors.mk1 import ConveyorMk1, ConveyorLiftMk1

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
                    "CA_Splitter": Splitter,
                    "CA_SplitterSmart": object,
                    "ConveyorBeltMk1": ConveyorMk1
                }
            }
        }
    }
}