# Thanks to @heinrich26 for the parser!

from io import BytesIO
import struct, itertools
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
    def isConveyorBelt(currentObject) -> bool:
        if currentObject['className'] in Building_Conveyor.availableConveyorBelts:
            return True
        
        # Belts Mod
        if (currentObject['className'].startsWith('/Conveyors_Mod/Build_BeltMk')
             or currentObject['className'].startsWith('/Game/Conveyors_Mod/Build_BeltMk')
             or currentObject['className'].startsWith('/UltraFastLogistics/Buildable/build_conveyorbeltMK')
             or currentObject['className'].startsWith('/FlexSplines/Conveyor/Build_Belt')
             or currentObject['className'].startsWith('/conveyorbeltmod/Belt/mk')
             or currentObject['className'].startsWith('/minerplus/content/buildable/Factory/belt_')
             or currentObject['className'].startsWith('/bamfp/content/buildable/Factory/belt_')):
            return True

        return False
    
    @staticmethod
    def isConveyorLift(currentObject) -> bool:
        if currentObject['className'] in Building_Conveyor.availableConveyorLifts:
            return True
        
        # Lifts Mod
        if (currentObject['className'].startsWith('/minerplus/content/buildable/Factory/lift')
             or currentObject['className'].startsWith('/bamfp/content/buildable/Factory/lift')
             or currentObject['className'].startsWith('/Game/Conveyors_Mod/Build_LiftMk')
             or currentObject['className'].startsWith('/Conveyors_Mod/Build_LiftMk')
             or currentObject['className'].startsWith('/Game/CoveredConveyor')
             or currentObject['className'].startsWith('/CoveredConveyor')
             or currentObject['className'].startsWith('/conveyorbeltmod/lift/')):
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
    def __init__(self) -> None:
        pass

    def postMessage(self, d: dict):
        print(d)


class Options:
    def __init__(self, fname='save.sav', lang='de_de') -> None:
        self.arrayBuffer = bytearray(open(fname, mode='rb').read())
        self.language = lang


