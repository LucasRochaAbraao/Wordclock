#!/usr/bin/env python3
#coding=utf-8

#################################
#           WORDCLOCK           #
#      Lucas Rocha Abraao       #
#     lucasrabraao@gmail.com    #
#           20/08/2021          #
#################################

import random
from datetime import datetime, timedelta

# TODO:
# - (OK) print to terminal time in words
# - (OK) print letter coords (to simulate leds)
# - função para ligar todas as leds
# - (OK) E pode ser qualquer um (choice entre opções)
# - da /horas/manhã/noite 10% de chance por hora (hora inteira)
# - se menos que 4 palavras, coloca o da noite/manhã/tarde (exceto meio dia/noite)
# - Draw stuff randomly for 5 minutes, or until button pressed. If
#   button pressed first, draw for 30 minutes or until button pressed again.
# - new years countdown

# Colors
RED     = (255, 0,   0  )
LIME    = (0,   255, 0  )
BLUE    = (0,   0,   255)
YELLOW  = (255, 255, 0  )
FUCHSIA = (255, 0,   255)
AQUA    = (0,   255, 255)
WHITE   = (255, 255, 255)

# Birthday
BIRTH_MONTH = 8
BIRTH_DAY = 24


special_words = {
    "": [],
    "": [],
    "": [],
    "o": []
}

"""
0  sao é
1  tres cinco
2  uma quatro vinte
3  duas oito
4  onze seis dez
5  nove quinze u
6  doze sete e
7  pras meio dia da e
8  vinte meia quinze
9  noite trinta e
10 nove duas uma sete
11 dez seis oito
12 quatro tres cinco
13 horas dia e meia da
14 manhã tarde noite
"""

def get_coord_hour(hour, pos=0):
    # hour = 3 or 15
    # pos = posição primária(0) ou secundária(1). Por exemplo, são vinte pras dez
    # dez fica na posição de hora secundária.

    time_words = {
        #     primária  secundária
        #   [ [(), ()], [(), ()] ]
        0:  [ [(8, 5), (8, 6), (8, 7), (8, 8), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14)], [] ], # meia noite
        1:  [ [(2, 0), (2, 1), (2, 2)], [(10, 8), (10, 9), (10, 10)] ], # uma
        2:  [ [(3, 3), (3, 4), (3, 5), (3, 6)], [(10, 4), (10, 5), (10, 6), (10, 7)] ], # duas
        3:  [ [(1, 1), (1, 2), (1, 3), (1, 4)], [(12, 6), (12, 7), (12, 8), (12, 9)] ], # tres
        4:  [ [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5)] ], # quatro
        5:  [ [(1, 5), (1, 6), (1, 7), (1, 8), (1, 9)], [(12, 10), (12, 11), (12, 12), (12, 13), (12, 14)] ], # cinco
        6:  [ [(4, 5), (4, 6), (4, 7), (4, 8)], [(11, 6), (11, 7), (11, 8), (11, 9)] ], # seis
        7:  [ [(6, 7), (6, 8), (6, 9), (6, 10)], [(10, 11), (10, 12), (10, 13), (10, 14)] ], # sete
        8:  [ [(3, 8), (3, 9), (3, 10), (3, 11)], [(11, 11), (11, 12), (11, 13), (11, 14)] ], # oito
        9:  [ [(5, 2), (5, 3), (5, 4), (5, 5)], [(10, 0), (10, 1), (10, 2), (10, 3)] ], # nove
        10: [ [(4, 10), (4, 11), (4, 12)], [(11, 3), (11, 4), (11, 5)] ], # dez
        11: [ [(4, 0), (4, 1), (4, 2), (4, 3)], [] ], # onze
        12: [ [(7, 4), (7, 5), (7, 6), (7, 7), (7, 9), (7, 10), (7, 11)], [] ], # meio dia
        13: [ [(2, 0), (2, 1), (2, 2)], [(10, 8), (10, 9), (10, 10)] ], # uma
        14: [ [(3, 3), (3, 4), (3, 5), (3, 6)], [(10, 4), (10, 5), (10, 6), (10, 7)] ], # duas
        15: [ [(1, 1), (1, 2), (1, 3), (1, 4)], [(12, 6), (12, 7), (12, 8), (12, 9)] ], # tres
        16: [ [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5)] ], # quatro
        17: [ [(1, 5), (1, 6), (1, 7), (1, 8), (1, 9)], [(12, 10), (12, 11), (12, 12), (12, 13), (12, 14)] ], # cinco
        18: [ [(4, 5), (4, 6), (4, 7), (4, 8)], [(11, 6), (11, 7), (11, 8), (11, 9)] ], # seis
        19: [ [(6, 7), (6, 8), (6, 9), (6, 10)], [(10, 11), (10, 12), (10, 13), (10, 14)] ], # sete
        20: [ [(3, 8), (3, 9), (3, 10), (3, 11)], [(11, 11), (11, 12), (11, 13), (11, 14)] ], # oito
        21: [ [(5, 2), (5, 3), (5, 4), (5, 5)], [(10, 0), (10, 1), (10, 2), (10, 3)] ], # nove
        22: [ [(4, 10), (4, 11), (4, 12)], [(11, 3), (11, 4), (11, 5)] ], # dez
        23: [ [(4, 0), (4, 1), (4, 2), (4, 3)], [] ], # onze
    }
    
    return time_words[hour][pos]

