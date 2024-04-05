"""Smart Splitter Class"""
from Objects import RawFactoryObject
from Objects.Splitters import BaseSplitter


class SmartSplitter(BaseSplitter, raw={}):
    """The Smart Splitter

    Args:
        raw (rawFactoryObject): The raw JSON data.
    """
    def __init__(self, raw: RawFactoryObject):
        super().__init__()
        super().__init_subclass__(raw)
