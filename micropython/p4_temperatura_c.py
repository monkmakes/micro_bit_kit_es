# P4 Temperatura C

from microbit import *

while True:
    lectura = pin1.read_analog()
    temperatura_c = round(lectura * 0.157 - 54)
    display.scroll(str(temperatura_c))