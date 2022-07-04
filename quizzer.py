from button import Button
from led import LED

class Quizzer:
    def __init__(self, name, button_pin, led_pin):
        self.name = name
        self.button = Button(button_pin)
        self.led = LED(led_pin)

    def buzzer(self):
        return self.button.is_pressed()
    
    def light(self, on):
        if on:
            self.led.on()
        else:
            self.led.off()   