def get_coord_minute(minute, pos=0):
    # minute = 30 or 15
    # pos = posição primária(0) ou secundária(1). Por exemplo, são vinte pras dez
    # vinte fica na posição de hora primária.

    time_words = {
        #     primária  secundária
        #   [ [(), ()], [(), ()] ]
        5:  [ [(1, 5), (1, 6), (1, 7), (1, 8), (1, 9)], [(12, 10), (12, 11), (12, 12), (12, 13), (12, 14)] ], # cinco
        10: [ [(4, 10), (4, 11), (4, 12)], [(11, 3), (11, 4), (11, 5)] ], # dez
        15: [ [(5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12)], [(8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14)] ], # quinze
        20: [ [(2, 10), (2, 11), (2, 12), (2, 13), (2, 14)], [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)] ], # vinte
        30: [ [(8, 5), (8, 6), (8, 7), (8, 8)], [(13, 9), (13, 10), (13, 11), (13, 12)] ] # meia
    }
    
    return time_words[minute][pos]

def get_matrix(coords):
    leds_to_activate = list()
    matrix = [
    #     0    1    2    3    4    5    6    7    8    9   10   11   12   13   14
        ['S', 'Ã', 'O', 'É', 'O', 'J', 'G', 'T', 'U', 'E', 'W', 'Z', 'N', 'X', 'A'], # 0 sao é
        ['E', 'T', 'R', 'Ê', 'S', 'C', 'I', 'N', 'C', 'O', 'R', 'R', 'I', 'K', 'A'], # 1 tres cinco
        ['U', 'M', 'A', 'Q', 'U', 'A', 'T', 'R', 'O', 'P', 'V', 'I', 'N', 'T', 'E'], # 2 uma quatro vinte
        ['D', 'H', 'W', 'D', 'U', 'A', 'S', 'Q', 'O', 'I', 'T', 'O', 'K', 'V', 'I'], # 3 duas oito
        ['O', 'N', 'Z', 'E', 'G', 'S', 'E', 'I', 'S', 'B', 'D', 'E', 'Z', 'A', 'Y'], # 4 onze seis dez
        ['K', 'J', 'N', 'O', 'V', 'E', 'B', 'Q', 'U', 'I', 'N', 'Z', 'E', 'U', 'F'], # 5 nove quinze u
        ['W', 'R', 'D', 'O', 'Z', 'E', 'F', 'S', 'E', 'T', 'E', 'B', 'E', 'H', 'T'], # 6 doze sete e
        ['P', 'R', 'A', 'S', 'M', 'E', 'I', 'O', 'V', 'D', 'I', 'A', 'D', 'A', 'E'], # 7 pras meio dia da e
        ['V', 'I', 'N', 'T', 'E', 'M', 'E', 'I', 'A', 'Q', 'U', 'I', 'N', 'Z', 'E'], # 8 vinte meia quinze
        ['N', 'O', 'I', 'T', 'E', 'T', 'R', 'I', 'N', 'T', 'A', 'E', 'F', 'Y', 'X'], # 9 noite trinta e
        ['N', 'O', 'V', 'E', 'D', 'U', 'A', 'S', 'U', 'M', 'A', 'S', 'E', 'T', 'E'], # 10 nove duas uma sete
        ['A', 'M', 'O', 'D', 'E', 'Z', 'S', 'E', 'I', 'S', 'H', 'O', 'I', 'T', 'O'], # 11 dez seis oito
        ['Q', 'U', 'A', 'T', 'R', 'O', 'T', 'R', 'E', 'S', 'C', 'I', 'N', 'C', 'O'], # 12 quatro tres cinco
        ['H', 'O', 'R', 'A', 'S', 'D', 'I', 'A', 'E', 'M', 'E', 'I', 'A', 'D', 'A'], # 13 horas dia e meia da
        ['M', 'A', 'N', 'H', 'Ã', 'T', 'A', 'R', 'D', 'E', 'N', 'O', 'I', 'T', 'E']  # 14 manhã tarde noite
    #     0    1    2    3    4    5    6    7    8    9   10   11   12   13   14
    ]

    for word_coords in coords:
        #print(f"word_coords: {word_coords}")
        leds_to_activate.append(matrix[word_coords[0]][word_coords[1]])
    return leds_to_activate

