"""The parser logic. None of this should be visible to the user"""
# Thanks to @heinrich26 for the parser!

from email import errors
from io import BytesIO
from os import PathLike
import struct, itertools
from typing import Any
import zlib

def pako_inflate(data):
    decompress = zlib.decompressobj(15)
    return decompress.decompress(data) + decompress.flush()

class Building_Conveyor:
    @staticmethod
    def isConveyor(obj: dict) -> bool:
        """
        BELT/LIFT LOOKUP, includes mods to avoid finding them everywhere
        """
        return Building_Conveyor.isConveyorBelt(obj) or Building_Conveyor.isConveyorLift(obj)

    @staticmethod
    def isConveyorBelt(currentObject: dict[str, str] | dict[str, dict[str, str]]) -> bool:
        try:
            assert isinstance(currentObject['className'], str)
            if currentObject['className'] in Building_Conveyor.availableConveyorBelts:
                return True
        
        # Belts Mod
            if (currentObject['className'].startswith('/Conveyors_Mod/Build_BeltMk')
                 or currentObject['className'].startswith('/Game/Conveyors_Mod/Build_BeltMk')
                 or currentObject['className'].startswith('/UltraFastLogistics/Buildable/build_conveyorbeltMK')
                 or currentObject['className'].startswith('/FlexSplines/Conveyor/Build_Belt')
                 or currentObject['className'].startswith('/conveyorbeltmod/Belt/mk')
                 or currentObject['className'].startswith('/minerplus/content/buildable/Factory/belt_')
                 or currentObject['className'].startswith('/bamfp/content/buildable/Factory/belt_')):
                return True
    
            return False
        except KeyError:
            assert isinstance(currentObject, dict)
            return Building_Conveyor.isConveyorBelt(list(currentObject.values())[0]) # type: ignore
    
    @staticmethod
    def isConveyorLift(currentObject: dict[str, str] | dict[str, dict[str, str]]) -> bool:
        try:
            assert isinstance(currentObject['className'], str)
        except KeyError:
            assert isinstance(currentObject, dict)
            return Building_Conveyor.isConveyorLift(list(currentObject.values())[0]) # type: ignore
        
        if currentObject['className'] in Building_Conveyor.availableConveyorLifts:
            return True
        
        # Lifts Mod
        if (currentObject['className'].startswith('/minerplus/content/buildable/Factory/lift')
             or currentObject['className'].startswith('/bamfp/content/buildable/Factory/lift')
             or currentObject['className'].startswith('/Game/Conveyors_Mod/Build_LiftMk')
             or currentObject['className'].startswith('/Conveyors_Mod/Build_LiftMk')
             or currentObject['className'].startswith('/Game/CoveredConveyor')
             or currentObject['className'].startswith('/CoveredConveyor')
             or currentObject['className'].startswith('/conveyorbeltmod/lift/')):
            return True

        return False
    

    availableConveyorBelts = [
        '/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk1/Build_ConveyorBeltMk1.Build_ConveyorBeltMk1_C',
        '/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk2/Build_ConveyorBeltMk2.Build_ConveyorBeltMk2_C',
        '/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk3/Build_ConveyorBeltMk3.Build_ConveyorBeltMk3_C',
        '/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk4/Build_ConveyorBeltMk4.Build_ConveyorBeltMk4_C',
        '/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk5/Build_ConveyorBeltMk5.Build_ConveyorBeltMk5_C'
    ]

    availableConveyorLifts = [
        '/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk1/Build_ConveyorLiftMk1.Build_ConveyorLiftMk1_C',
        '/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk2/Build_ConveyorLiftMk2.Build_ConveyorLiftMk2_C',
        '/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk3/Build_ConveyorLiftMk3.Build_ConveyorLiftMk3_C',
        '/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk4/Build_ConveyorLiftMk4.Build_ConveyorLiftMk4_C',
        '/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk5/Build_ConveyorLiftMk5.Build_ConveyorLiftMk5_C'
    ]
  
  
