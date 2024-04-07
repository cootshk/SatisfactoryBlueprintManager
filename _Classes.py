"""Tools to convert raw JSON into the classes"""
from Objects.Conveyors import ConveyorPole
from Objects.Splitters.merger import Merger
from Objects.Splitters.smart import SmartSplitter
from Objects.Splitters.splitter import Splitter
from Objects import BaseFactoryObject, RawFactoryObject
from Objects.Conveyors.mk1 import ConveyorLiftMk1, ConveyorMk1
from Objects.Conveyors.mk2 import ConveyorLiftMk2, ConveyorMk2
from Objects.Conveyors.mk3 import ConveyorLiftMk3, ConveyorMk3
from Objects.Conveyors.mk4 import ConveyorLiftMk4, ConveyorMk4
from Objects.Conveyors.mk5 import ConveyorLiftMk5, ConveyorMk5

def get_class(obj: RawFactoryObject) -> BaseFactoryObject:
    """Gets the python class of an object from the raw JSON

    Args:
        obj (RawFactoryObject): The raw JSON to find the class for

    Raises:
        KeyError: There is no class associated with this JSON

    Returns:
        BaseFactoryObject: A building in satisfactory
    """
    assert isinstance(classpath:=list(obj.values())[0]["className"], str)
    classname = classpath.removeprefix("").split("/")
    currentitem = dict(objects)
    for path in classname:
        if path == "":
            continue
        try:
            print("Finding", path, "in", currentitem)
            currentitem = currentitem[path] #type: ignore
        except TypeError: #! OBJECT FOUND
            #assert isinstance(currentitem, BaseFactoryObject)
            return currentitem #TODO: re-add assertion
        except KeyError: #! OBJECT NOT FOUND
            if isinstance(currentitem, BaseFactoryObject): #? If we have a class already
                return currentitem
            print(classname)
            input()
            break
    #raise KeyError(f"Object {classname} not found!")



objects = {
    "Game": {
        "FactoryGame": {
            "Buildable": {
                "Factory": {
                    # Splitters
                    "CA_Merger": Merger,
                    "CA_Splitter": Splitter,
                    "CA_SplitterSmart": SmartSplitter,
                    # Belts
                    "ConveyorBeltMk1": ConveyorMk1,
                    "ConveyorBeltMk2": ConveyorMk2,
                    "ConveyorBeltMk3": ConveyorMk3,
                    "ConveyorBeltMk4": ConveyorMk4,
                    "ConveyorBeltMk5": ConveyorMk5,
                    "ConveyorPole": ConveyorPole,
                    "ConveyorLiftMk1": ConveyorLiftMk1,
                    "ConveyorLiftMk2": ConveyorLiftMk2,
                    "ConveyorLiftMk3": ConveyorLiftMk3,
                    "ConveyorLiftMk4": ConveyorLiftMk4,
                    "ConveyorLiftMk5": ConveyorLiftMk5,
                    "FoundationPassthrough": None, #TODO: Coneyor Lift Floor Hole
                    
                    # Hypertubes
                    "PipeHyperSupport": None, #TODO: Hypertube Support
                    "PipeHyperStart": None, #TODO: Hypertube Entrance
                    "PipeHyper": None, #TODO: Hypertube
                    
                    # Production
                    "AssemblerMk1": None, #TODO: Assembler(?)
                    
                    # Power
                    "PowerLine": None, #TODO: Power Line
                    "PowerPoleWall": None, #TODO: Wall Power Pole (Mk. 1?)
                    
                    # Signs
                    "SignDigital": {
                        "Build_StandaloneWidgetSign_Medium.Build_StandaloneWidgetSign_Medium_C": None, #TODO: Medium Sign
                        "Build_StandaloneWidgetSign_SmallVeryWide.Build_StandaloneWidgetSign_SmallVeryWide_C": None, #TODO: Large Sign
                    },
                },
                "Building": {
                    "Catwalk": {
                        "Build_CatwalkCross.Build_CatwalkCross_C": None, #TODO: Some catwalk
                    },
                    "Foundation": {
                        "Build_Flat_Frame_01.Build_Flat_Frame_01_C": None
                    },
                },
            },
            "Prototype": {
                "Buildable": {
                    "Beams": {
                        "Build_Beam_Painted.Build_Beam_Painted_C": None,
                    },
                },
            },
        },
    },
    "Script": #{
        NotImplementedError
#    },
}