class Parser:
    currentChunks: list

    def __init__(self, worker: Worker, options: Options) -> None:
        self.worker = worker
        self.objects = dict()

        self.language = options.language

        self.arrayBuffer = options.arrayBuffer
        self.maxByte = len(self.arrayBuffer)
        # Still used for header try not to shrink it too much as modMetadata can be longer than anticipated...
        self.bufferView = DataView(BytesIO(self.arrayBuffer))
        # self.currentByte = 0

        self.parse()

    def parse(self):
        pass

    @property
    def currentByte(self):
        return self.bufferView.buf.tell()

    @currentByte.setter
    def currentByte(self, new_pos):
        self.bufferView.buf.seek(new_pos, 0)

    def skip_bytes(self, byteLength: int = 1):
        self.bufferView.buf.seek(byteLength, 1)
        # self.currentByte += byteLength

    def read_byte(self) -> int:
        """
        TODO super useless method???
        """
        return int(self.bufferView.get_uint_8())

    def read_hex(self, hexLength) -> str:
        return ''.join(chr(self.bufferView.get_uint_8()) for _ in range(hexLength))

    def read_int(self) -> int:
        # self.currentByte += 4
        return self.bufferView.get_int_32()

    def read_int_8(self) -> int:
        # self.currentByte += 1
        return self.bufferView.get_int_8()

    def read_long(self) -> int:
        return self.bufferView.get_long()

    def read_float(self) -> float:
        # self.currentByte += 4
        return self.bufferView.get_float_32()

    def read_double(self) -> float:
        # self.currentByte += 8
        return self.bufferView.get_float_64()

    def read_string(self) -> str:
        strLength = self.read_int()
        self.lastStrRead = strLength
        startBytes = self.currentByte

        if strLength == 0:
            return ''

        # Range error!
        if strLength > (self.maxByte - self.currentByte):
            debugSize = 512
            self.currentByte = max(0, startBytes - (debugSize * 2))
            errorMessage = f"Cannot readString ({strLength}): {self.read_hex(debugSize * 2)}========={self.read_hex(debugSize)}"
            print(errorMessage)
            self.worker.postMessage({'command': 'alertParsing'})
            raise Exception(errorMessage)

        # UTF16
        if (strLength < 0):
            strLength = -strLength - 1
            s = ''.join(chr(self.bufferView.get_uint_16())
                        for _ in range(strLength))
            self.skip_bytes(2)
            return s

        try:
            strLength = strLength - 1
            s = ''.join(chr(self.bufferView.get_uint_8())
                        for _ in range(strLength))
            self.skip_bytes(1)
            return s
        except Exception as error:
            debugSize = 512
            self.currentByte = max(0, startBytes - (debugSize * 2))
            errorMessage = f"Cannot readString ({strLength}): {self.read_hex(debugSize * 2)}========={self.read_hex(debugSize)}"
            print(error)
            self.worker.postMessage({'command': 'alertParsing'})
            raise Exception(errorMessage)

    def readObject(self) -> dict:
        """
        Main objects
        """
        object = dict()
        object['className'] = self.read_string()
        object = self.readObjectProperty(object)
        object['outerPathName'] = self.read_string()

        return object
    
    def readActor(self):
        actor = self.readObjectProperty({'className': self.read_string()})

        if (needTransform := self.read_int()) != 0:
            actor['needTransform'] = needTransform

        # {rotation: [0, 0, 0, 1], translation: [0, 0, 0], scale3d: [1, 1, 1]}
        actor['transform'] = {
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
        
        if (wasPlacedInLevel := self.read_int()) != 0: # TODO: Switch to 1?
            actor['wasPlacedInLevel'] = wasPlacedInLevel

        return actor

    def readEntity(self, objectKey):
        entityLength = self.read_int()
        startByte = self.currentByte

        if not 'outerPathName' in self.objects[objectKey]:
            self.objects[objectKey]['entity'] = self.readObjectProperty(dict())

            if (countChild := self.read_int()) > 0:
                self.objects[objectKey]['children'] = [self.readObjectProperty(dict()) for _ in countChild]
            
        if (self.currentByte - startByte) == entityLength:
            self.objects[objectKey]['shouldBeNulled'] = True
            return
        
        # Read properties
        self.objects[objectKey]['properties'] = []
        while True:
            property = self.readProperty(self.objects[objectKey]['className'], objectKey)
            if property is None:
                break

            if property['name'] != 'CachedActorTransform': # Should be removed on release
                self.objects[objectKey]['properties'].append(property)

        # Read Conveyor missing bytes
        if Building_Conveyor.isConveyor(self.objects[objectKey]):
            self.objects[objectKey]['extra'] = { 'count': self.read_int(), 'items': [] }
            itemsLength = self.read_int()
            for _ in range(itemsLength):
                currentItem = dict()
                currentItemLength = self.read_int()
                if currentItemLength != 0:
                    currentItem.length = currentItemLength
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
                    self.objects[objectKey]['extra']['game'] = [self.readObjectProperty(dict()) for _ in range(gameLength)]
                # in Blueprints, there are no Players!
                # case '/Game/FactoryGame/Character/Player/BP_PlayerState.BP_PlayerState_C':
                #    pass
                # TODO: Not 0 here so bypass those special cases, but why? We mainly do not want to get warned here...
                case '/Game/FactoryGame/Buildable/Factory/DroneStation/BP_DroneTransport.BP_DroneTransport_C':
                    missingDrone = (startByte + entityLength) - self.currentByte
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
                        'source': self.readObjectProperty(dict()),
                        'target': self.readObjectProperty(dict())
                    }

                    # 2022-10-18: Added Cached locations for wire locations for use in visualization in blueprint hologram (can't depend on connection components)
                    if (self.header.saveVersion >= 33):
                        self.objects[objectKey]['extra']['sourceTranslation'] = [self.read_float(), self.read_float(), self.read_float()]
                        self.objects[objectKey]['extra']['targetTranslation'] = [self.read_float(), self.read_float(), self.read_float()]
                case '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C', '/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/BP_FreightWagon.BP_FreightWagon_C', '/x3_mavegrag/Vehicles/Trains/Locomotive_Mk1/BP_X3Locomotive_Mk1.BP_X3Locomotive_Mk1_C', '/x3_mavegrag/Vehicles/Trains/CargoWagon_Mk1/BP_X3CargoWagon_Mk1.BP_X3CargoWagon_Mk1_C':
                    self.objects[objectKey]['extra'] = { 'count': self.read_int(), 'objects': [] }
                    trainLength = self.read_int()
                    self.objects[objectKey]['extra']['objects'] = [{
                            'name': self.read_string(),
                            'unk': self.read_hex(53)
                        } for _ in range(trainLength)]

                    self.objects[objectKey]['extra']['previous'] = self.readObjectProperty(dict())
                    self.objects[objectKey]['extra']['next'] = self.readObjectProperty(dict())
                case '/Game/FactoryGame/Buildable/Vehicle/Tractor/BP_Tractor.BP_Tractor_C', '/Game/FactoryGame/Buildable/Vehicle/Truck/BP_Truck.BP_Truck_C', '/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_Explorer.BP_Explorer_C', '/Game/FactoryGame/Buildable/Vehicle/Cyberwagon/Testa_BP_WB.Testa_BP_WB_C', '/Game/FactoryGame/Buildable/Vehicle/Golfcart/BP_Golfcart.BP_Golfcart_C', '/Game/FactoryGame/Buildable/Vehicle/Golfcart/BP_GolfcartGold.BP_GolfcartGold_C', '/x3_mavegrag/Vehicles/Trucks/TruckMk1/BP_X3Truck_Mk1.BP_X3Truck_Mk1_C':
                    self.objects[objectKey]['extra'] = { 'count': self.read_int(), 'objects': [] }
                    vehicleLength = self.read_int()
                    self.objects[objectKey]['extra']['objects'] = [{
                            'name': self.read_string(),
                            'unk': self.read_hex(53)
                        } for _ in range(vehicleLength)]
                case _:
                    missingBytes = (startByte + entityLength) - self.currentByte
                    if missingBytes > 4:
                        self.objects[objectKey]['missing'] = self.read_hex(missingBytes) # TODO
                        print(f'MISSING {missingBytes} BYTES', self.objects[objectKey])
                    else:
                        self.skipBytes(4)

    """
    Reading Properties
    """
    def readObjectProperty(self, currentProperty):
        if (levelName := self.read_string()) != self.header['mapName']:
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
            data.prev = self.readFINNetworkTrace()

        hasStep = self.read_int()
        if hasStep == 1:
            data['step'] = self.read_string()

        return data

    # https://github.com/CoderDE/FicsIt-Networks/blob/master/Source/FicsItNetworks/FicsItKernel/Processor/Lua/LuaProcessorStateStorage.cpp#L6
    def readFINLuaProcessorStateStorage(self):
        data = {'trace': [self.readFINNetworkTrace() for i in range(
            self.read_int())], 'reference': [{
                'levelName': self.read_string(),
                'pathName': self.read_string()
            } for _ in range(self.readInt())], 'structs': []}

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
                    structure['unk3'] = self.read_hex(45)  # TODO: Not sure at all!
                case _:
                    self.worker.postMessage({'command': 'alertParsing'})

                    raise Exception(f"Unimplemented {structure['unk2']} in readFINLuaProcessorStateStorage")

            return structure

        countStructs = self.read_int()
        data['structs'] = [read_struct() for _ in range(countStructs)]
        
        return data

