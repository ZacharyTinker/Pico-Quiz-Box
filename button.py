from machine import Pin
from time import time

class Button:
    def __init__(self, pin_number):
        self.pin_number = pin_number
        self.pin = Pin(self.pin_number, Pin.IN, Pin.PULL_DOWN)
        self.was_pressed = False 

    def is_pressed(self):
        if bool(self.pin.value()):
            self.was_pressed = True
        else:
            self.was_pressed = False
        return self.was_pressed

    def is_toggled(self):
        was_pressed = self.was_pressed
        return not self.is_pressed() and was_pressed
