"""The normal splitter"""
from dataclasses import dataclass
from Objects import RawFactoryObject
from ..Splitters import BaseSplitter, SplitterRule

@dataclass
class Splitter(BaseSplitter, raw={}):
    """A normal splitter, as seen in game"""
    def __init__(self, raw: RawFactoryObject) -> None:
        self.raw = raw
        self.front = SplitterRule("Any")
        self.left = SplitterRule("Any")
        self.right = SplitterRule("Any")

        super().__init_subclass__(raw)
