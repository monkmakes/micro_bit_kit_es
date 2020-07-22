# P3 Gritometro
from microbit import *

def graficobarras(a):
    display.clear()
    for y in range(0, 5):
        if a > y:
            for x in range(0, 5):
                display.set_pixel(x, 4-y, 9)

while True:
    nivel_sonido = (pin0.read_analog() - 511) / 100
    graficobarras(nivel_sonido)
