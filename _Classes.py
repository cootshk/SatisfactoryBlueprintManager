"""Tools to convert raw JSON into the classes"""
from Objects.Splitters.smart import SmartSplitter
from Objects.Splitters.splitter import Splitter
from Objects import BaseFactoryObject, RawFactoryObject
from Objects.Conveyors.mk1 import ConveyorMk1
from Objects.Conveyors.mk2 import ConveyorMk2
from Objects.Conveyors.mk3 import ConveyorMk3
from Objects.Conveyors.mk4 import ConveyorMk4
from Objects.Conveyors.mk5 import ConveyorMk5

def get_class(obj: RawFactoryObject) -> BaseFactoryObject:
    """Gets the python class of an object from the raw JSON

    Args:
        obj (RawFactoryObject): The raw JSON to find the class for

    Raises:
        KeyError: There is no class associated with this JSON

    Returns:
        BaseFactoryObject: The Python Class
    """
    assert isinstance(classpath:=list(obj.values())[0]["className"], str)
    classname = classpath.removeprefix("").split("/")
    currentitem = dict(objects)
    for path in classname:
        if path == "":
            continue
        try:
            currentitem = currentitem[path] #type: ignore
        except KeyError: #! OBJECT NOT FOUND
            if isinstance(currentitem, BaseFactoryObject): #? If we have a class already
                return currentitem
            print(classname)
            input()
            break
    raise KeyError(f"Object {classname} not found!")



objects = {
    "Game": {
        "FactoryGame": {
            "Buildable": {
                "Factory": {
                    # Splitters
                    "CA_Splitter": Splitter,
                    "CA_SplitterSmart": SmartSplitter,
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
