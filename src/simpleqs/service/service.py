from src.lib.api import API
from src.simpleqs.model.dto import ConnectionListDTO, AlertDTO
from src.simpleqs.model.item import Item
from src.lib.sqs import SimpleQS

class QueueService:
    def __init__(self):
        self.sqs = SimpleQS()
        self.api = API()

    def enqueue(self, input_data: ConnectionListDTO):
        for connection in input_data.alerts:
            alert = AlertDTO(
                deviceId=connection.deviceId,
                alertType=connection.alertType,
                alertTime=connection.alertedTime
            )
            self.sqs.enqueue(Item(alert.Schema().dump(alert)))

    def dispatch(self):
        item = self.sqs.dequeue()
        if item:
            self.api.send_request(item.value)
        return None