class BlueprintParser(Parser):
    def __init__(self, worker: Worker, options: Options) -> None:
        super().__init__(worker, options)

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
        print(f"Unzipping... currentByte: {self.currentByte}")
        self.arrayBuffer = self.arrayBuffer[self.currentByte:]

        self.handledByte = 0
        self.currentByte = 0
        self.maxByte = len(self.arrayBuffer)

        self.PACKAGE_FILE_TAG = None
        self.maxChunkSize = None
        self.currentChunks = []

        return self.inflateChunks()
        

    def inflateChunks(self):
        """
        Progress bar from 0 to 30%
        """
        while self.handledByte < self.maxByte:
            # Read chunk info size...
            chunkHeader = DataView(self.arrayBuffer[0:48])
            self.currentByte = 48
            self.handledByte += 48

            if self.PACKAGE_FILE_TAG is None:
                # self.PACKAGE_FILE_TAG = chunkHeader.getBigInt64(0, true)
                self.PACKAGE_FILE_TAG = chunkHeader.get_uint_32()
                self.worker.postMessage({ 'command': 'transferData', 'data': { 'PACKAGE_FILE_TAG': self.PACKAGE_FILE_TAG } })
            
            if (self.maxChunkSize is None):
                chunkHeader.buf.seek(8, 0)
                self.maxChunkSize = chunkHeader.get_uint_32()
                self.worker.postMessage({ 'command': 'transferData', 'data': { 'maxChunkSize': self.maxChunkSize } })
            
            chunkHeader.buf.seek(16, 0)
            # TODO Chunk-Size is weird
            currentChunkSize = chunkHeader.get_uint_32()
            print(f"ChunkSize: {currentChunkSize}")
            if self.arrayBuffer[self.currentByte:self.currentByte + 1] == b'\x00':
                self.currentByte += 1
                self.handledByte += 1
                # TODO bit aligning ???
            currentChunk = self.arrayBuffer[self.currentByte:
                                            self.currentByte + currentChunkSize]
            self.handledByte += currentChunkSize
            self.currentByte += currentChunkSize

            # Free memory from previous chunk...
            self.arrayBuffer = self.arrayBuffer[self.currentByte:]
            self.currentByte = 0

            # Unzip!
            try:
                # Inflate current chunk
                currentInflatedChunk = None
                currentInflatedChunk = pako_inflate(currentChunk)
                self.currentChunks.append(currentInflatedChunk)
            except Exception as error:
                self.worker.postMessage({ 'command': 'alert', 'message': 'Something went wrong while trying to inflate your savegame. It seems to be related to adblock and we are looking into it.' })                

                raise error
            

            currentPercentage = round(self.handledByte / self.maxByte * 100)
            self.worker.postMessage({ 'command': 'loaderMessage', 'message': 'Inflating save game (%1$s%)...', 'replace': currentPercentage })
            self.worker.postMessage({ 'command': 'loaderProgress', 'percentage': (currentPercentage * 0.3) })
        

        del self.arrayBuffer
        print(f'Inflated: {len(self.currentChunks)} chunks...')
        self.worker.postMessage({ 'command': 'loaderMessage', 'message': 'Merging inflated chunks...' })

        tempChunk = bytearray(itertools.chain(*self.currentChunks))

        # Parse them as usual while skipping the first 4 bytes!
        del self.currentChunks
        self.maxByte = len(tempChunk)
        self.bufferView = DataView(tempChunk)
        self.bufferView.buf.seek(4, 0)

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
                        object = self.readObject()
                        self.objects[object['pathName']] = object
                        entitiesToObjects.append(object['pathName'])
                    case 1:
                        actor = self.readActor()
                        self.objects[actor['pathName']] = actor
                        entitiesToObjects.append(actor['pathName'])
                    case _:
                        entitiesToObjects.append(None)
                        print('Unknown object type', objectType)
               
            self.worker.postMessage({ 'command': 'endSaveLoading' })
            return
        

        return self.parseObjects()





