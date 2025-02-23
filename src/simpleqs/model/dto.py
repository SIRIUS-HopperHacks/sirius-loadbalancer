from typing import ClassVar, List, Type
from marshmallow import Schema as MSchema
from marshmallow_dataclass import dataclass

@dataclass
class ConnectionDTO:
    connectionId: str
    deviceId: str
    detectedLocation: str
    alertType: str
    alertedTime: str
    detectedTime: str
    Schema: ClassVar[Type[MSchema]] = MSchema

@dataclass
class ConnectionListDTO:
    alerts: List[ConnectionDTO]
    Schema: ClassVar[Type[MSchema]] = MSchema

@dataclass
class AlertDTO:
    deviceId: str
    alertType: str
    alertTime: str
    Schema: ClassVar[Type[MSchema]] = MSchema