class DataView:
    def __init__(self, buf: BytesIO | bytearray, bytes_per_element=1, size = None):
        """
        bytes_per_element is the size of each element in bytes.
        By default we are assume the array is one byte per element.
        """
        self.size = size
        self.buf = buf if isinstance(buf, BytesIO) else BytesIO(buf)
        self.bytes_per_element = bytes_per_element # unused

    def get_long(self) -> int:
        return int.from_bytes(self.buf.read(8), 'little', signed=True)

    def get_int_32(self) -> int:
        return int.from_bytes(self.buf.read(4), 'little', signed=True)

    def get_int_8(self) -> int:
        return int.from_bytes(self.buf.read(1), 'little', signed=True)

    def get_uint_8(self) -> int:
        return int.from_bytes(self.buf.read(1), 'little', signed=False)

    def get_uint_16(self) -> int:
        return int.from_bytes(self.buf.read(2), 'little', signed=False)

    def get_uint_32(self) -> int:
        return int.from_bytes(self.buf.read(4), 'little', signed=False)

    def get_float_32(self) -> float:
        return struct.unpack('<f', self.buf.read(4))[0]  # <f for little endian

    def get_float_64(self) -> float:
        return struct.unpack('<f', self.buf.read(8))[0]

class Worker:
    """A class that does nothing. Exists for the sake of copy-paste.
    """
    def __init__(self) -> None:
        pass

    def post_message(self, d: dict):
        """DEBUG - print a dictionary

        Args:
            d (dict): The dictionary to print
        """
        print(d)


class Options:
    """Parser Options
    
    Arguments:
        fname (Path or str): the blueprint file to open
        lang (str, optional): The language to open the blueprint file in. Defaults to en_us.
    """
    def __init__(self, fname: PathLike|str='save.sav', lang='en_us') -> None:
        self.array_buffer = bytearray(open(fname, mode='rb').read())
        self.language = lang


