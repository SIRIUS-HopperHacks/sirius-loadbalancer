from flask import Blueprint
from flask_restful import Api
from queue.controller.controller import QueueController


queue_blueprint = Blueprint('queue', __name__, url_prefix='/sqs')
queue_api = Api(queue_blueprint)

queue_api.add_resource(QueueController, '/enqueue')