def flip_coin(weight):
    reference = random.getrandbits(3) / 7
    return True if weight >= reference else False

def get_time_phrase(hour, minute):
    #print(hour, minute)
    coords = list() # create coordenates to activate leds in a matrix
    
    if minute > 55:
        if hour!= 23: # qualquer hora menos 23
            hour += 1 # arredonda pra próxima hora de uma vez
        else:
            hour = 0 # mas se a hora era 23, a próxima precisa ser 0 e não 24.
        minute = 0 # arredonda minutos acima de 55 pra próxima hora.

    # é 1h..., é meio dia..., é meia noite...
    if (hour == 1 or hour == 12 or hour == 13 or hour == 0) and minute == 0:
        #if flip_coin(weight=0.9): # weight returns True or False
        #    phrase += ['é']
        # ainda tenho que ajustar essa probabilidade de não ter o 'é' ou 'são',
        # pq olha como pode sair: dez cinco pras da noite 21:55
        coords.append([(0, 3)]) # é
        #phrase += matrix[time_words2['é'][0]][matrix[time_words2['é'][0]]]
    else:
        #if flip_coin(weight=0.9): # weight returns True or False
        #    phrase += ['são']
        coords.append([(0, 0), (0, 1), (0, 2)]) # são

    if minute >= 40:
        hour += 1
        if hour == 24:
            hour = 0 #

    # HORA
    if hour == 0:
        coords.append([(8, 5), (8, 6), (8, 7), (8, 8)]) # meia
        coords.append([(14, 10), (14, 11), (14, 12), (14, 13), (14, 14)]) # noite
        if minute == 0:
            return coords
    elif hour == 23 and minute > 55 or hour == 0 and minute < 3: # se não for exatamente, como acima.
        coords = list()
        coords.append([(0, 3)]) # é
        coords.append([(8, 5), (8, 6), (8, 7), (8, 8)]) # meia
        coords.append([(14, 10), (14, 11), (14, 12), (14, 13), (14, 14)]) # noite
        return coords
    elif hour == 12:
        coords.append([(7, 4), (7, 5), (7, 6), (7, 7)]) # meio
        coords.append([(7, 9), (7, 10), (7, 11)]) # dia
        if minute == 0:
            return coords
    elif hour == 11 and minute > 55 or hour == 12 and minute == 0:
        coords = list()
        coords.append([(0, 3)]) # é
        coords.append([(7, 4), (7, 5), (7, 6), (7, 7)]) # meio
        coords.append([(7, 9), (7, 10), (7, 11)]) # dia
        return coords
    else:
        coords.append(get_coord_hour(hour, pos=0)) # the hours?

    # MINUTO
    if minute == 0 and (hour == 1 or hour == 13):
        coords.append([(13, 0), (13, 1), (13, 2), (13, 3)]) # hora
        return coords

    if minute == 0:
        if hour < 12:
            coords.append([(13, 0), (13, 1), (13, 2), (13, 3), (13, 4)]) # horas
            if flip_coin(weight=0.8): # weight returns True or False
                coords.append([(13, 13), (13, 14)]) # da
                coords.append([(14, 0), (14, 1), (14, 2), (14, 3), (14, 4)]) # manhã
        elif hour > 12 and hour < 18:
            coords.append([(13, 0), (13, 1), (13, 2), (13, 3), (13, 4)]) # horas
            if flip_coin(weight=0.5): # weight returns True or False
                coords.append([(13, 13), (13, 14)]) # da
                coords.append([(14, 5), (14, 6), (14, 7), (14, 8), (14, 9)]) # tarde
        else:
            coords.append([(13, 0), (13, 1), (13, 2), (13, 3), (13, 4)]) # horas
            if flip_coin(weight=0.6): # weight returns True or False
                coords.append([(13, 13), (13, 14)]) # da
                coords.append([(14, 10), (14, 11), (14, 12), (14, 13), (14, 14)]) # noite
        return coords

    elif minute == 25:
        coords.append([(6, 12)]) # e
        coords.append([(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)]) # vinte
        coords.append([(6, 12)]) # e
        coords.append([(12, 10), (12, 11), (12, 12), (12, 13), (12, 14)]) # cinco
        

    elif minute == 35:
        coords.append([(6, 12)]) # e
        coords.append([(9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10)]) # trinta
        coords.append([(6, 12)]) # e
        coords.append([(12, 10), (12, 11), (12, 12), (12, 13), (12, 14)]) # cinco
        
    elif minute == 40:
        coords.insert(1, [(2, 10), (2, 11), (2, 12), (2, 13), (2, 14)]) # vinte
        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            coords.insert(2, [(7, 0), (7, 1), (7, 2)]) # pra
        else:
            coords.insert(2, [(7, 0), (7, 1), (7, 2), (7, 3)]) # pras

    elif minute == 45:
        coords.insert(1, [(5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12)])
        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            coords.insert(2, [(7, 0), (7, 1), (7, 2)]) # pra
        else:
            coords.insert(2, [(7, 0), (7, 1), (7, 2), (7, 3)]) # pras

    elif minute == 50:
        coords.insert(1, [(4, 10), (4, 11), (4, 12)])
        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            coords.insert(2, [(7, 0), (7, 1), (7, 2)]) # pra
        else:
            coords.insert(2, [(7, 0), (7, 1), (7, 2), (7, 3)]) # pras

    elif minute == 55:
        coords.insert(1, [(1, 5), (1, 6), (1, 7), (1, 8), (1, 9)]) # cinco
        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            coords.insert(2, [(7, 0), (7, 1), (7, 2)]) # pra
        else:
            coords.insert(2, [(7, 0), (7, 1), (7, 2), (7, 3)]) # pras

    else: # cinco dez quinze vinte
        coords.append([(9, 11)]) # e
        coords.append(get_coord_minute(minute, pos=1)) # minute

    # Time of Day
    if hour > 0 and hour < 12:
        if flip_coin(weight=0.8): # weight returns True or False
            coords.append([(13, 13), (13, 14)]) # da
            coords.append([(14, 0), (14, 1), (14, 2), (14, 3), (14, 4)]) # manhã

    elif hour >= 13 and hour < 19:
        if flip_coin(weight=0.8): # weight returns True or False
            coords.append([(13, 13), (13, 14)]) # da
            coords.append([(14, 5), (14, 6), (14, 7), (14, 8), (14, 9)]) # tarde
    elif (hour >= 19 and hour < 23) or (hour == 23 and minute <= 59):
        if flip_coin(weight=0.8): # weight returns True or False
            coords.append([(13, 13), (13, 14)]) # da
            coords.append([(14, 10), (14, 11), (14, 12), (14, 13), (14, 14)]) # noite
    
    return coords