class Parser:
    """Parser - The main parser"""
    currentChunks: list

    def __init__(self, worker: Worker, options: Options) -> None:
        self.worker = worker
        self.objects = dict()
        # Non __init__ options:
        self.PACKAGE_FILE_TAG = 0
        self.last_str_read = 0

        self.language = options.language

        self.array_buffer = options.array_buffer
        self.max_byte = len(self.array_buffer)
        # Still used for header try not to shrink it too much,
        # as modMetadata can be longer than anticipated...
        self.buffer_view = DataView(BytesIO(self.array_buffer))
        # self.current_byte = 0

        self.parse()

    def parse(self):
        pass

    @property
    def current_byte(self):
        """Gets the current byte"""
        return self.buffer_view.buf.tell()

    @current_byte.setter
    def current_byte(self, new_pos):
        self.buffer_view.buf.seek(new_pos, 0)

    def skip_bytes(self, byte_length: int = 1):
        """Skip over bytes"""
        self.buffer_view.buf.seek(byte_length, 1)
        # self.current_byte += byte_length

    def read_byte(self) -> int:
        """
        TO DO super useless method???
        """
        return int(self.buffer_view.get_uint_8())

    def read_hex(self, hexLength) -> str:
        return ''.join(chr(self.buffer_view.get_uint_8()) for _ in range(hexLength))

    def read_int(self) -> int:
        # self.current_byte += 4
        return self.buffer_view.get_int_32()

    def read_int_8(self) -> int:
        # self.current_byte += 1
        return self.buffer_view.get_int_8()

    def read_long(self) -> int:
        return self.buffer_view.get_long()

    def read_float(self) -> float:
        # self.current_byte += 4
        return self.buffer_view.get_float_32()

    def read_double(self) -> float:
        # self.current_byte += 8
        return self.buffer_view.get_float_64()

    def read_string(self) -> str:
        str_length = self.read_int()
        self.last_str_read = str_length
        startBytes = self.current_byte

        if str_length == 0:
            return ''

        # Range error!
        if str_length > (self.max_byte - self.current_byte):
            debug_size = 512
            self.current_byte = max(0, startBytes - (debug_size * 2))
            error_message = (f"Cannot readString ({str_length}):" +
                             f" {self.read_hex(debug_size * 2)}========={self.read_hex(debug_size)}")

            print(error_message)
            self.worker.post_message({'command': 'alertParsing'})
            raise ValueError(error_message)

        # UTF16
        if str_length < 0:
            str_length = -str_length - 1
            s = ''.join(chr(self.buffer_view.get_uint_16())
                        for _ in range(str_length))
            self.skip_bytes(2)
            return s

        try:
            str_length = str_length - 1
            s = ''.join(chr(self.buffer_view.get_uint_8())
                        for _ in range(str_length))
            self.skip_bytes(1)
            return s
        except Exception as error:
            debug_size = 512
            self.current_byte = max(0, startBytes - (debug_size * 2))
            error_message = (f"Cannot readString ({str_length}): " +
                             f"{self.read_hex(debug_size * 2)}========={self.read_hex(debug_size)}")
            print(error)
            self.worker.post_message({'command': 'alertParsing'})
            raise ValueError(error_message) from error

    def readObject(self) -> dict:
        """
        Main objects
        """
        obj = dict()
        obj['className'] = self.read_string()
        obj = self.read_object_property(obj)
        obj['outerPathName'] = self.read_string()

        return obj
    
    def readActor(self):
        actor = self.read_object_property({'className': self.read_string()})
        if (needTransform := self.read_int()) != 0:
            actor['needTransform'] = needTransform # type: ignore

        # {rotation: [0, 0, 0, 1], translation: [0, 0, 0], scale3d: [1, 1, 1]}
        actor['transform'] = { # type: ignore
            'rotation': [self.read_float(), self.read_float(), self.read_float(), self.read_float()],
            'translation': [self.read_float(), self.read_float(), self.read_float()]
        }

        # Enforce bounding on the map to avoid the game from skipping physics!
        if actor['transform']['translation'][0] < -500000 or actor['transform']['translation'][0] > 500000 or actor['transform']['translation'][1] < -500000 or actor['transform']['translation'][1] > 500000 or actor['transform']['translation'][2] < -500000 or actor['transform']['translation'][2] > 500000:
            actor['transform']['translation'] = [0, 0, 2000]
            print('Out of bounds translation', actor['pathName'])
        # Avoid lost vehicles in the game!
        if None in actor['transform']['translation']:
            actor['transform']['translation'] = [0, 0, 2000]
            print('NaN translation', actor['pathName'])

        if (scale3d := [self.read_float() for _ in range(3)]) != [1.0, 1.0, 1.0]:
            actor['transform']['scale3d'] = scale3d
        
        if (wasPlacedInLevel := self.read_int()) != 0: # TO DO: Switch to 1?
            actor['wasPlacedInLevel'] = wasPlacedInLevel # type: ignore

        return actor

    def readEntity(self, objectKey):
        entityLength = self.read_int()
        startByte = self.current_byte

        if not 'outerPathName' in self.objects[objectKey]:
            self.objects[objectKey]['entity'] = self.read_object_property(dict())

            if (countChild := self.read_int()) > 0:
                self.objects[objectKey]['children'] = [self.read_object_property(dict()) for _ in countChild] # type: ignore
            
        if (self.current_byte - startByte) == entityLength:
            self.objects[objectKey]['shouldBeNulled'] = True
            return
        
        # Read properties
        self.objects[objectKey]['properties'] = []
        while True:
            read_property = self.readProperty(self.objects[objectKey]['className'], objectKey) # type: ignore
            if read_property is None:
                break

            if read_property['name'] != 'CachedActorTransform': # Should be removed on release
                self.objects[objectKey]['properties'].append(read_property)

        # Read Conveyor missing bytes
        if Building_Conveyor.isConveyor(self.objects[objectKey]):
            self.objects[objectKey]['extra'] = { 'count': self.read_int(), 'items': [] }
            itemsLength = self.read_int()
            for _ in range(itemsLength):
                currentItem = dict()
                currentItemLength = self.read_int()
                if currentItemLength != 0:
                    currentItem.length = currentItemLength # type: ignore
                currentItem['name'] = self.read_string()
                self.read_string() # currentItem.levelName   = self.readString()
                self.read_string() # currentItem.pathName    = self.readString()
                currentItem['position'] = self.read_float()

                self.objects[objectKey]['extra']['items'].append(currentItem)
        else:
            # Extra processing
            match self.objects[objectKey]['className']:
                case '/Game/FactoryGame/-Shared/Blueprint/BP_GameState.BP_GameState_C', '/Game/FactoryGame/-Shared/Blueprint/BP_GameMode.BP_GameMode_C':
                    self.objects[objectKey]['extra'] = { 'count': self.read_int(), 'game': [] }
                    gameLength = self.read_int()
                    self.objects[objectKey]['extra']['game'] = [self.read_object_property(dict()) for _ in range(gameLength)]
                # in Blueprints, there are no Players!
                # case '/Game/FactoryGame/Character/Player/BP_PlayerState.BP_PlayerState_C':
                #    pass
                # TO DO: Not 0 here so bypass those special cases, but why? We mainly do not want to get warned here...
                case '/Game/FactoryGame/Buildable/Factory/DroneStation/BP_DroneTransport.BP_DroneTransport_C':
                    missingDrone = (startByte + entityLength) - self.current_byte
                    self.objects[objectKey]['missing'] = self.read_hex(missingDrone)
                case '/Game/FactoryGame/-Shared/Blueprint/BP_CircuitSubsystem.BP_CircuitSubsystem_C':
                    self.objects[objectKey]['extra'] = { 'count': self.read_int(), 'circuits': [] }
                    circuitsLength = self.read_int()

                    self.objects[objectKey]['extra']['circuits'] = [{
                            'circuitId': self.read_int(),
                            'levelName': self.read_string(),
                            'pathName': self.read_string()
                        } for _ in range(circuitsLength)]
                case '/Game/FactoryGame/Buildable/Factory/PowerLine/Build_PowerLine.Build_PowerLine_C', '/Game/FactoryGame/Events/Christmas/Buildings/PowerLineLights/Build_XmassLightsLine.Build_XmassLightsLine_C', '/FlexSplines/PowerLine/Build_FlexPowerline.Build_FlexPowerline_C', '/AB_CableMod/Visuals1/Build_AB-PLCopper.Build_AB-PLCopper_C', '/AB_CableMod/Visuals1/Build_AB-PLCaterium.Build_AB-PLCaterium_C', '/AB_CableMod/Visuals3/Build_AB-PLHeavy.Build_AB-PLHeavy_C', '/AB_CableMod/Visuals4/Build_AB-SPLight.Build_AB-SPLight_C', '/AB_CableMod/Visuals3/Build_AB-PLPaintable.Build_AB-PLPaintable_C':
                    self.objects[objectKey]['extra'] = {
                        'count': self.read_int(),
                        'source': self.read_object_property(dict()),
                        'target': self.read_object_property(dict())
                    }

                    # 2022-10-18: Added Cached locations for wire locations for use in visualization in blueprint hologram (can't depend on connection components)
                    if (self.header.saveVersion >= 33): # type: ignore
                        self.objects[objectKey]['extra']['sourceTranslation'] = [self.read_float(), self.read_float(), self.read_float()]
                        self.objects[objectKey]['extra']['targetTranslation'] = [self.read_float(), self.read_float(), self.read_float()]
                case '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C', '/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/BP_FreightWagon.BP_FreightWagon_C', '/x3_mavegrag/Vehicles/Trains/Locomotive_Mk1/BP_X3Locomotive_Mk1.BP_X3Locomotive_Mk1_C', '/x3_mavegrag/Vehicles/Trains/CargoWagon_Mk1/BP_X3CargoWagon_Mk1.BP_X3CargoWagon_Mk1_C':
                    self.objects[objectKey]['extra'] = { 'count': self.read_int(), 'objects': [] }
                    trainLength = self.read_int()
                    self.objects[objectKey]['extra']['objects'] = [{
                            'name': self.read_string(),
                            'unk': self.read_hex(53)
                        } for _ in range(trainLength)]

                    self.objects[objectKey]['extra']['previous'] = self.read_object_property(dict())
                    self.objects[objectKey]['extra']['next'] = self.read_object_property(dict())
                case '/Game/FactoryGame/Buildable/Vehicle/Tractor/BP_Tractor.BP_Tractor_C', '/Game/FactoryGame/Buildable/Vehicle/Truck/BP_Truck.BP_Truck_C', '/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_Explorer.BP_Explorer_C', '/Game/FactoryGame/Buildable/Vehicle/Cyberwagon/Testa_BP_WB.Testa_BP_WB_C', '/Game/FactoryGame/Buildable/Vehicle/Golfcart/BP_Golfcart.BP_Golfcart_C', '/Game/FactoryGame/Buildable/Vehicle/Golfcart/BP_GolfcartGold.BP_GolfcartGold_C', '/x3_mavegrag/Vehicles/Trucks/TruckMk1/BP_X3Truck_Mk1.BP_X3Truck_Mk1_C':
                    self.objects[objectKey]['extra'] = { 'count': self.read_int(), 'objects': [] }
                    vehicleLength = self.read_int()
                    self.objects[objectKey]['extra']['objects'] = [{
                            'name': self.read_string(),
                            'unk': self.read_hex(53)
                        } for _ in range(vehicleLength)]
                case _:
                    missing_bytes = (startByte + entityLength) - self.current_byte
                    if missing_bytes > 4:
                        self.objects[objectKey]['missing'] = self.read_hex(missing_bytes) # TO DO
                        print(f'MISSING {missing_bytes} BYTES', self.objects[objectKey])
                    else:
                        self.skipBytes(4) # type: ignore

    #Reading Properties
    def read_object_property(self, currentProperty):
        if (levelName := self.read_string()) != self.header['mapName']: # type: ignore
            currentProperty['levelName'] = levelName
            currentProperty['pathName'] = self.read_string()
        else:
            currentProperty.pathName = self.read_string()
            # currentProperty.pathName    = this.readString().replace(this.header.mapName + ':', '');

        return currentProperty
    

    def readFINGPUT1BufferPixel(self):
        """
        FicsIt-Networks properties
        """
        return {
            'character': self.read_hex(2),
            'foregroundColor': {
                'r': self.read_float(),
                'g': self.read_float(),
                'b': self.read_float(),
                'a': self.read_float()
            },
            'backgroundColor': {
                'r': self.read_float(),
                'g': self.read_float(),
                'b': self.read_float(),
                'a': self.read_float()
            }
        }

    # https://github.com/CoderDE/FicsIt-Networks/blob/ab918a81a8a7527aec0cf6cd35270edfc5a1ddfe/Source/FicsItNetworks/Network/FINNetworkTrace.cpp#L154
    def readFINNetworkTrace(self):
        data = dict()
        data['levelName'] = self.read_string()
        data['pathName'] = self.read_string()

        hasPrev = self.read_int()
        if hasPrev == 1:
            data.prev = self.readFINNetworkTrace() # type: ignore

        has_step = self.read_int()
        if has_step == 1:
            data['step'] = self.read_string()

        return data

    # https://github.com/CoderDE/FicsIt-Networks/blob/master/Source/FicsItNetworks/FicsItKernel/Processor/Lua/LuaProcessorStateStorage.cpp#L6
    def readFINLuaProcessorStateStorage(self):
        """Reads the Lua Processor Storage"""
        data = {'trace': [self.readFINNetworkTrace() for i in range(
            self.read_int())], 'reference': [{
                'levelName': self.read_string(),
                'pathName': self.read_string()
            } for _ in range(self.readInt())], 'structs': []} # type: ignore

        data['thread'] = self.read_string()
        data['globals'] = self.read_string()


        def read_struct() -> dict:
            structure = {
                'unk1': self.read_int(),
                'unk2': self.read_string()
            }
            match structure['unk2']:
                case '/Script/CoreUObject.Vector':
                    structure['x'] = self.read_float()
                    structure['y'] = self.read_float()
                    structure['z'] = self.read_float()
                case '/Script/CoreUObject.LinearColor':
                    structure['r'] = self.read_float()
                    structure['g'] = self.read_float()
                    structure['b'] = self.read_float()
                    structure['a'] = self.read_float()
                case '/Script/FactoryGame.InventoryStack':
                    structure['unk3'] = self.read_int()
                    structure['unk4'] = self.read_string()
                    structure['unk5'] = self.read_int()
                    structure['unk6'] = self.read_int()
                    structure['unk7'] = self.read_int()
                case '/Script/FactoryGame.ItemAmount':
                    structure['unk3'] = self.read_int()
                    structure['unk4'] = self.read_string()
                    structure['unk5'] = self.read_int()
                case '/Script/FicsItNetworks.FINTrackGraph':
                    structure['trace'] = self.readFINNetworkTrace()
                    structure['trackId'] = self.read_int()
                case '/Script/FactoryGame.PrefabSignData': pass  # Skip!
                case '/Script/FicsItNetworks.FINInternetCardHttpRequestFuture': pass  # Skip!
                case '/Script/FactoryGame.InventoryItem': pass  # Skip!
                case '/Script/FicsItNetworks.FINGPUT1Buffer':
                    structure['x'] = self.read_int()
                    structure['y'] = self.read_int()
                    structure['size'] = self.read_int()
                    structure['name'] = self.read_string()
                    structure['type'] = self.read_string()
                    structure['length'] = self.read_int()
                    structure['buffer'] = [self.readFINGPUT1BufferPixel()
                                           for _ in range(structure['size'])]
                    structure['unk3'] = self.read_hex(45)  # TO DO: Not sure at all!
                case _:
                    self.worker.post_message({'command': 'alertParsing'})

                    raise ValueError(
                        f"Unimplemented {structure['unk2']} in readFINLuaProcessorStateStorage")

            return structure

        countStructs = self.read_int()
        data['structs'] = [read_struct() for _ in range(countStructs)]
        
        return data

