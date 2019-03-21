from pythx.models.exceptions import RequestValidationError
from pythx.models.request.base import BaseRequest


class OASRequest(BaseRequest):
    def __init__(self, mode="yaml"):
        if not mode in ("yaml", "html"):
            raise RequestValidationError("'mode' must be one of {html,yaml}")
        self.mode = mode

    @property
    def endpoint(self):
        return "v1/openapi" + (".yaml" if self.mode == "yaml" else "")

    @property
    def method(self):
        return "GET"

    @property
    def payload(self):
        return {}

    @property
    def parameters(self):
        return {}

    @property
    def headers(self):
        return {}

    @classmethod
    def from_dict(cls, d):
        return cls()

    def to_dict(self):
        return {}
