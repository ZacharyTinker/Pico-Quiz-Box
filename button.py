from machine import Pin
from time import time

class Button:
    def __init__(self, pin_number):
        self.pin_number = pin_number
        self.pin = Pin(self.pin_number, Pin.IN, Pin.PULL_DOWN)
        self.last_state = 0
        self.last_time = 0
        self.current_state = bool(self.pin.value())
        self.current_time = time()

    def update_state(self):
        current_state = bool(self.pin.value())
        if current_state != self.current_state:
            self.last_state = self.current_state
            self.last_time = self.current_time
            self.current_state = current_state
            self.current_time = time()

    def is_pressed(self):
        return self.current_state

    def is_toggled(self):
        return (not self.current_state) and (not self.current_state) == self.last_state
