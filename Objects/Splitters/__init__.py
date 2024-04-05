"""Splitter base class & Rule class"""
from typing import Literal
from Items import BaseItem
from Objects import BaseFactoryObject, RawFactoryObject


class BaseSplitter(BaseFactoryObject, raw={}):
    """The base splitter/merger class"""
    def __init_subclass__(cls, raw: RawFactoryObject) -> None:
        super().__init_subclass__(raw)


SpecialSplitterRule = Literal[
    "Any",
    "Any Undefined",
    "Overflow",
    "None"
]


class SplitterRule:
    """Any rule you can put inside a splitter or smart splitter"""
    def __init__(self, rule: BaseItem | SpecialSplitterRule = "Any") -> None:
        assert (
            isinstance(rule, BaseItem)
            ) or (
            rule in ["Any","Any Undefined","Overflow","None"]
        ), "Invalid Splitter Rule!"
        self.rule = rule
