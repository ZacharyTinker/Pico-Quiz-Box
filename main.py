from button import Button
from led import LED
from quizzer import Quizzer

STATE_TEST = "test"
STATE_RESET = "reset"
STATE_LIVE = "live"

current_state = STATE_RESET

# TODO: Make sure pin numbers are correct
reset = Button(0)
qm_led = LED(28)

quizzers = [
    Quizzer("Team 1 Seat 1", 1, 13),
    Quizzer("Team 1 Seat 2", 2, 14),
    Quizzer("Team 1 Seat 3", 3, 15),
    Quizzer("Team 1 Seat 4", 4, 16),
    Quizzer("Team 2 Seat 1", 5, 17),
    Quizzer("Team 2 Seat 2", 6, 18),
    Quizzer("Team 2 Seat 3", 7, 19),
    Quizzer("Team 2 Seat 4", 8, 20),
    Quizzer("Team 3 Seat 1", 9, 21),
    Quizzer("Team 3 Seat 2", 10, 22),
    Quizzer("Team 3 Seat 3", 11, 26),
    Quizzer("Team 3 Seat 4", 12, 27)
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