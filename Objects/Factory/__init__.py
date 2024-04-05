from Objects import BaseFactoryObject


class BaseProducer(BaseFactoryObject, raw = {}):
    """Any object that produces material"""
    def __init_subclass__(cls, raw: dict) -> None:
        return super().__init_subclass__(raw)