def main():
    #cinco = 0
    #for _ in range(291):
    #    #time_reference = datetime.now() - timedelta(hours=10, minutes=30)
    #    #time_reference.time()
    #    #time_reference = datetime.now().time()
    #    time_reference = datetime.now() + timedelta(minutes=cinco)
    #    current_minute = 5 * round(time_reference.minute/5)
    #    current_hour = time_reference.hour
    #    if current_minute == 60:
    #        current_minute = 0
    #        if current_hour != 23:
    #            current_hour += 1
    #        else:
    #            current_hour = 0
    #    display_phrase = get_time_phrase(current_hour, current_minute)
    #    final_phrase = [''.join(get_matrix(word_list)) for word_list in display_phrase]
    #    print(f"{current_hour}:{current_minute}", ' '.join(final_phrase))
    #    #print(time_reference)
    #    cinco += 5

    time_reference = datetime.now()
    current_minute = 5 * round(time_reference.minute/5)
    current_hour = time_reference.hour
    if current_minute == 60:
        current_minute = 0
        if current_hour!= 23:
            current_hour += 1
        else:
            current_hour = 0

    display_phrase = get_time_phrase(current_hour, current_minute)
    final_phrase = [''.join(get_matrix(word_list)) for word_list in display_phrase]
    print(' '.join(final_phrase))
    
if __name__ == '__main__':
    main()


"""
### MicroPython


### synchronize with ntp
# need to be connected to wifi
import network, utime, ntptime

def connect_wifi():
    print("Connecting to WiFi...")
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect('Ana Paula', 'naotemsenha')
    while not wifi.isconnected():
        pass
    print("Connected.")

def update_time():
    ntptime.settime()
    local_time_sec = utime.time() + -3 * 3600
    local_time = utime.localtime(local_time_sec)
    return local_time

print(update_time())
print(utime.localtime())


### NEOPIXEL
from machine import Pin
from neopixel import NeoPixel

pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (255, 255, 255) # set the first pixel to white
np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour

"""

"""
import dht
import machine

d = dht.DHT11(machine.Pin(4))
d.measure()
d.temperature() # eg. 23 (°C)
d.humidity()    # eg. 41 (% RH)

d = dht.DHT22(machine.Pin(4))
d.measure()
d.temperature() # eg. 23.6 (°C)
d.humidity()    # eg. 41.3 (% RH)

"""
