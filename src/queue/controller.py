from queue.sqs import SimpleQS


class QueueController:
    def __init__(self):
        self.sqs = SimpleQS()

    def post(self, message: str, message_id: str):
        return self.sqs.enqueue(message, message_id)
