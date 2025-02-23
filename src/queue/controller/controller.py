from queue.model.dto import ConnectionListDTO
from queue.service.service import QueueService
from flask.views import MethodView
from flask import request


class QueueController(MethodView):
    def __init__(self):
        self.service = QueueService()

    def post(self):
        input_data = ConnectionListDTO.Schema().load(
            request.get_json(force=True, silent=True))
        self.service.enqueue(input_data)
        self.service.dispatch()