if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        prog="Satisfactory Blueprint Info",
        description="Gets information about a satisfactory blueprint"
    )
    parser.add_argument("--file", "-f", default=None, required=False)
    parser.add_argument("--cli", "-c", action="store_true", required=False)
    args = parser.parse_args()
    if args.cli: 
        print(f"Parsing {str(args.file)}!")
        assert os.path.isfile(args.file) and str(args.file).removesuffix("/").endswith(".sbp")
        p = BlueprintParser(Worker(), Options(args.file))
        print(p.objects)
    else:
        # GUI
        import os
        import tkinter as tk
        from tkinter.filedialog import askopenfilename

        window = tk.Tk()
        window.wm_title("SBM v1.0")
        greeting = tk.Label(text="Satisfactory Blueprint Manager")
        greeting.pack()
        #label = tk.Label(text="Blueprint File Path: ")
        submitbutton = tk.Button(
            text="Choose File",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
        )
        #label.pack()
        #submitbutton.pack()
        filetypes = (
            ('Satisfactory Blueprint Files', '*.sbp'),
            ('All files', '*.*'),
        )
        filename = askopenfilename(
            filetypes=filetypes, 
            initialdir=os.path.expandvars(r'%LOCALAPPDATA%\FactoryGame\Saved\SaveGames\blueprints') if os.name == "nt" else None # C:\Users\___\AppData\Local\FactoryGame\Saved\SaveGames\blueprints\Atlass Factory
        ) 
        assert os.path.isfile(filename)

        p = BlueprintParser(filename)
        window.mainloop()
    