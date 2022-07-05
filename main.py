from time import sleep, time
from button import Button
from led import LED
from quizzer import Quizzer

STATE_TEST = "test"
STATE_RESET = "reset"
STATE_JUMP = "jump"
STATE_STATS = "stats"

LED_OFF = True
LED_ON = False

current_state = STATE_RESET
current_time = time()
state_switch_time = time()
current_quizzer = None
last_light_toggle_time = time()

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

def log(message):
    # TODO: Show time along with message
    # print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
    print(message)

def switch_state(next_state):
    global current_state, state_switch_time
    for quizzer in quizzers:
        quizzer.light(LED_OFF)
    qm_led.off()
    current_state = next_state
    state_switch_time = time()
    log(f"Current state: {current_state}")

switch_state(STATE_RESET)

while True:
    # Update all button states
    current_time = time()
    reset.update_state()
    for quizzer in quizzers:
        quizzer.button.update_state()

    # Reset state
    if current_state == STATE_RESET:
        for quizzer in quizzers:
            # If quizzer hit their button, turn on their light and switch to stats state 
            if quizzer.buzzer():
                log(f"{quizzer.name} pressed button")
                current_quizzer = quizzer
                switch_state(STATE_STATS)
                quizzer.light(LED_ON)
                qm_led.on()
                break
        # If the reset button is toggled, switch to testing state
        if reset.is_toggled():
            sleep(.1)
            switch_state(STATE_TEST)
            qm_led.on()

    # Test state
    elif current_state == STATE_TEST:
        # Blink QM light on and off
        if current_time - last_light_toggle_time > .5:
            qm_led.toggle()
            last_light_toggle_time = current_time
        # Turn lights on or off depending on if the quizzer presses their button
        for quizzer in quizzers:
            if quizzer.buzzer():
                log(f"{quizzer.name} pressed button")
                quizzer.light(LED_ON)
            else:
                quizzer.light(LED_OFF)
        # If the reset button is toggles, switch to the reset state
        if reset.is_toggled():
            sleep(.1)
            switch_state(STATE_RESET)
            qm_led.on()
 
    # Stats state
    elif current_state == STATE_STATS:
        # If we're two or more seconds since the first quizzer rang in, show some stats!
        if current_time - state_switch_time >= 2:
            # TODO: Show stats for all the quizzers who jumped for this question
            switch_state(STATE_JUMP)
            current_quizzer.light(LED_ON)

    # Jump state
    elif current_state == STATE_JUMP:
        if reset.is_toggled():
            sleep(.1)
            switch_state(STATE_RESET)
