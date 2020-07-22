# P4 Temperatura F 

from microbit import *

while True:
    lectura = pin1.read_analog()
    temperatura_f = round(lectura * 0.135 +1)
    display.scroll(str(temperatura_f))
