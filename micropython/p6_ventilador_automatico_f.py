from microbit import *

def lee_temp_c():
    lectura = pin1.read_analog()
    temp_c = round( lectura * 0.135 + 1)
    return temp_c

temp_umbral = lee_temp_c() + 2
   
while True:
    if button_a.was_pressed():
        temp_umbral -= 1
        display.scroll('Umbral' + str(temp_umbral))
    elif button_b.was_pressed():
        temp_umbral += 1
        display.scroll('Umbral' + str(temp_umbral))
    display.scroll(str(read_temp_c()))
    if lee_temp_c() > temp_umbral:
        pin0.write_digital(1)
    else:
        pin0.write_digital(0)
