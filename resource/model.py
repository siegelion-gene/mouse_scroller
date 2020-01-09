import time
from pynput.mouse import Button, Controller


class Model:
    def __init__(self):
        self.tick = 0.2
        step = 10
        direction = [-1, -1, -1, -1, -1, 1]
        self.actions = [x * step if x < 0 else x * step * (len(direction)-1) for x in direction]
        self.c = Controller()

    def scroll(self):
        for action in self.actions:
            time.sleep(self.tick)
            self.c.scroll(0, action)


