from Objects import rawFactoryObject
from ..Splitters import BaseSplitter


class Splitter(BaseSplitter, raw={}):
    def __init__(self, raw: rawFactoryObject) -> None:
        self.raw = raw
        self.front = None
        self.left = None
        self.right = None