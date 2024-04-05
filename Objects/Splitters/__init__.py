from typing import Any, Literal
from Items import BaseItem
from Objects import BaseFactoryObject


class BaseSplitter(BaseFactoryObject, raw={}):
    def __init_subclass__(cls, raw: dict) -> None:
        return super().__init_subclass__(raw)


class SpecialRule:
    class Any:
        pass
    class Overflow:
        pass
    class Undefined:
        pass

class SplitterRule:
    def __init__(self, item: BaseItem | SpecialRule | None = None) -> None:
        self.item = item