from enum import Enum


class APIVersionPrefix(str, Enum):
    V1: str = "/v1"


class EndpointPrefix(str, Enum):
    LIVEZ: str = "/livez"
    READYZ: str = "/readyz"
