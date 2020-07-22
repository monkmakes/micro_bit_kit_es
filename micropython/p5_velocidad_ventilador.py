from microbit import *

potencia_minima = 600
potencia_maxima = 1023
potencia_paso = (potencia_maxima - potencia_minima) / 9
velocidad = 0

def establecer_potencia(velocidad):
    display.show(str(velocidad))
    if velocidad == 0:
        pin0.write_analog(0)
    else:
        pin0.write_analog(velocidad * potencia_paso + potencia_minima)

establecer_potencia(velocidad)

while True:
    if button_a.was_pressed():
        velocidad -= 1
        if velocidad < 0:
            velocidad = 0
        establecer_potencia(velocidad)
    elif button_b.was_pressed():
        velocidad += 1
        if velocidad > 9:
            velocidad = 9
        establecer_potencia(velocidad)
    sleep(100)
