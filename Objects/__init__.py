from dataclasses import dataclass


@dataclass
class BaseFactoryObject:
    def __init_subclass__(cls, raw: dict) -> None:
        assert isinstance(raw, dict)
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


rawFactoryObject = dict[str, dict[str, str|list[float|int]|dict[str,list[float|int]]]]