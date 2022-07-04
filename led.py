from machine import Pin

class LED:
    def __init__(self, pin_number, on=False):
        self.pin_number = pin_number
        self.pin = Pin(self.pin_number, Pin.OUT)
        self.light_on = on

    def toggle(self):
        if self.light_on:
            self.off()
        else:
            self.on()

    def on(self):
        self.light_on = True
        self.pin.on()

    def off(self):
        self.light_on = False
        self.pin.off()