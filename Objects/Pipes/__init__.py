from Objects import BaseConnector, BaseFactoryObject


class BasePipe(BaseFactoryObject, raw={}):
    pass
class BasePump(BaseConnector, raw={}):
    pass

class Valve(BasePump, raw={}):
    pass