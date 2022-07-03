from machine import Pin

class LED:
    def __init__(self, pin_number, on=False):
        self.pin_number = pin_number
        self.pin = Pin(self.pin_number, Pin.OUT)
        self.on = on
        if self.on:
            self.pin.on()

    def toggle(self):
        if self.on:
            self.off()
        else:
            self.on()

    def on(self):
        self.on = True
        self.pin.on()

    def off(self):
        self.on = False
        self.pin.off()
