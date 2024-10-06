#include "iostream"
#include "string"

using namespace std;

string get_icon_name(const int& id) {
    /* {
    "1": "The HUB",
    "2": "Craft Bench",
    "3": "Equipment Workshop",
    "4": "Smelter",
    "5": "Power Line",
    "6": "Constructor",
    "7": "Power Pole Mk.1",
    "8": "Conveyor Pole",
    "9": "Conveyor Belt Mk.1",
    "10": "Miner Mk.1",
    "11": "Storage Container",
    "12": "Space Elevator",
    "13": "Biomass Burner",
    "14": "Giant FICSMAS Tree",
    "15": "Green Screen Wall 8m x 4m",
    "16": "Foundation 4x16",
    "17": "Green Screen Foundation 8m x 4m",
    "18": "Ceiling Light",
    "19": "Wall Mounted Flood Light",
    "20": "Flood Light Tower",
    "21": "Lights Control Panel",
    "22": "Resource Well Pressurizer",
    "23": "Resource Well Extractor",
    "24": "WalkwayStairs_01",
    "25": "Ladder",
    "26": "Drone Port",
    "27": "Fence",
    "28": "Stairs",
    "29": "Panel Window",
    "31": "Old Jump Pad",
    "32": "Power Pole Mk.2",
    "33": "Wall Outlet Mk.2",
    "34": "Double Wall Outlet Mk.2",
    "35": "Smart Splitter",
    "36": "Converter",
    "37": "Remote Storage",
    "38": "Lookout Tower",
    "39": "Foundation 8m x 1m",
    "40": "Foundation 8m x 2m",
    "41": "Ramp 8m x 1m",
    "42": "Ramp 8m x 2m",
    "43": "Ramp 8m x 4m",
    "44": "Wall 8m x 4m",
    "45": "Conveyor Splitter",
    "46": "Conveyor Merger",
    "47": "Conveyor Lift Mk.1",
    "48": "MAM",
    "49": "Personal Storage Box",
    "51": "Wall Conveyor x3",
    "52": "Wall Conveyor x2",
    "53": "Wall Conveyor x1",
    "54": "Wall Conveyor x3",
    "55": "Wall Conveyor x2",
    "56": "Wall Conveyor x1",
    "57": "Stairs Left",
    "58": "Stairs Right",
    "59": "Assembler",
    "60": "U-Jelly Landing Pad",
    "61": "Walkway Straight",
    "62": "Walkway Crossing",
    "63": "Walkway T-Crossing",
    "64": "Walkway Turn",
    "65": "AWESOME Sink",
    "66": "AWESOME Shop",
    "67": "Coal Generator",
    "68": "Water Extractor",
    "69": "Pipeline Mk.1",
    "70": "Pipeline Support",
    "71": "Pipeline Junction Cross",
    "72": "Pipeline Pump Mk.1",
    "73": "Fluid Buffer",
    "74": "Conveyor Belt Mk.2",
    "75": "Stackable Conveyor Pole",
    "76": "Conveyor Lift Mk.2",
    "77": "Truck Station",
    "78": "Foundry",
    "79": "Miner Mk.2",
    "80": "Hypertube Entrance",
    "81": "Hypertube",
    "82": "Hypertube Support",
    "83": "Stackable Hypertube Support",
    "84": "Oil Extractor",
    "85": "Refinery",
    "86": "Valve",
    "87": "Manufacturer",
    "88": "Power Storage",
    "89": "Industrial Storage Container",
    "90": "Conveyor Belt Mk.3",
    "91": "Conveyor Lift Mk.3",
    "92": "Stackable Pipeline Support",
    "93": "Packager",
    "94": "Industrial Fluid Buffer",
    "95": "Fuel Generator",
    "96": "Conveyor Belt Mk.4",
    "97": "Conveyor Lift Mk.4",
    "98": "Railway",
    "99": "Train Station",
    "100": "Freight Platform",
    "101": "Fluid Freight Platform",
    "102": "Empty Platform",
    "103": "Pipeline Mk.2",
    "104": "Pipeline Pump Mk.2",
    "105": "Blender",
    "106": "Conveyor Belt Mk.5",
    "107": "Conveyor Lift Mk.5",
    "108": "Nuclear Power Plant",
    "109": "Miner Mk.3",
    "110": "Particle Accelerator",
    "111": "Power Switch",
    "112": "Power Pole Mk.3",
    "113": "Programmable Splitter",
    "114": "Geothermal Generator",
    "115": "Radar Tower",
    "116": "Candy Cane",
    "117": "Snowman",
    "118": "FICSMAS Gift Tree",
    "119": "FICSMAS Snow Dispenser",
    "120": "FICSMAS Wreath",
    "121": "Quarter Pipe",
    "122": "Inverted Quarter Pipe",
    "123": "Inner Corner Quarter Pipe",
    "124": "Inverted Inner Corner Quarter Pipe",
    "125": "Outer Corner Quarter Pipe",
    "127": "Up Corner Ramp 8m x 1m",
    "128": "Up Corner Ramp 8m x 2m",
    "129": "Up Corner Ramp 8m x 4m",
    "130": "Down Corner Ramp 8m x 1m",
    "131": "Down Corner Ramp 8m x 2m",
    "132": "Down Corner Ramp 8m x 4m",
    "133": "Center Door Wall",
    "134": "Left Door Wall",
    "135": "Right Door Wall",
    "136": "Center Door Wall",
    "137": "Left Door Wall",
    "138": "Right Door Wall",
    "139": "Gate Wall",
    "140": "Pillar Top",
    "141": "Pillar Middle",
    "142": "Pillar Base",
    "143": "Double Ramp 8m x 2m",
    "144": "Double Ramp 8m x 4m",
    "145": "Double Ramp 8m x 8m",
    "146": "Frame Foundation 8m x 4m",
    "147": "Glass Foundation 8m x 1m",
    "148": "Hypertube Wall Support",
    "149": "Hypertube Wall Hole",
    "150": "Up Corner 8m x 1m Inverted",
    "151": "Up Corner 8m x 2m Inverted",
    "152": "Up Corner 8m x 4m Inverted",
    "153": "Down Corner 8m x 1m Inverted",
    "154": "Down Corner 8m x 2m Inverted",
    "155": "Down Corner 8m x 4m Inverted",
    "156": "Inverted Ramp 8m x 1m",
    "157": "Inverted Ramp 8m x 2m",
    "158": "Inverted Ramp 8m x 4m",
    "159": "Pipeline Wall Support",
    "160": "Pipeline Wall Hole",
    "161": "Street Light",
    "162": "Wall Outlet Mk.1",
    "163": "Double Wall Outlet Mk.1",
    "164": "Wall Outlet Mk.3",
    "165": "Double Wall Outlet Mk.3",
    "166": "Single Window",
    "167": "Frame Window",
    "168": "Reinforced Window",
    "169": "Xeno-Zapper",
    "170": "Portable Miner",
    "171": "Beacon",
    "172": "Blade Runners",
    "173": "Object Scanner",
    "174": "Nobelisk Detonator",
    "175": "Chainsaw",
    "176": "Xeno-Basher",
    "177": "Jetpack",
    "178": "Gas Mask",
    "179": "Hazmat Suit",
    "180": "Hover Pack",
    "181": "Rebar Gun",
    "182": "Medicinal Inhaler",
    "183": "Zipline",
    "184": "Color Gun",
    "185": "Parachute",
    "186": "Bacon Agaric",
    "187": "Paleberry",
    "188": "Beryl Nut",
    "189": "Rifle",
    "190": "Candy Cane Basher",
    "191": "Snowball Pile",
    "192": "Factory Cart\u2122",
    "193": "Iron Ore",
    "194": "Iron Ingot",
    "195": "Iron Plate",
    "196": "Iron Rod",
    "197": "HUB Parts",
    "198": "Copper Ore",
    "199": "Bauxite",
    "200": "Caterium Ore",
    "201": "Uranium",
    "202": "Crude Oil",
    "203": "Sulfur",
    "204": "Limestone",
    "205": "Coal",
    "206": "Raw Quartz",
    "207": "Reinforced Iron Plate",
    "208": "Cable",
    "209": "Wire",
    "210": "Copper Ingot",
    "211": "Concrete",
    "212": "Screw",
    "213": "Wood",
    "214": "Biomass",
    "215": "Leaves",
    "216": "FICSMAS Tree Branch",
    "217": "FICSMAS Gift",
    "218": "Quartz Crystal",
    "219": "Steel Beam",
    "220": "Copper Sheet",
    "221": "Encased Industrial Beam",
    "222": "Rubber",
    "223": "Motor",
    "224": "Plastic",
    "225": "Heavy Modular Frame",
    "226": "High-Speed Connector",
    "227": "Alclad Aluminum Sheet",
    "228": "Aluminum Casing",
    "229": "Radio Control Unit",
    "230": "AI Limiter",
    "231": "Drone",
    "232": "Rotor",
    "233": "Modular Frame",
    "234": "Heavy Oil Residue",
    "235": "Empty Canister",
    "236": "Petroleum Coke",
    "237": "Steel Ingot",
    "238": "Packaged Water",
    "239": "Packaged Fuel",
    "240": "Alumina Solution",
    "241": "Aluminum Scrap",
    "242": "Water",
    "243": "Circuit Board",
    "244": "Versatile Framework",
    "245": "Caterium Ingot",
    "246": "Polymer Resin",
    "247": "Stator",
    "248": "Automated Wiring",
    "249": "Smart Plating",
    "250": "Fabric",
    "251": "Aluminum Ingot",
    "252": "Fuel",
    "253": "Compacted Coal",
    "254": "Turbofuel",
    "255": "Packaged Turbofuel",
    "256": "Steel Pipe",
    "257": "Battery",
    "258": "Heat Sink",
    "259": "Cooling System",
    "260": "Electromagnetic Control Rod",
    "261": "Uranium Waste",
    "262": "Nitric Acid",
    "263": "Sulfuric Acid",
    "264": "Non-fissile Uranium",
    "265": "Fused Modular Frame",
    "266": "Encased Plutonium Cell",
    "267": "Supercomputer",
    "268": "Pressure Conversion Cube",
    "269": "Plutonium Fuel Rod",
    "270": "Crystal Oscillator",
    "271": "Computer",
    "272": "Packaged Nitrogen Gas",
    "273": "Turbo Motor",
    "274": "Quickwire",
    "275": "Silica",
    "276": "Black Powder",
    "277": "Nobelisk",
    "278": "Encased Uranium Cell",
    "279": "Uranium Fuel Rod",
    "280": "SAM Ore",
    "281": "Power Shard",
    "282": "Solid Biofuel",
    "283": "Tractor",
    "284": "Truck",
    "285": "Modular Engine",
    "286": "Adaptive Control Unit",
    "287": "Packaged Oil",
    "288": "Packaged Heavy Oil Residue",
    "289": "Packaged Liquid Biofuel",
    "290": "Liquid Biofuel",
    "291": "Electric Locomotive",
    "292": "Freight Car",
    "293": "Gas Filter",
    "294": "Packaged Alumina Solution",
    "295": "Iodine Infused Filter",
    "296": "Packaged Sulfuric Acid",
    "297": "Assembly Director System",
    "298": "Magnetic Field Generator",
    "299": "Empty Fluid Tank",
    "300": "Thermal Propulsion Rocket",
    "301": "Packaged Nitric Acid",
    "302": "Plutonium Pellet",
    "303": "Copper Powder",
    "304": "Nuclear Pasta",
    "305": "Alien Carapace",
    "306": "Spiked Rebar",
    "307": "Alien Organs",
    "308": "Mycelia",
    "309": "Flower Petals",
    "310": "Color Cartridge",
    "311": "Blue Power Slug",
    "312": "Yellow Power Slug",
    "313": "Purple Power Slug",
    "314": "Explorer",
    "315": "Rifle Cartridge",
    "316": "Candy Cane",
    "317": "FICSMAS Bow",
    "318": "Actual Snow",
    "319": "Red FICSMAS Ornament",
    "320": "Blue FICSMAS Ornament",
    "321": "Copper FICSMAS Ornament",
    "322": "Iron FICSMAS Ornament",
    "323": "FICSMAS Ornament Bundle",
    "324": "FICSMAS Decoration",
    "325": "FICSMAS Wonder Star",
    "326": "Snowball",
    "327": "Cyber Wagon",
    "329": "Arrow Down",
    "330": "Arrow Down Left",
    "331": "Arrow Down Right",
    "332": "Arrow Left",
    "333": "Arrow Up Left",
    "334": "Arrow Up",
    "335": "Arrow Up Right",
    "336": "Arrow Right",
    "337": "Drop",
    "338": "Radiation",
    "339": "Thumb Up",
    "340": "Thumb Down",
    "341": "Stop X",
    "342": "Road Arrow Down",
    "343": "Road Arrow Turn Around",
    "344": "Road Arrow Turn Left",
    "345": "Road Arrow Turn Right",
    "346": "Road Arrow Up",
    "347": "Storage Crate",
    "348": "Exit Door",
    "349": "Factory",
    "350": "Home House",
    "351": "Player Pioneer",
    "352": "Power",
    "353": "Vehicle Tractor",
    "354": "Vehicle Explorer",
    "355": "Vehicle Truck",
    "356": "Vehicle Train",
    "357": "Vehicle Factory Cart",
    "358": "Drone",
    "359": "Conveyor Lift Floor Hole",
    "360": "Empty Platform With Catwalk",
    "361": "Block Signal",
    "362": "Warning",
    "363": "Background Blueprint Grid",
    "364": "Background Grid",
    "365": "Background Checkered",
    "366": "Background Diagonal Lines",
    "367": "Background Dots",
    "368": "Background Rectangles",
    "369": "None",
    "370": "Radial Gradient",
    "371": "Wave",
    "372": "Vertical Gradient",
    "373": "Horizontal Gradient",
    "374": "Checkmark",
    "375": "FICSIT",
    "376": "Conveyor Lift Floor Hole",
    "377": "Pipeline Floor Hole",
    "378": "Industrial Railing",
    "379": "Walkway Straight",
    "380": "Walkway Crossing",
    "381": "Walkway T-Crossing",
    "382": "Walkway Ramp",
    "383": "Tilted Wall 4m",
    "384": "Foundation 1m",
    "385": "Foundation 2m",
    "386": "Foundation 4m",
    "387": "Ramp 1m",
    "388": "Ramp 2m",
    "389": "Ramp 4m",
    "390": "Basic Wall 4m",
    "391": "Basic Wall 1m",
    "392": "Metal Beam",
    "393": "Painted Beam",
    "394": "Beam Support",
    "395": "Beam Connector",
    "396": "Beam Connector Double",
    "397": "Small Billboard",
    "398": "Large Billboard",
    "399": "Catwalk Straight",
    "400": "Catwalk Crossing",
    "401": "Catwalk T-Crossing",
    "402": "Catwalk Corner",
    "403": "Catwalk Ramp",
    "404": "Catwalk Stairs",
    "405": "Big Concrete Pillar",
    "406": "Small Concrete Pillar",
    "407": "Small Pillar Support",
    "408": "Up Corner Ramp 1m",
    "409": "Up Corner Ramp 2m",
    "410": "Up Corner Ramp 4m",
    "411": "Down Corner Ramp 1m",
    "412": "Down Corner Ramp 2m",
    "413": "Down Corner Ramp 4m",
    "414": "Inv. Ramp Wall 1m",
    "415": "Inv. Ramp Wall 2m",
    "416": "Inv. Ramp Wall 4m",
    "417": "Inv. Ramp Wall 8m",
    "418": "Ramp Wall 1m",
    "419": "Ramp Wall 2m",
    "420": "Ramp Wall 4m",
    "421": "Ramp Wall 8m",
    "422": "Display Sign",
    "423": "Portrait Sign",
    "424": "Square Sign 1m",
    "425": "Square Sign 2m",
    "426": "Center Door Wall",
    "427": "Side Door Wall",
    "428": "Center Door Wall",
    "429": "Side Door Wall",
    "430": "Road Barrier",
    "431": "Modern Railing",
    "432": "Small Metal Pillar",
    "433": "Double Ramp 2m",
    "434": "Double Ramp 4m",
    "435": "Double Ramp 8m",
    "436": "Big Frame Pillar",
    "437": "Small Frame Pillar",
    "438": "Full Frame Window",
    "439": "Hex Frame Window",
    "440": "Frame Floor",
    "441": "Frame Foundation",
    "442": "Frame Wall",
    "443": "Frame Ramp",
    "444": "Inverted Frame Ramp",
    "445": "Gate Hole Wall",
    "446": "Automated Gate",
    "447": "Hazard Storage Box",
    "448": "Inv. Up Corner 1m",
    "449": "Inv. Up Corner 2m",
    "450": "Inv. Up Corner 4m",
    "451": "Inv. Down Corner 1m",
    "452": "Inv. Down Corner 2m",
    "453": "Inv. Down Corner 4m",
    "454": "Inv. Ramp 1m",
    "455": "Inv. Ramp 2m",
    "456": "Inv. Ramp 4m",
    "457": "Label Sign 2m",
    "458": "Label Sign 3m",
    "459": "Label Sign 4m",
    "460": "Square Sign 0.5m",
    "461": "Medical Storage Box",
    "462": "FICSIT Roof Flat",
    "463": "FICSIT Roof 1m",
    "464": "FICSIT Roof 2m",
    "465": "FICSIT Roof 4m",
    "466": "Tilted Wall 4m",
    "467": "Tilted Wall 8m",
    "468": "Tilted Corner Wall 4m",
    "469": "Tilted Corner Wall 8m",
    "470": "Glass Roof Flat",
    "471": "Glass Roof 1m",
    "472": "Glass Roof 2m",
    "473": "Glass Roof 4m",
    "474": "Metal Roof Flat",
    "475": "Metal Roof 1m",
    "476": "Metal Roof 2m",
    "477": "Metal Roof 4m",
    "478": "Tar Roof Flat",
    "479": "Tar Roof 1m",
    "480": "Tar Roof 2m",
    "481": "Tar Roof 4m",
    "482": "Basic Wall 1m",
    "483": "Basic Wall 4m",
    "484": "Conveyor Wall x1",
    "485": "Conveyor Wall x2",
    "486": "Conveyor Wall x3",
    "487": "Inv. Ramp Wall 1m",
    "488": "Inv. Ramp Wall 2m",
    "489": "Inv. Ramp Wall 4m",
    "490": "Inv. Ramp Wall 8m",
    "491": "Ramp Wall 1m",
    "492": "Ramp Wall 2m",
    "493": "Ramp Wall 4m",
    "494": "Ramp Wall 8m",
    "495": "Center Door Wall",
    "496": "Side Door Wall",
    "497": "Gate Hole Wall",
    "498": "Tilted Wall 4m",
    "499": "Tilted Wall 8m",
    "500": "Tilted Corner Wall 4m",
    "501": "Tilted Corner Wall 8m",
    "502": "Single Window",
    "503": "Frame Window",
    "504": "Panel Window",
    "505": "Reinforced Window",
    "506": "Foundation 1m",
    "507": "Foundation 2m",
    "508": "Foundation 4m",
    "509": "Ramp 1m",
    "510": "Ramp 2m",
    "511": "Ramp 4m",
    "512": "Foundation 1m",
    "513": "Foundation 2m",
    "514": "Foundation 4m",
    "515": "Ramp 1m",
    "516": "Ramp 2m",
    "517": "Ramp 4m",
    "518": "Foundation 1m",
    "519": "Foundation 2m",
    "520": "Foundation 4m",
    "521": "Ramp 1m",
    "522": "Ramp 2m",
    "523": "Ramp 4m",
    "524": "Up Corner Ramp 1m",
    "525": "Up Corner Ramp 2m",
    "526": "Up Corner Ramp 4m",
    "527": "Down Corner Ramp 1m",
    "528": "Down Corner Ramp 2m",
    "529": "Down Corner Ramp 4m",
    "530": "Down Corner Ramp 1m",
    "531": "Down Corner Ramp 2m",
    "532": "Down Corner Ramp 4m",
    "533": "Up Corner Ramp 1m",
    "534": "Up Corner Ramp 2m",
    "535": "Up Corner Ramp 4m",
    "536": "Down Corner Ramp 1m",
    "537": "Down Corner Ramp 2m",
    "538": "Down Corner Ramp 4m",
    "539": "Up Corner Ramp 1m",
    "540": "Up Corner Ramp 2m",
    "541": "Up Corner Ramp 4m",
    "542": "Double Ramp 2m",
    "543": "Double Ramp 4m",
    "544": "Double Ramp 8m",
    "545": "Double Ramp 2m",
    "546": "Double Ramp 4m",
    "547": "Double Ramp 8m",
    "548": "Double Ramp 2m",
    "549": "Double Ramp 4m",
    "550": "Double Ramp 8m",
    "551": "Inv. Down Corner 1m",
    "552": "Inv. Down Corner 2m",
    "553": "Inv. Down Corner 4m",
    "554": "Inv. Up Corner 1m",
    "555": "Inv. Up Corner 2m",
    "556": "Inv. Up Corner 4m",
    "557": "Inv. Down Corner 1m",
    "558": "Inv. Down Corner 2m",
    "559": "Inv. Down Corner 4m",
    "560": "Inv. Up Corner 1m",
    "561": "Inv. Up Corner 2m",
    "562": "Inv. Up Corner 4m",
    "563": "Inv. Down Corner 1m",
    "564": "Inv. Down Corner 2m",
    "565": "Inv. Down Corner 4m",
    "566": "Inv. Up Corner 1m",
    "567": "Inv. Up Corner 2m",
    "568": "Inv. Up Corner 4m",
    "569": "Inv. Ramp 1m",
    "570": "Inv. Ramp 2m",
    "571": "Inv. Ramp 4m",
    "572": "Inv. Ramp 1m",
    "573": "Inv. Ramp 2m",
    "574": "Inv. Ramp 4m",
    "575": "Inv. Ramp 1m",
    "576": "Inv. Ramp 2m",
    "577": "Inv. Ramp 4m",
    "578": "Basic Wall 1m",
    "579": "Inv. Ramp Wall 1m",
    "580": "Inv. Ramp Wall 4m",
    "581": "Inv. Ramp Wall 8m",
    "582": "Ramp Wall 1m",
    "583": "Ramp Wall 2m",
    "584": "Ramp Wall 4m",
    "585": "Ramp Wall 8m",
    "586": "Gate Hole Wall",
    "587": "Tilted Wall 4m",
    "588": "Tilted Wall 8m",
    "589": "Tilted Corner Wall 4m",
    "590": "Tilted Corner Wall 8m",
    "591": "Single Window",
    "592": "Reinforced Window",
    "593": "Frame Window",
    "594": "Panel Window",
    "595": "Golden Factory Cart\u2122",
    "596": "Block Signal",
    "597": "Path Signal",
    "598": "FICSIT Check Mark",
    "599": "Emote Build Gun Spin",
    "600": "Emote Clap",
    "601": "Emote Face Palm",
    "602": "Emote Heart",
    "603": "Emote Paper",
    "604": "Emote Rock",
    "605": "Emote Scissors",
    "606": "Emote Point",
    "607": "Emote Wave",
    "608": "Checkit",
    "609": "Lizard Doggo",
    "610": "FICSMAS Logo",
    "611": "FICSMAS Snowflake",
    "612": "FICSIT Check Snowflakes",
    "613": "FICSMAS Wrapping Paper",
    "614": "FicsMas Berries",
    "615": "FICSMAS Check",
    "616": "FICSMAS Checkit",
    "617": "FicsMas Gift",
    "618": "FICSMAS Ugly Sweater",
    "619": "Hypertube Floor Hole",
    "620": "Foundation 1m",
    "621": "Foundation 2m",
    "622": "Foundation 4m",
    "623": "Ramp 1m",
    "624": "Ramp 2m",
    "625": "Ramp 4m",
    "626": "Down Corner Ramp 1m",
    "627": "Down Corner Ramp 2m",
    "628": "Down Corner Ramp 4m",
    "629": "Up Corner Ramp 1m",
    "630": "Up Corner Ramp 2m",
    "631": "Up Corner Ramp 4m",
    "632": "Double Ramp 2m",
    "633": "Double Ramp 4m",
    "634": "Double Ramp 8m",
    "635": "Inv. Down Corner 1m",
    "636": "Inv. Down Corner 2m",
    "637": "Inv. Down Corner 4m",
    "638": "Inv. Up Corner 1m",
    "639": "Inv. Up Corner 2m",
    "640": "Inv. Up Corner 4m",
    "641": "Inv. Ramp 1m",
    "642": "Inv. Ramp 2m",
    "643": "Inv. Ramp 4m",
    "644": "Recycle",
    "645": "Trash",
    "646": "Sweet Fireworks",
    "647": "Fancy Fireworks",
    "648": "Sparkly Fireworks",
    "656": "Question Mark",
    "650": "Biomass",
    "651": "Cave",
    "652": "Crash",
    "653": "Crate",
    "654": "Creature",
    "657": "Fluids",
    "659": "Radiation",
    "660": "Rock",
    "661": "Warning",
    "662": "Fruit",
    "663": "Slug",
    "664": "Pipeline Mk.1",
    "665": "Pipeline Mk.2",
    "666": "Tilted Concave Wall 4m",
    "667": "Tilted Concave Wall 8m",
    "668": "Tilted Concave Wall 4m",
    "669": "Tilted Concave Wall 8m",
    "670": "Tilted Concave Wall 4m",
    "671": "Tilted Concave Wall 8m",
    "672": "Alien Protein",
    "673": "Iron Rebar",
    "674": "Alien Data Capsule",
    "675": "Hatcher Remains",
    "676": "Stinger Remains",
    "677": "Stun Rebar",
    "678": "Rifle Ammo",
    "679": "Homing Rifle Ammo",
    "680": "Gas Nobelisk",
    "681": "Shatter Rebar",
    "682": "Pulse Nobelisk",
    "683": "Smokeless Powder",
    "684": "Cluster Nobelisk",
    "685": "Explosive Rebar",
    "686": "Nuke Nobelisk",
    "687": "Turbo Rifle Ammo",
    "688": "Inverted Outer Corner Quarter Pipe",
    "689": "Half 1m Foundation",
    "690": "Half 2m Foundation",
    "691": "Half 4m Foundation",
    "692": "Inner Corner Extension 1m",
    "693": "Inner Corner Extension 2m",
    "694": "Inner Corner Extension 4m",
    "695": "Outer Corner Extension 1m",
    "696": "Outer Corner Extension 2m",
    "697": "Outer Corner Extension 4m",
    "698": "Inner Corner Roof 1m",
    "699": "Inner Corner Roof 2m",
    "700": "Inner Corner Roof 4m",
    "701": "Outer Corner Roof 1m",
    "702": "Outer Corner Roof 2m",
    "703": "Outer Corner Roof 4m",
    "704": "Inner Corner Extension 1m",
    "705": "Inner Corner Extension 2m",
    "706": "Inner Corner Extension 4m",
    "707": "Outer Corner Extension 1m",
    "708": "Outer Corner Extension 2m",
    "709": "Outer Corner Extension 4m",
    "710": "Inner Corner Extension 1m",
    "711": "Inner Corner Extension 2m",
    "712": "Inner Corner Extension 4m",
    "713": "Outer Corner Extension 1m",
    "714": "Outer Corner Extension 2m",
    "715": "Outer Corner Extension 4m",
    "716": "Inner Corner Extension 1m",
    "717": "Inner Corner Extension 2m",
    "718": "Inner Corner Extension 4m",
    "719": "Outer Corner Extension 1m",
    "720": "Outer Corner Extension 2m",
    "721": "Outer Corner Extension 4m",
    "722": "Inner Corner Extension 1m",
    "723": "Inner Corner Extension 2m",
    "724": "Inner Corner Extension 4m",
    "725": "Outer Corner Extension 1m",
    "726": "Outer Corner Extension 2m",
    "727": "Outer Corner Extension 4m",
    "728": "Half 1m Foundation",
    "729": "Half 2m Foundation",
    "730": "Half 4m Foundation",
    "731": "Half 1m Foundation",
    "732": "Half 2m Foundation",
    "733": "Half 4m Foundation",
    "734": "Half 1m Foundation",
    "735": "Half 2m Foundation",
    "736": "Half 4m Foundation",
    "737": "Half 1m Foundation",
    "738": "Half 2m Foundation",
    "739": "Half 4m Foundation",
    "740": "Inverted Quarter Pipe",
    "741": "Inverted Inner Corner Quarter Pipe",
    "742": "Inverted Outer Corner Quarter Pipe",
    "743": "Quarter Pipe",
    "744": "Inner Corner Quarter Pipe",
    "745": "Outer Corner Quarter Pipe",
    "746": "Inverted Quarter Pipe",
    "747": "Inverted Inner Corner Quarter Pipe",
    "748": "Inverted Outer Corner Quarter Pipe",
    "749": "Quarter Pipe",
    "750": "Inner Corner Quarter Pipe",
    "751": "Outer Corner Quarter Pipe",
    "752": "Inverted Quarter Pipe",
    "753": "Inverted Inner Corner Quarter Pipe",
    "754": "Inverted Outer Corner Quarter Pipe",
    "755": "Quarter Pipe",
    "756": "Inner Corner Quarter Pipe",
    "757": "Outer Corner Quarter Pipe",
    "758": "Inverted Quarter Pipe",
    "759": "Inverted Inner Corner Quarter Pipe",
    "760": "Inverted Outer Corner Quarter Pipe",
    "761": "Quarter Pipe",
    "762": "Inner Corner Quarter Pipe",
    "763": "Outer Corner Quarter Pipe",
    "764": "Inner Corner Roof 1m",
    "765": "Inner Corner Roof 2m",
    "766": "Inner Corner Roof 4m",
    "767": "Outer Corner Roof 1m",
    "768": "Outer Corner Roof 2m",
    "769": "Outer Corner Roof 4m",
    "770": "Inner Corner Roof 1m",
    "771": "Inner Corner Roof 2m",
    "772": "Inner Corner Roof 4m",
    "773": "Outer Corner Roof 1m",
    "774": "Outer Corner Roof 2m",
    "775": "Outer Corner Roof 4m",
    "776": "Inner Corner Roof 1m",
    "777": "Inner Corner Roof 2m",
    "778": "Inner Corner Roof 4m",
    "779": "Outer Corner Roof 1m",
    "780": "Outer Corner Roof 2m",
    "781": "Outer Corner Roof 4m",
    "782": "Question Mark",
    "783": "Power Tower",
    "784": "Power Tower Platform",
    "785": "Priority Power Switch",
    "786": "Blueprint Designer",
    "787": "Conveyor Wall Mount",
    "788": "Conveyor Ceiling Mount",
    "789": "Inv. Ramp Wall 2m"
}
     */
    switch (id) {
        case 1:
            return "The HUB";
        case 2:
            return "Craft Bench";
        case 3:
            return "Equipment Workshop";
        case 4:
            return "Smelter";
        case 5:
            return "Power Line";
        case 6:
            return "Constructor";
        case 7:
            return "Power Pole Mk.1";
        case 8:
            return "Conveyor Pole";
        case 9:
            return "Conveyor Belt Mk.1";
        case 10:
            return "Miner Mk.1";
        case 11:
            return "Storage Container";
        case 12:
            return "Space Elevator";
        case 13:
            return "Biomass Burner";
        case 14:
            return "Giant FICSMAS Tree";
        case 15:
            return "Green Screen Wall 8m x 4m";
        case 16:
            return "Foundation 4x16";
        case 17:
            return "Green Screen Foundation 8m x 4m";
        case 18:
            return "Ceiling Light";
        case 19:
            return "Wall Mounted Flood Light";
        case 20:
            return "Flood Light Tower";
        case 21:
            return "Lights Control Panel";
        case 22:
            return "Resource Well Pressurizer";
        case 23:
            return "Resource Well Extractor";
        case 24:
            return "WalkwayStairs_01";
        case 25:
            return "Ladder";
        case 26:
            return "Drone Port";
        case 27:
            return "Fence";
        case 28:
            return "Stairs";
        case 29:
            return "Panel Window";
        case 31:
            return "Old Jump Pad";
        case 32:
            return "Power Pole Mk.2";
        case 33:
            return "Wall Outlet Mk.2";
        case 34:
            return "Double Wall Outlet Mk.2";
        case 35:
            return "Smart Splitter";
        case 36:
            return "Converter";
        case 37:
            return "Remote Storage";
        case 38:
            return "Lookout Tower";
        case 39:
            return "Foundation 8m x 1m";
        case 40:
            return "Foundation 8m x 2m";
        case 41:
            return "Ramp 8m x 1m";
        case 42:
            return "Ramp 8m x 2m";
        case 43:
            return "Ramp 8m x 4m";
        case 44:
            return "Wall 8m x 4m";
        case 45:
            return "Conveyor Splitter";
        case 46:
            return "Conveyor Merger";
        case 47:
            return "Conveyor Lift Mk.1";
        case 48:
            return "MAM";
        case 49:
            return "Personal Storage Box";
        case 51:
            return "Wall Conveyor x3";
        case 52:
            return "Wall Conveyor x2";
        case 53:
            return "Wall Conveyor x1";
        case 54:
            return "Wall Conveyor x3";
        case 55:
            return "Wall Conveyor x2";
        case 56:
            return "Wall Conveyor x1";
        case 57:
            return "Stairs Left";
        case 58:
            return "Stairs Right";
        case 59:
            return "Assembler";
        case 60:
            return "U-Jelly Landing Pad";
        case 61:
            return "Walkway Straight";
        case 62:
            return "Walkway Crossing";
        case 63:
            return "Walkway T-Crossing";
        case 64:
            return "Walkway Turn";
        case 65:
            return "AWESOME Sink";
        case 66:
            return "AWESOME Shop";
        case 67:
            return "Coal Generator";
        case 68:
            return "Water Extractor";
        case 69:
            return "Pipeline Mk.1";
        case 70:
            return "Pipeline Support";
        case 71:
            return "Pipeline Junction Cross";
        case 72:
            return "Pipeline Pump Mk.1";
        case 73:
            return "Fluid Buffer";
        case 74:
            return "Conveyor Belt Mk.2";
        case 75:
            return "Stackable Conveyor Pole";
        case 76:
            return "Conveyor Lift Mk.2";
        case 77:
            return "Truck Station";
        case 78:
            return "Foundry";
        case 79:
            return "Miner Mk.2";
        case 80:
            return "Hypertube Entrance";
        case 81:
            return "Hypertube";
        case 82:
            return "Hypertube Support";
        case 83:
            return "Stackable Hypertube Support";
        case 84:
            return "Oil Extractor";
        case 85:
            return "Refinery";
        case 86:
            return "Valve";
        case 87:
            return "Manufacturer";
        case 88:
            return "Power Storage";
        case 89:
            return "Industrial Storage Container";
        case 90:
            return "Conveyor Belt Mk.3";
        case 91:
            return "Conveyor Lift Mk.3";
        case 92:
            return "Stackable Pipeline Support";
        case 93:
            return "Packager";
        case 94:
            return "Industrial Fluid Buffer";
        case 95:
            return "Fuel Generator";
        case 96:
            return "Conveyor Belt Mk.4";
        case 97:
            return "Conveyor Lift Mk.4";
        case 98:
            return "Railway";
        case 99:
            return "Train Station";
        case 100:
            return "Freight Platform";
        case 101:
            return "Fluid Freight Platform";
        case 102:
            return "Empty Platform";
        case 103:
            return "Pipeline Mk.2";
        case 104:
            return "Pipeline Pump Mk.2";
        case 105:
            return "Blender";
        case 106:
            return "Conveyor Belt Mk.5";
        case 107:
            return "Conveyor Lift Mk.5";
        case 108:
            return "Nuclear Power Plant";
        case 109:
            return "Miner Mk.3";
        case 110:
            return "Particle Accelerator";
        case 111:
            return "Power Switch";
        case 112:
            return "Power Pole Mk.3";
        case 113:
            return "Programmable Splitter";
        case 114:
            return "Geothermal Generator";
        case 115:
            return "Radar Tower";
        case 116:
            return "Candy Cane";
        case 117:
            return "Snowman";
        case 118:
            return "FICSMAS Gift Tree";
        case 119:
            return "FICSMAS Snow Dispenser";
        case 120:
            return "FICSMAS Wreath";
        case 121:
            return "Quarter Pipe";
        case 122:
            return "Inverted Quarter Pipe";
        case 123:
            return "Inner Corner Quarter Pipe";
        case 124:
            return "Inverted Inner Corner Quarter Pipe";
        case 125:
            return "Outer Corner Quarter Pipe";
        case 127:
            return "Up Corner Ramp 8m x 1m";
        case 128:
            return "Up Corner Ramp 8m x 2m";
        case 129:
            return "Up Corner Ramp 8m x 4m";
        case 130:
            return "Down Corner Ramp 8m x 1m";
        case 131:
            return "Down Corner Ramp 8m x 2m";
        case 132:
            return "Down Corner Ramp 8m x 4m";
        case 133:
            return "Center Door Wall";
        case 134:
            return "Left Door Wall";
        case 135:
            return "Right Door Wall";
        case 136:
            return "Center Door Wall";
        case 137:
            return "Left Door Wall";
        case 138:
            return "Right Door Wall";
        case 139:
            return "Gate Wall";
        case 140:
            return "Pillar Top";
        case 141:
            return "Pillar Middle";
        case 142:
            return "Pillar Base";
        case 143:
            return "Double Ramp 8m x 2m";
        case 144:
            return "Double Ramp 8m x 4m";
        case 145:
            return "Double Ramp 8m x 8m";
        case 146:
            return "Frame Foundation 8m x 4m";
        case 147:
            return "Glass Foundation 8m x 1m";
        case 148:
            return "Hypertube Wall Support";
        case 149:
            return "Hypertube Wall Hole";
        case 150:
            return "Up Corner 8m x 1m Inverted";
        case 151:
            return "Up Corner 8m x 2m Inverted";
        case 152:
            return "Up Corner 8m x 4m Inverted";
        case 153:
            return "Down Corner 8m x 1m Inverted";
        case 154:
            return "Down Corner 8m x 2m Inverted";
        case 155:
            return "Down Corner 8m x 4m Inverted";
        case 156:
            return "Inverted Ramp 8m x 1m";
        case 157:
            return "Inverted Ramp 8m x 2m";
        case 158:
            return "Inverted Ramp 8m x 4m";
        case 159:
            return "Pipeline Wall Support";
        case 160:
            return "Pipeline Wall Hole";
        case 161:
            return "Street Light";
        case 162:
            return "Wall Outlet Mk.1";
        case 163:
            return "Double Wall Outlet Mk.1";
        case 164:
            return "Wall Outlet Mk.3";
        case 165:
            return "Double Wall Outlet Mk.3";
        case 166:
            return "Single Window";
        case 167:
            return "Frame Window";
        case 168:
            return "Reinforced Window";
        case 169:
            return "Xeno-Zapper";
        case 170:
            return "Portable Miner";
        case 171:
            return "Beacon";
        case 172:
            return "Blade Runners";
        case 173:
            return "Object Scanner";
        case 174:
            return "Nobelisk Detonator";
        case 175:
            return "Chainsaw";
        case 176:
            return "Xeno-Basher";
        case 177:
            return "Jetpack";
        case 178:
            return "Gas Mask";
        case 179:
            return "Hazmat Suit";
        case 180:
            return "Hover Pack";
        case 181:
            return "Rebar Gun";
        case 182:
            return "Medicinal Inhaler";
        case 183:
            return "Zipline";
        case 184:
            return "Color Gun";
        case 185:
            return "Parachute";
        case 186:
            return "Bacon Agaric";
        case 187:
            return "Paleberry";
        case 188:
            return "Beryl Nut";
        case 189:
            return "Rifle";
        case 190:
            return "Candy Cane Basher";
        case 191:
            return "Snowball Pile";
        case 192:
            return "Factory Cart\u2122";
        case 193:
            return "Iron Ore";
        case 194:
            return "Iron Ingot";
        case 195:
            return "Iron Plate";
        case 196:
            return "Iron Rod";
        case 197:
            return "HUB Parts";
        case 198:
            return "Copper Ore";
        case 199:
            return "Bauxite";
        case 200:
            return "Caterium Ore";
        case 201:
            return "Uranium";
        case 202:
            return "Crude Oil";
        case 203:
            return "Sulfur";
        case 204:
            return "Limestone";
        case 205:
            return "Coal";
        case 206:
            return "Raw Quartz";
        case 207:
            return "Reinforced Iron Plate";
        case 208:
            return "Cable";
        case 209:
            return "Wire";
        case 210:
            return "Copper Ingot";
        case 211:
            return "Concrete";
        case 212:
            return "Screw";
        case 213:
            return "Wood";
        case 214:
            return "Biomass";
        case 215:
            return "Leaves";
        case 216:
            return "FICSMAS Tree Branch";
        case 217:
            return "FICSMAS Gift";
        case 218:
            return "Quartz Crystal";
        case 219:
            return "Steel Beam";
        case 220:
            return "Copper Sheet";
        case 221:
            return "Encased Industrial Beam";
        case 222:
            return "Rubber";
        case 223:
            return "Motor";
        case 224:
            return "Plastic";
        case 225:
            return "Heavy Modular Frame";
        case 226:
            return "High-Speed Connector";
        case 227:
            return "Alclad Aluminum Sheet";
        case 228:
            return "Aluminum Casing";
        case 229:
            return "Radio Control Unit";
        case 230:
            return "AI Limiter";
        case 231:
            return "Drone";
        case 232:
            return "Rotor";
        case 233:
            return "Modular Frame";
        case 234:
            return "Heavy Oil Residue";
        case 235:
            return "Empty Canister";
        case 236:
            return "Petroleum Coke";
        case 237:
            return "Steel Ingot";
        case 238:
            return "Packaged Water";
        case 239:
            return "Packaged Fuel";
        case 240:
            return "Alumina Solution";
        case 241:
            return "Aluminum Scrap";
        case 242:
            return "Water";
        case 243:
            return "Circuit Board";
        case 244:
            return "Versatile Framework";
        case 245:
            return "Caterium Ingot";
        case 246:
            return "Polymer Resin";
        case 247:
            return "Stator";
        case 248:
            return "Automated Wiring";
        case 249:
            return "Smart Plating";
        case 250:
            return "Fabric";
        case 251:
            return "Aluminum Ingot";
        case 252:
            return "Fuel";
        case 253:
            return "Compacted Coal";
        case 254:
            return "Turbofuel";
        case 255:
            return "Packaged Turbofuel";
        case 256:
            return "Steel Pipe";
        case 257:
            return "Battery";
        case 258:
            return "Heat Sink";
        case 259:
            return "Cooling System";
        case 260:
            return "Electromagnetic Control Rod";
        case 261:
            return "Uranium Waste";
        case 262:
            return "Nitric Acid";
        case 263:
            return "Sulfuric Acid";
        case 264:
            return "Non-fissile Uranium";
        case 265:
            return "Fused Modular Frame";
        case 266:
            return "Encased Plutonium Cell";
        case 267:
            return "Supercomputer";
        case 268:
            return "Pressure Conversion Cube";
        case 269:
            return "Plutonium Fuel Rod";
        case 270:
            return "Crystal Oscillator";
        case 271:
            return "Computer";
        case 272:
            return "Packaged Nitrogen Gas";
        case 273:
            return "Turbo Motor";
        case 274:
            return "Quickwire";
        case 275:
            return "Silica";
        case 276:
            return "Black Powder";
        case 277:
            return "Nobelisk";
        case 278:
            return "Encased Uranium Cell";
        case 279:
            return "Uranium Fuel Rod";
        case 280:
            return "SAM Ore";
        case 281:
            return "Power Shard";
        case 282:
            return "Solid Biofuel";
        case 283:
            return "Tractor";
        case 284:
            return "Truck";
        case 285:
            return "Modular Engine";
        case 286:
            return "Adaptive Control Unit";
        case 287:
            return "Packaged Oil";
        case 288:
            return "Packaged Heavy Oil Residue";
        case 289:
            return "Packaged Liquid Biofuel";
        case 290:
            return "Liquid Biofuel";
        case 291:
            return "Electric Locomotive";
        case 292:
            return "Freight Car";
        case 293:
            return "Gas Filter";
        case 294:
            return "Packaged Alumina Solution";
        case 295:
            return "Iodine Infused Filter";
        case 296:
            return "Packaged Sulfuric Acid";
        case 297:
            return "Assembly Director System";
        case 298:
            return "Magnetic Field Generator";
        case 299:
            return "Empty Fluid Tank";
        case 300:
            return "Thermal Propulsion Rocket";
        case 301:
            return "Packaged Nitric Acid";
        case 302:
            return "Plutonium Pellet";
        case 303:
            return "Copper Powder";
        case 304:
            return "Nuclear Pasta";
        case 305:
            return "Alien Carapace";
        case 306:
            return "Spiked Rebar";
        case 307:
            return "Alien Organs";
        case 308:
            return "Mycelia";
        case 309:
            return "Flower Petals";
        case 310:
            return "Color Cartridge";
        case 311:
            return "Blue Power Slug";
        case 312:
            return "Yellow Power Slug";
        case 313:
            return "Purple Power Slug";
        case 314:
            return "Explorer";
        case 315:
            return "Rifle Cartridge";
        case 316:
            return "Candy Cane";
        case 317:
            return "FICSMAS Bow";
        case 318:
            return "Actual Snow";
        case 319:
            return "Red FICSMAS Ornament";
        case 320:
            return "Blue FICSMAS Ornament";
        case 321:
            return "Copper FICSMAS Ornament";
        case 322:
            return "Iron FICSMAS Ornament";
        case 323:
            return "FICSMAS Ornament Bundle";
        case 324:
            return "FICSMAS Decoration";
        case 325:
            return "FICSMAS Wonder Star";
        case 326:
            return "Snowball";
        case 327:
            return "Cyber Wagon";
        case 329:
            return "Arrow Down";
        case 330:
            return "Arrow Down Left";
        case 331:
            return "Arrow Down Right";
        case 332:
            return "Arrow Left";
        case 333:
            return "Arrow Up Left";
        case 334:
            return "Arrow Up";
        case 335:
            return "Arrow Up Right";
        case 336:
            return "Arrow Right";
        case 337:
            return "Drop";
        case 338:
            return "Radiation";
        case 339:
            return "Thumb Up";
        case 340:
            return "Thumb Down";
        case 341:
            return "Stop X";
        case 342:
            return "Road Arrow Down";
        case 343:
            return "Road Arrow Turn Around";
        case 344:
            return "Road Arrow Turn Left";
        case 345:
            return "Road Arrow Turn Right";
        case 346:
            return "Road Arrow Up";
        case 347:
            return "Storage Crate";
        case 348:
            return "Exit Door";
        case 349:
            return "Factory";
        case 350:
            return "Home House";
        case 351:
            return "Player Pioneer";
        case 352:
            return "Power";
        case 353:
            return "Vehicle Tractor";
        case 354:
            return "Vehicle Explorer";
        case 355:
            return "Vehicle Truck";
        case 356:
            return "Vehicle Train";
        case 357:
            return "Vehicle Factory Cart";
        case 358:
            return "Drone";
        case 359:
            return "Conveyor Lift Floor Hole";
        case 360:
            return "Empty Platform With Catwalk";
        case 361:
            return "Block Signal";
        case 362:
            return "Warning";
        case 363:
            return "Background Blueprint Grid";
        case 364:
            return "Background Grid";
        case 365:
            return "Background Checkered";
        case 366:
            return "Background Diagonal Lines";
        case 367:
            return "Background Dots";
        case 368:
            return "Background Rectangles";
        case 369:
            return "None";
        case 370:
            return "Radial Gradient";
        case 371:
            return "Wave";
        case 372:
            return "Vertical Gradient";
        case 373:
            return "Horizontal Gradient";
        case 374:
            return "Checkmark";
        case 375:
            return "FICSIT";
        case 376:
            return "Conveyor Lift Floor Hole";
        case 377:
            return "Pipeline Floor Hole";
        case 378:
            return "Industrial Railing";
        case 379:
            return "Walkway Straight";
        case 380:
            return "Walkway Crossing";
        case 381:
            return "Walkway T-Crossing";
        case 382:
            return "Walkway Ramp";
        case 383:
            return "Tilted Wall 4m";
        case 384:
            return "Foundation 1m";
        case 385:
            return "Foundation 2m";
        case 386:
            return "Foundation 4m";
        case 387:
            return "Ramp 1m";
        case 388:
            return "Ramp 2m";
        case 389:
            return "Ramp 4m";
        case 390:
            return "Basic Wall 4m";
        case 391:
            return "Basic Wall 1m";
        case 392:
            return "Metal Beam";
        case 393:
            return "Painted Beam";
        case 394:
            return "Beam Support";
        case 395:
            return "Beam Connector";
        case 396:
            return "Beam Connector Double";
        case 397:
            return "Small Billboard";
        case 398:
            return "Large Billboard";
        case 399:
            return "Catwalk Straight";
        case 400:
            return "Catwalk Crossing";
        case 401:
            return "Catwalk T-Crossing";
        case 402:
            return "Catwalk Corner";
        case 403:
            return "Catwalk Ramp";
        case 404:
            return "Catwalk Stairs";
        case 405:
            return "Big Concrete Pillar";
        case 406:
            return "Small Concrete Pillar";
        case 407:
            return "Small Pillar Support";
        case 408:
            return "Up Corner Ramp 1m";
        case 409:
            return "Up Corner Ramp 2m";
        case 410:
            return "Up Corner Ramp 4m";
        case 411:
            return "Down Corner Ramp 1m";
        case 412:
            return "Down Corner Ramp 2m";
        case 413:
            return "Down Corner Ramp 4m";
        case 414:
            return "Inv. Ramp Wall 1m";
        case 415:
            return "Inv. Ramp Wall 2m";
        case 416:
            return "Inv. Ramp Wall 4m";
        case 417:
            return "Inv. Ramp Wall 8m";
        case 418:
            return "Ramp Wall 1m";
        case 419:
            return "Ramp Wall 2m";
        case 420:
            return "Ramp Wall 4m";
        case 421:
            return "Ramp Wall 8m";
        case 422:
            return "Display Sign";
        case 423:
            return "Portrait Sign";
        case 424:
            return "Square Sign 1m";
        case 425:
            return "Square Sign 2m";
        case 426:
            return "Center Door Wall";
        case 427:
            return "Side Door Wall";
        case 428:
            return "Center Door Wall";
        case 429:
            return "Side Door Wall";
        case 430:
            return "Road Barrier";
        case 431:
            return "Modern Railing";
        case 432:
            return "Small Metal Pillar";
        case 433:
            return "Double Ramp 2m";
        case 434:
            return "Double Ramp 4m";
        case 435:
            return "Double Ramp 8m";
        case 436:
            return "Big Frame Pillar";
        case 437:
            return "Small Frame Pillar";
        case 438:
            return "Full Frame Window";
        case 439:
            return "Hex Frame Window";
        case 440:
            return "Frame Floor";
        case 441:
            return "Frame Foundation";
        case 442:
            return "Frame Wall";
        case 443:
            return "Frame Ramp";
        case 444:
            return "Inverted Frame Ramp";
        case 445:
            return "Gate Hole Wall";
        case 446:
            return "Automated Gate";
        case 447:
            return "Hazard Storage Box";
        case 448:
            return "Inv. Up Corner 1m";
        case 449:
            return "Inv. Up Corner 2m";
        case 450:
            return "Inv. Up Corner 4m";
        case 451:
            return "Inv. Down Corner 1m";
        case 452:
            return "Inv. Down Corner 2m";
        case 453:
            return "Inv. Down Corner 4m";
        case 454:
            return "Inv. Ramp 1m";
        case 455:
            return "Inv. Ramp 2m";
        case 456:
            return "Inv. Ramp 4m";
        case 457:
            return "Label Sign 2m";
        case 458:
            return "Label Sign 3m";
        case 459:
            return "Label Sign 4m";
        case 460:
            return "Square Sign 0.5m";
        case 461:
            return "Medical Storage Box";
        case 462:
            return "FICSIT Roof Flat";
        case 463:
            return "FICSIT Roof 1m";
        case 464:
            return "FICSIT Roof 2m";
        case 465:
            return "FICSIT Roof 4m";
        case 466:
            return "Tilted Wall 4m";
        case 467:
            return "Tilted Wall 8m";
        case 468:
            return "Tilted Corner Wall 4m";
        case 469:
            return "Tilted Corner Wall 8m";
        case 470:
            return "Glass Roof Flat";
        case 471:
            return "Glass Roof 1m";
        case 472:
            return "Glass Roof 2m";
        case 473:
            return "Glass Roof 4m";
        case 474:
            return "Metal Roof Flat";
        case 475:
            return "Metal Roof 1m";
        case 476:
            return "Metal Roof 2m";
        case 477:
            return "Metal Roof 4m";
        case 478:
            return "Tar Roof Flat";
        case 479:
            return "Tar Roof 1m";
        case 480:
            return "Tar Roof 2m";
        case 481:
            return "Tar Roof 4m";
        case 482:
            return "Basic Wall 1m";
        case 483:
            return "Basic Wall 4m";
        case 484:
            return "Conveyor Wall x1";
        case 485:
            return "Conveyor Wall x2";
        case 486:
            return "Conveyor Wall x3";
        case 487:
            return "Inv. Ramp Wall 1m";
        case 488:
            return "Inv. Ramp Wall 2m";
        case 489:
            return "Inv. Ramp Wall 4m";
        case 490:
            return "Inv. Ramp Wall 8m";
        case 491:
            return "Ramp Wall 1m";
        case 492:
            return "Ramp Wall 2m";
        case 493:
            return "Ramp Wall 4m";
        case 494:
            return "Ramp Wall 8m";
        case 495:
            return "Center Door Wall";
        case 496:
            return "Side Door Wall";
        case 497:
            return "Gate Hole Wall";
        case 498:
            return "Tilted Wall 4m";
        case 499:
            return "Tilted Wall 8m";
        case 500:
            return "Tilted Corner Wall 4m";
        case 501:
            return "Tilted Corner Wall 8m";
        case 502:
            return "Single Window";
        case 503:
            return "Frame Window";
        case 504:
            return "Panel Window";
        case 505:
            return "Reinforced Window";
        case 506:
            return "Foundation 1m";
        case 507:
            return "Foundation 2m";
        case 508:
            return "Foundation 4m";
        case 509:
            return "Ramp 1m";
        case 510:
            return "Ramp 2m";
        case 511:
            return "Ramp 4m";
        case 512:
            return "Foundation 1m";
        case 513:
            return "Foundation 2m";
        case 514:
            return "Foundation 4m";
        case 515:
            return "Ramp 1m";
        case 516:
            return "Ramp 2m";
        case 517:
            return "Ramp 4m";
        case 518:
            return "Foundation 1m";
        case 519:
            return "Foundation 2m";
        case 520:
            return "Foundation 4m";
        case 521:
            return "Ramp 1m";
        case 522:
            return "Ramp 2m";
        case 523:
            return "Ramp 4m";
        case 524:
            return "Up Corner Ramp 1m";
        case 525:
            return "Up Corner Ramp 2m";
        case 526:
            return "Up Corner Ramp 4m";
        case 527:
            return "Down Corner Ramp 1m";
        case 528:
            return "Down Corner Ramp 2m";
        case 529:
            return "Down Corner Ramp 4m";
        case 530:
            return "Down Corner Ramp 1m";
        case 531:
            return "Down Corner Ramp 2m";
        case 532:
            return "Down Corner Ramp 4m";
        case 533:
            return "Up Corner Ramp 1m";
        case 534:
            return "Up Corner Ramp 2m";
        case 535:
            return "Up Corner Ramp 4m";
        case 536:
            return "Down Corner Ramp 1m";
        case 537:
            return "Down Corner Ramp 2m";
        case 538:
            return "Down Corner Ramp 4m";
        case 539:
            return "Up Corner Ramp 1m";
        case 540:
            return "Up Corner Ramp 2m";
        case 541:
            return "Up Corner Ramp 4m";
        case 542:
            return "Double Ramp 2m";
        case 543:
            return "Double Ramp 4m";
        case 544:
            return "Double Ramp 8m";
        case 545:
            return "Double Ramp 2m";
        case 546:
            return "Double Ramp 4m";
        case 547:
            return "Double Ramp 8m";
        case 548:
            return "Double Ramp 2m";
        case 549:
            return "Double Ramp 4m";
        case 550:
            return "Double Ramp 8m";
        case 551:
            return "Inv. Down Corner 1m";
        case 552:
            return "Inv. Down Corner 2m";
        case 553:
            return "Inv. Down Corner 4m";
        case 554:
            return "Inv. Up Corner 1m";
        case 555:
            return "Inv. Up Corner 2m";
        case 556:
            return "Inv. Up Corner 4m";
        case 557:
            return "Inv. Down Corner 1m";
        case 558:
            return "Inv. Down Corner 2m";
        case 559:
            return "Inv. Down Corner 4m";
        case 560:
            return "Inv. Up Corner 1m";
        case 561:
            return "Inv. Up Corner 2m";
        case 562:
            return "Inv. Up Corner 4m";
        case 563:
            return "Inv. Down Corner 1m";
        case 564:
            return "Inv. Down Corner 2m";
        case 565:
            return "Inv. Down Corner 4m";
        case 566:
            return "Inv. Up Corner 1m";
        case 567:
            return "Inv. Up Corner 2m";
        case 568:
            return "Inv. Up Corner 4m";
        case 569:
            return "Inv. Ramp 1m";
        case 570:
            return "Inv. Ramp 2m";
        case 571:
            return "Inv. Ramp 4m";
        case 572:
            return "Inv. Ramp 1m";
        case 573:
            return "Inv. Ramp 2m";
        case 574:
            return "Inv. Ramp 4m";
        case 575:
            return "Inv. Ramp 1m";
        case 576:
            return "Inv. Ramp 2m";
        case 577:
            return "Inv. Ramp 4m";
        case 578:
            return "Basic Wall 1m";
        case 579:
            return "Inv. Ramp Wall 1m";
        case 580:
            return "Inv. Ramp Wall 4m";
        case 581:
            return "Inv. Ramp Wall 8m";
        case 582:
            return "Ramp Wall 1m";
        case 583:
            return "Ramp Wall 2m";
        case 584:
            return "Ramp Wall 4m";
        case 585:
            return "Ramp Wall 8m";
        case 586:
            return "Gate Hole Wall";
        case 587:
            return "Tilted Wall 4m";
        case 588:
            return "Tilted Wall 8m";
        case 589:
            return "Tilted Corner Wall 4m";
        case 590:
            return "Tilted Corner Wall 8m";
        case 591:
            return "Single Window";
        case 592:
            return "Reinforced Window";
        case 593:
            return "Frame Window";
        case 594:
            return "Panel Window";
        case 595:
            return "Golden Factory Cart\u2122";
        case 596:
            return "Block Signal";
        case 597:
            return "Path Signal";
        case 598:
            return "FICSIT Check Mark";
        case 599:
            return "Emote Build Gun Spin";
        case 600:
            return "Emote Clap";
        case 601:
            return "Emote Face Palm";
        case 602:
            return "Emote Heart";
        case 603:
            return "Emote Paper";
        case 604:
            return "Emote Rock";
        case 605:
            return "Emote Scissors";
        case 606:
            return "Emote Point";
        case 607:
            return "Emote Wave";
        case 608:
            return "Checkit";
        case 609:
            return "Lizard Doggo";
        case 610:
            return "FICSMAS Logo";
        case 611:
            return "FICSMAS Snowflake";
        case 612:
            return "FICSIT Check Snowflakes";
        case 613:
            return "FICSMAS Wrapping Paper";
        case 614:
            return "FicsMas Berries";
        case 615:
            return "FICSMAS Check";
        case 616:
            return "FICSMAS Checkit";
        case 617:
            return "FicsMas Gift";
        case 618:
            return "FICSMAS Ugly Sweater";
        case 619:
            return "Hypertube Floor Hole";
        case 620:
            return "Foundation 1m";
        case 621:
            return "Foundation 2m";
        case 622:
            return "Foundation 4m";
        case 623:
            return "Ramp 1m";
        case 624:
            return "Ramp 2m";
        case 625:
            return "Ramp 4m";
        case 626:
            return "Down Corner Ramp 1m";
        case 627:
            return "Down Corner Ramp 2m";
        case 628:
            return "Down Corner Ramp 4m";
        case 629:
            return "Up Corner Ramp 1m";
        case 630:
            return "Up Corner Ramp 2m";
        case 631:
            return "Up Corner Ramp 4m";
        case 632:
            return "Double Ramp 2m";
        case 633:
            return "Double Ramp 4m";
        case 634:
            return "Double Ramp 8m";
        case 635:
            return "Inv. Down Corner 1m";
        case 636:
            return "Inv. Down Corner 2m";
        case 637:
            return "Inv. Down Corner 4m";
        case 638:
            return "Inv. Up Corner 1m";
        case 639:
            return "Inv. Up Corner 2m";
        case 640:
            return "Inv. Up Corner 4m";
        case 641:
            return "Inv. Ramp 1m";
        case 642:
            return "Inv. Ramp 2m";
        case 643:
            return "Inv. Ramp 4m";
        case 644:
            return "Recycle";
        case 645:
            return "Trash";
        case 646:
            return "Sweet Fireworks";
        case 647:
            return "Fancy Fireworks";
        case 648:
            return "Sparkly Fireworks";
        case 656:
            return "Question Mark";
        case 650:
            return "Biomass";
        case 651:
            return "Cave";
        case 652:
            return "Crash";
        case 653:
            return "Crate";
        case 654:
            return "Creature";
        case 657:
            return "Fluids";
        case 659:
            return "Radiation";
        case 660:
            return "Rock";
        case 661:
            return "Warning";
        case 662:
            return "Fruit";
        case 663:
            return "Slug";
        case 664:
            return "Pipeline Mk.1";
        case 665:
            return "Pipeline Mk.2";
        case 666:
            return "Tilted Concave Wall 4m";
        case 667:
            return "Tilted Concave Wall 8m";
        case 668:
            return "Tilted Concave Wall 4m";
        case 669:
            return "Tilted Concave Wall 8m";
        case 670:
            return "Tilted Concave Wall 4m";
        case 671:
            return "Tilted Concave Wall 8m";
        case 672:
            return "Alien Protein";
        case 673:
            return "Iron Rebar";
        case 674:
            return "Alien Data Capsule";
        case 675:
            return "Hatcher Remains";
        case 676:
            return "Stinger Remains";
        case 677:
            return "Stun Rebar";
        case 678:
            return "Rifle Ammo";
        case 679:
            return "Homing Rifle Ammo";
        case 680:
            return "Gas Nobelisk";
        case 681:
            return "Shatter Rebar";
        case 682:
            return "Pulse Nobelisk";
        case 683:
            return "Smokeless Powder";
        case 684:
            return "Cluster Nobelisk";
        case 685:
            return "Explosive Rebar";
        case 686:
            return "Nuke Nobelisk";
        case 687:
            return "Turbo Rifle Ammo";
        case 688:
            return "Inverted Outer Corner Quarter Pipe";
        case 689:
            return "Half 1m Foundation";
        case 690:
            return "Half 2m Foundation";
        case 691:
            return "Half 4m Foundation";
        case 692:
            return "Inner Corner Extension 1m";
        case 693:
            return "Inner Corner Extension 2m";
        case 694:
            return "Inner Corner Extension 4m";
        case 695:
            return "Outer Corner Extension 1m";
        case 696:
            return "Outer Corner Extension 2m";
        case 697:
            return "Outer Corner Extension 4m";
        case 698:
            return "Inner Corner Roof 1m";
        case 699:
            return "Inner Corner Roof 2m";
        case 700:
            return "Inner Corner Roof 4m";
        case 701:
            return "Outer Corner Roof 1m";
        case 702:
            return "Outer Corner Roof 2m";
        case 703:
            return "Outer Corner Roof 4m";
        case 704:
            return "Inner Corner Extension 1m";
        case 705:
            return "Inner Corner Extension 2m";
        case 706:
            return "Inner Corner Extension 4m";
        case 707:
            return "Outer Corner Extension 1m";
        case 708:
            return "Outer Corner Extension 2m";
        case 709:
            return "Outer Corner Extension 4m";
        case 710:
            return "Inner Corner Extension 1m";
        case 711:
            return "Inner Corner Extension 2m";
        case 712:
            return "Inner Corner Extension 4m";
        case 713:
            return "Outer Corner Extension 1m";
        case 714:
            return "Outer Corner Extension 2m";
        case 715:
            return "Outer Corner Extension 4m";
        case 716:
            return "Inner Corner Extension 1m";
        case 717:
            return "Inner Corner Extension 2m";
        case 718:
            return "Inner Corner Extension 4m";
        case 719:
            return "Outer Corner Extension 1m";
        case 720:
            return "Outer Corner Extension 2m";
        case 721:
            return "Outer Corner Extension 4m";
        case 722:
            return "Inner Corner Extension 1m";
        case 723:
            return "Inner Corner Extension 2m";
        case 724:
            return "Inner Corner Extension 4m";
        case 725:
            return "Outer Corner Extension 1m";
        case 726:
            return "Outer Corner Extension 2m";
        case 727:
            return "Outer Corner Extension 4m";
        case 728:
            return "Half 1m Foundation";
        case 729:
            return "Half 2m Foundation";
        case 730:
            return "Half 4m Foundation";
        case 731:
            return "Half 1m Foundation";
        case 732:
            return "Half 2m Foundation";
        case 733:
            return "Half 4m Foundation";
        case 734:
            return "Half 1m Foundation";
        case 735:
            return "Half 2m Foundation";
        case 736:
            return "Half 4m Foundation";
        case 737:
            return "Half 1m Foundation";
        case 738:
            return "Half 2m Foundation";
        case 739:
            return "Half 4m Foundation";
        case 740:
            return "Inverted Quarter Pipe";
        case 741:
            return "Inverted Inner Corner Quarter Pipe";
        case 742:
            return "Inverted Outer Corner Quarter Pipe";
        case 743:
            return "Quarter Pipe";
        case 744:
            return "Inner Corner Quarter Pipe";
        case 745:
            return "Outer Corner Quarter Pipe";
        case 746:
            return "Inverted Quarter Pipe";
        case 747:
            return "Inverted Inner Corner Quarter Pipe";
        case 748:
            return "Inverted Outer Corner Quarter Pipe";
        case 749:
            return "Quarter Pipe";
        case 750:
            return "Inner Corner Quarter Pipe";
        case 751:
            return "Outer Corner Quarter Pipe";
        case 752:
            return "Inverted Quarter Pipe";
        case 753:
            return "Inverted Inner Corner Quarter Pipe";
        case 754:
            return "Inverted Outer Corner Quarter Pipe";
        case 755:
            return "Quarter Pipe";
        case 756:
            return "Inner Corner Quarter Pipe";
        case 757:
            return "Outer Corner Quarter Pipe";
        case 758:
            return "Inverted Quarter Pipe";
        case 759:
            return "Inverted Inner Corner Quarter Pipe";
        case 760:
            return "Inverted Outer Corner Quarter Pipe";
        case 761:
            return "Quarter Pipe";
        case 762:
            return "Inner Corner Quarter Pipe";
        case 763:
            return "Outer Corner Quarter Pipe";
        case 764:
            return "Inner Corner Roof 1m";
        case 765:
            return "Inner Corner Roof 2m";
        case 766:
            return "Inner Corner Roof 4m";
        case 767:
            return "Outer Corner Roof 1m";
        case 768:
            return "Outer Corner Roof 2m";
        case 769:
            return "Outer Corner Roof 4m";
        case 770:
            return "Inner Corner Roof 1m";
        case 771:
            return "Inner Corner Roof 2m";
        case 772:
            return "Inner Corner Roof 4m";
        case 773:
            return "Outer Corner Roof 1m";
        case 774:
            return "Outer Corner Roof 2m";
        case 775:
            return "Outer Corner Roof 4m";
        case 776:
            return "Inner Corner Roof 1m";
        case 777:
            return "Inner Corner Roof 2m";
        case 778:
            return "Inner Corner Roof 4m";
        case 779:
            return "Outer Corner Roof 1m";
        case 780:
            return "Outer Corner Roof 2m";
        case 781:
            return "Outer Corner Roof 4m";
        case 782:
            return "Question Mark";
        case 783:
            return "Power Tower";
        case 784:
            return "Power Tower Platform";
        case 785:
            return "Priority Power Switch";
        case 786:
            return "Blueprint Designer";
        case 787:
            return "Conveyor Wall Mount";
        case 788:
            return "Conveyor Ceiling Mount";
        case 789:
            return "Inv. Ramp Wall 2m";
        default:
            return "";
    }
}