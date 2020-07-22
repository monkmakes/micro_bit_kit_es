# P4 Calibracion Temperatura
from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll(pin1.read_analog())
