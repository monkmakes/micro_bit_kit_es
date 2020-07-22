# P7 Musica Magica

from microbit import *
import music

multiplicador = 20

base_iluminacion = pin2.read_analog()

while True:
    iluminacion = pin2.read_analog()
    tono = base_iluminacion - iluminacion
    if tono > 0:
        music.pitch(tono * multiplicador)
    sleep(100)