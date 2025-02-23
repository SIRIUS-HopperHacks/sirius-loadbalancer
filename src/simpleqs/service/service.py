from src.lib.api import API
from src.simpleqs.model.dto import ConnectionListDTO, AlertDTO
from src.simpleqs.model.item import Item
from src.lib.sqs import SimpleQS


class QueueService:
    def __init__(self):
        self.sqs = SimpleQS()
        self.api = API()

    def enqueue(self, input_data: ConnectionListDTO):
        for connection in input_data.connections:
            alert = AlertDTO(
                device_id=connection.device_id,
                alert_type=connection.alert_type,
                alert_time=connection.alerted_time
            )
            self.sqs.enqueue(Item(alert.Schema().dump(alert)))

    def dispatch(self):
        item = self.sqs.dequeue()
        if item:
            self.api.send_request(item.value)
        return None
