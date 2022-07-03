from machine import Pin

class Button:
    def __init__(self, pin_number):
        self.pin_number = pin_number
        self.pin = Pin(self.pin_number, Pin.IN, Pin.PULL_DOWN)

    def is_pressed(self):
        return bool(self.pin.value())

    def is_toggled(self):
        # TODO: Return true if the button was recently pressed and released
        return False