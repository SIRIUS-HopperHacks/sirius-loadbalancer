import queue
import threading

from src.simpleqs.model.item import Item


class SimpleQS:
    def __init__(self):
        self.q = queue.Queue()
        self.identifiers = set()
        self.lock = threading.Lock()
        
    def enqueue(self, item: Item) -> bool:
        with self.lock:
            # if item.value in self.identifiers:
            #     return False
            # self.identifiers.add(item.value)
            self.q.put(item)
        return True

    def dequeue(self) -> Item:
        try:
            return self.q.get(timeout=1)
        except queue.Empty:
            return None
