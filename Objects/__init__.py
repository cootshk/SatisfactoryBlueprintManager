"""The base of all Satisfactory Objects"""
from dataclasses import dataclass
from .. import BaseClassException

RawFactoryObject = dict[str, dict[str, str|list[float|int]|dict[str,list[float|int]]]]
@dataclass
class BaseFactoryObject:
    """BaseFactoryObject:
    Any object that can appear in game.

    Properties:
        - raw (dict): the raw JSON of the object (before compression)
    """
    def __init_subclass__(cls, raw: dict) -> None:
        if not isinstance(raw, dict):
            raise TypeError("raw must be a RawFactoryObject!")
#        if raw == {}: raise ValueError("raw does not contain a factory object!")
        cls.raw = raw # type: ignore

    def __repr__(self) -> str:
        return str(self.raw)
    def __eq__(self, value: object) -> bool:
        if isinstance(value, BaseFactoryObject):
            return self.raw == value.raw
        else:
            return False
    def __hash__(self) -> int:
        return hash(self.raw)


