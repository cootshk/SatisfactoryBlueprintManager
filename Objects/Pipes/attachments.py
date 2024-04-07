from Objects import BaseConnector


class BasePipelineSupport(BaseConnector, raw={}):
    pass
class PipelineSupport(BasePipelineSupport, raw={}):
    pass
class WallPipelineSupport(BasePipelineSupport, raw={}):
    pass
class CeilingPipelineSupport(BasePipelineSupport, raw={}):
    pass