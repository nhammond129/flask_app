import random
import time
import json
from threading import Thread
from typing import Callable
from datetime import datetime

class DataGenerator:
    class Subscriber:
        def __init__(self, parent):
            self.queue = []
            self.parent = parent
            self.parent.subscribers.add(self)
        def write(self, val):
            self.queue.append(val)
        def read(self):
            while True:
                if len(self.queue):
                    yield self.queue.pop(0)
        def __del__(self):
            self.parent.remove(self)

    def __init__(self):
        self.subscribers = set()
        self.thread = Thread(target=self.runner)
        self.thread.start()
    
    def runner(self):
        value = random.uniform(0, 100)
        while True:
            value += random.uniform(-1,1)
            if value > 100: value = 100
            if value < 0: value = 0

            json_data = json.dumps({
                'time': datetime.now().strftime('%H:%M:%S'),
                'value': value
                })
            for sub in self.subscribers:
                sub.write(f"data:{json_data}\n\n")

            time.sleep(0.1)

    def subscribe(self):
        return self.Subscriber(self)

generator = DataGenerator()