class BlueprintParser(Parser):
    """The main class. Parses your blueprints"""
    def __init__(self, worker: Worker, options: Options) -> None:
        super().__init__(worker, options)
        return

    def parse(self):
        self.header = dict()
        self.header['saveHeaderType'] = self.read_int()  # unknown
        self.header['saveVersion'] = self.read_int() # unknown
        self.header['buildVersion'] = self.read_int() # unknown
        self.header['mapName'] = self.read_int() # unknown
        self.header['mapOptions'] = self.read_int() # unknown
        self.header['sessionName'] = self.read_int() # unknown
        
        self.resources = {}
        
        for _ in range(self.read_int()):
            objType = self.read_int()
            if objType != 0:
                raise Exception("UNKNOWN TYPE")
            # Attention, "dict[key] = value" is evaluated RIGHT-TO-LEFT!!!
            self.resources.__setitem__(self.read_string(), self.read_int())

        self.parts = [self.read_string() if (objType := self.read_int()) == 0
                        else print("UNKNOWN TYPE")
                        for _ in range(self.read_int())]
        
        print(f"resources: {self.resources},\nparts: {self.parts}")

        # We should now unzip the body!
        # Remove the header...
        print(f"Unzipping... current_byte: {self.current_byte}")
        self.array_buffer = self.array_buffer[self.current_byte:]

        self.handledByte = 0
        self.current_byte = 0
        self.max_byte = len(self.array_buffer)

        self.PACKAGE_FILE_TAG = None
        self.maxChunkSize = None
        self.currentChunks = []

        return self.inflateChunks()
        

    def inflateChunks(self):
        """
        Progress bar from 0 to 30%
        """
        while self.handledByte < self.max_byte:
            # Read chunk info size...
            chunk_header = DataView(self.array_buffer[0:48])
            self.current_byte = 48
            self.handledByte += 48

            if self.PACKAGE_FILE_TAG is None:
                # self.PACKAGE_FILE_TAG = chunk_header.getBigInt64(0, true)
                self.PACKAGE_FILE_TAG = chunk_header.get_uint_32()
                self.worker.post_message({ 'command': 'transferData', 'data': { 'PACKAGE_FILE_TAG': self.PACKAGE_FILE_TAG } })
            
            if (self.maxChunkSize is None):
                chunk_header.buf.seek(8, 0)
                self.maxChunkSize = chunk_header.get_uint_32()
                self.worker.post_message({ 'command': 'transferData', 'data': { 'maxChunkSize': self.maxChunkSize } })
            
            chunk_header.buf.seek(16, 0)
            # TO DO Chunk-Size is weird
            currentChunkSize = chunk_header.get_uint_32()
            print(f"ChunkSize: {currentChunkSize}")
            if self.array_buffer[self.current_byte:self.current_byte + 1] == b'\x00':
                self.current_byte += 1
                self.handledByte += 1
                # TO DO bit aligning ???
            currentChunk = self.array_buffer[self.current_byte:
                                            self.current_byte + currentChunkSize]
            self.handledByte += currentChunkSize
            self.current_byte += currentChunkSize

            # Free memory from previous chunk...
            self.array_buffer = self.array_buffer[self.current_byte:]
            self.current_byte = 0

            # Unzip!
            try:
                # Inflate current chunk
                currentInflatedChunk = None
                currentInflatedChunk = pako_inflate(currentChunk)
                self.currentChunks.append(currentInflatedChunk)
            except Exception as error:
                self.worker.post_message({ 'command': 'alert', 'message': 'Something went wrong while trying to inflate your savegame. It seems to be related to adblock and we are looking into it.' })                

                raise error
            

            currentPercentage = round(self.handledByte / self.max_byte * 100)
            self.worker.post_message({ 'command': 'loaderMessage', 'message': 'Inflating save game (%1$s%)...', 'replace': currentPercentage })
            self.worker.post_message({ 'command': 'loaderProgress', 'percentage': (currentPercentage * 0.3) })
        

        del self.array_buffer
        print(f'Inflated: {len(self.currentChunks)} chunks...')
        self.worker.post_message({ 'command': 'loaderMessage', 'message': 'Merging inflated chunks...' })

        tempChunk = bytearray(itertools.chain(*self.currentChunks))

        # Parse them as usual while skipping the first 4 bytes!
        del self.currentChunks
        self.max_byte = len(tempChunk)
        self.buffer_view = DataView(tempChunk)
        self.buffer_view.buf.seek(4, 0)

        if self.header['saveVersion'] >= 29:
            # unused number
            nbLevels = self.read_int()
            # print(f"nbLevels: {nbLevels}")


            countObjects = self.read_int()
            print(f"Object Count: {countObjects}")
            entitiesToObjects = []

            for _ in range(countObjects):
                objectType = self.read_int()
                match objectType:
                    case 0:
                        obj = self.readObject()
                        self.objects[obj['pathName']] = obj
                        entitiesToObjects.append(obj['pathName'])
                    case 1:
                        actor = self.readActor()
                        self.objects[actor['pathName']] = actor
                        entitiesToObjects.append(actor['pathName'])
                    case _:
                        entitiesToObjects.append(None)
                        print('Unknown object type', objectType)
               
            self.worker.post_message({ 'command': 'endSaveLoading' })
            return
        

        return self.parseObjects() # type: ignore


