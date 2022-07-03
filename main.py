from button import Button
from led import LED
from quizzer import Quizzer

STATE_TEST = "test"
STATE_RESET = "reset"
STATE_LIVE = "live"

current_state = STATE_RESET

# TODO: Make sure pin numbers are correct
reset = Button(0)
qm_led = LED(25)

quizzers = [
    Quizzer("Team 1 Seat 1", 0, 0),
    Quizzer("Team 1 Seat 2", 0, 0),
    Quizzer("Team 1 Seat 3", 0, 0),
    Quizzer("Team 1 Seat 4", 0, 0),
    Quizzer("Team 2 Seat 1", 0, 0),
    Quizzer("Team 2 Seat 2", 0, 0),
    Quizzer("Team 2 Seat 3", 0, 0),
    Quizzer("Team 2 Seat 4", 0, 0),
    Quizzer("Team 3 Seat 1", 0, 0),
    Quizzer("Team 3 Seat 2", 0, 0),
    Quizzer("Team 3 Seat 3", 0, 0),
    Quizzer("Team 3 Seat 4", 0, 0)
]


while True:
    if current_state == STATE_RESET:
        for quizzer in quizzers:
            if quizzer.buzzer():
                quizzer.light(True)
                qm_led.on()
                current_state = STATE_LIVE
                break
        if reset.is_toggled():
            current_state = STATE_TEST
            qm_led.on()
    elif current_state == STATE_TEST:
        for quizzer in quizzers:
            quizzer.light(quizzer.pressed())
        if reset.is_toggled():
            for quizzer in quizzers:
                quizzer.light(False)
            qm_led.off()
            current_state = STATE_RESET
    elif current_state == STATE_LIVE:
        if reset.is_toggled():
            qm_led.off()
            current_state = STATE_RESET