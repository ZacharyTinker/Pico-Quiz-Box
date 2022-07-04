from machine import Pin
from time import time

class Button:
    def __init__(self, pin_number):
        self.pin_number = pin_number
        self.pin = Pin(self.pin_number, Pin.IN, Pin.PULL_DOWN)
        self.last_pressed = 0 

    def is_pressed(self):
        if bool(self.pin.value()):
            self.last_pressed = round(time() * 1000)
            return True
        else:
            return False

    def is_toggled(self):
        last_pressed = self.last_pressed
        pressed = self.is_pressed()
        return not pressed and (self.last_pressed - last_pressed < 50)
