import datetime
from typing import ClassVar, List, Type
from marshmallow import Schema as MSchema
from marshmallow_dataclass import dataclass


@dataclass
class ConnectionDTO:
    connection_id: str
    device_id: str
    detected_location: str
    alert_type: str
    alerted_time: datetime.datetime
    detected_time: datetime.datetime
    Schema: ClassVar[Type[MSchema]] = MSchema


@dataclass
class ConnectionListDTO:
    connections: List[ConnectionDTO]
    Schema: ClassVar[Type[MSchema]] = MSchema


@dataclass
class AlertDTO:
    device_id: str
    alert_type: str
    alert_time: datetime.datetime
    Schema: ClassVar[Type[MSchema]] = MSchema
