#!/usr/bin/env python3

import random
from random import getrandbits
from machine import Pin
from neopixel import NeoPixel
import network, utime, ntptime
import time

# TODO:
# - da /horas/manhã/noite 10% de chance por hora (hora inteira)
# - Draw stuff randomly for 5 minutes, or until button pressed. If
#   button pressed first, draw for 30 minutes or until button pressed again.
# - new years countdown
#  CLEAR PIXEL: neopixel[x] = (0, 0, 0)


### synchronize with ntp
# need to be connected to wifi
def connect_wifi():
    print("Connecting to WiFi...")
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect('Ana Paula', 'naotemsenha')
    while not wifi.isconnected():
        print("Não foi possível conectar no wifi.")
        pass
    print("Connected.")

def update_time():
    ntptime.settime()
    local_time_ajustment = utime.time() + -3 * 3600
    local_time = utime.localtime(local_time_ajustment)
    return local_time

def flip_coin(weight):
    reference = random.getrandbits(3) / 7
    return True if weight >= reference else False

def get_color():
    random_index = getrandbits(3)
    colors = [
        (255, 0,   0  ), # RED
        (0,   255, 0  ), # GREEN
        (0,   0,   255), # BLUE
        (255, 255, 0  ), # YELLOW
        (255, 0,   255), # FUCHSIA
        (0,   255, 255), # AQUA
        (255, 255, 255), # WHITE
        (165,42,42)      # BROWN
    ]
    return colors[random_index]

def enable_pixel(neopx, index, size):
    """neopixel instance, index of first LED, size is how many LEDs to enable with index """
    for pixel in range(size):
        neopx[index+pixel] = get_color()

def main(hour, minute):
    # Birthday
    BIRTH_MONTH = 8
    BIRTH_DAY = 24

    special_words = {
        "": [9, 25, 41, 57, 73],
        "": [87, 88],
        "": [104, 119],
        "": [165, 166, 167]
    }

    pin = Pin(0, Pin.OUT)   # set GPIO0 (D3) to output to drive NeoPixels
    neopixel = NeoPixel(pin, 225)   # create NeoPixel driver on GPIO0 for 225 pixels

    if minute > 55:
        if hour!= 23: # qualquer hora menos 23
            hour += 1 # arredonda pra próxima hora de uma vez
        else:
            hour = 0 # mas se a hora era 23, a próxima precisa ser 0 e não 24.
        minute = 0 # arredonda minutos acima de 55 pra próxima hora.

    # é 1h..., é meio dia..., é meia noite...
    if (hour == 1 or hour == 12 or hour == 13 or hour == 0) and minute == 0:
        enable_pixel(neopixel, 3, 1) # é
    else:
        enable_pixel(neopixel, 0, 3) # são

    if minute >= 40:
        hour += 1
        if hour == 24:
            hour = 0 #

    # HORA
    if hour == 0:
        enable_pixel(neopixel, 125, 4) # meia
        enable_pixel(neopixel, 220, 5) # noite
        if minute == 0:
            return # finaliza a função com "é meia noite"

    elif hour == 23 and minute > 55 or hour == 0 and minute < 3: # se não for exatamente, como acima.
        #coords = list() # RESET PIXELS
        enable_pixel(neopixel, 3, 1) # é
        enable_pixel(neopixel, 125, 4) # meia

    elif hour == 12:
        enable_pixel(neopixel, 109, 4) # meio
        enable_pixel(neopixel, 114, 3) # dia
        if minute == 0:
            return # finaliza a função com "é meio dia"

    else:
        #coords.append(get_coord_hour(hour, pos=0)) # the hours?
        #????????????????????
        ...

    # MINUTO
    if minute == 0 and (hour == 1 or hour == 13):
        enable_pixel(neopixel, 195, 4) # hora

        #return coords

    if minute == 0:
        enable_pixel(neopixel, 195, 5) # horas

        if hour < 12:
            if flip_coin(weight=0.8): # weight returns True or False
                enable_pixel(neopixel, 208, 2) # da
                enable_pixel(neopixel, 210, 5) # manhã

        elif hour > 12 and hour < 18:
            if flip_coin(weight=0.5): # weight returns True or FalseA
                enable_pixel(neopixel, 208, 2) # da
                enable_pixel(neopixel, 215, 5) # tarde

        else:
            if flip_coin(weight=0.6): # weight returns True or False
                enable_pixel(neopixel, 208, 2) # da
                enable_pixel(neopixel, 220, 5) # noite

        #return coords

    elif minute == 25:
        enable_pixel(neopixel, 102, 1) # e
        enable_pixel(neopixel, 120, 5) # vinte
        enable_pixel(neopixel, 102, 5) # e
        enable_pixel(neopixel, 191, 5) # cinco

    elif minute == 35:
        enable_pixel(neopixel, 102, 1) # e
        enable_pixel(neopixel, 140, 6) # trinta
        enable_pixel(neopixel, 102, 1) # e
        enable_pixel(neopixel, 191, 5) # cinco

    elif minute == 40:
        enable_pixel(neopixel, 40, 5) # vinte

        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            enable_pixel(neopixel, 40, 3) # pra

        else:
            enable_pixel(neopixel, 40, 4) # pras

    elif minute == 45:
        enable_pixel(neopixel, 82, 6) # quinze

        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            enable_pixel(neopixel, 40, 3) # pra
        else:
            enable_pixel(neopixel, 40, 43) # pras

    elif minute == 50:
        enable_pixel(neopixel, 70, 3) # dez

        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            enable_pixel(neopixel, 40, 3) # pra
        else:
            enable_pixel(neopixel, 40, 4) # pras

    elif minute == 55:
        enable_pixel(neopixel, 20, 5) # cinco

        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            enable_pixel(neopixel, 40, 3) # pra

        else:
            enable_pixel(neopixel, 40, 4) # pras

    else: # cinco dez quinze vinte
        enable_pixel(neopixel, 146, 1) # e

        #coords.append(get_coord_minute(minute, pos=1)) # minute
        #????????????????

    # Time of Day
    if hour > 0 and hour < 12:
        if flip_coin(weight=0.8): # weight returns True or False
            enable_pixel(neopixel, 208, 2) # da
            enable_pixel(neopixel, 210, 5) #  manhã

    elif hour >= 13 and hour < 19:
        if flip_coin(weight=0.8): # weight returns True or Falsey
            enable_pixel(neopixel, 208, 2) # da
            enable_pixel(neopixel, 215, 5) # tarde

    elif (hour >= 19 and hour < 23) or (hour == 23 and minute <= 59):
        if flip_coin(weight=0.8): # weight returns True or False
            enable_pixel(neopixel, 208, 2) # da
            enable_pixel(neopixel, 220, 5) # noite
    print("Funcionando!")

if __name__ == '__main__':
    connect_wifi()
    while True:
        local_time = update_time()
        print(utime.localtime()) # year, month, mday, hour, minute, second, weekday (mon-sun: 0-6), yearday
        hour = 4
        minute = 20
        main(hour, minute)
        time.sleep(2)







#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




from machine import Pin
from neopixel import NeoPixel
from random import getrandbits
import time

# https://core-electronics.com.au/tutorials/copy-files-to-micropython.html
# micropython commands (for esp8266):
# sudo ampy -p /dev/ttyUSB0 -b 115200 ls
# sudo ampy -p /dev/ttyUSB0 -b 115200 rm main.py
# sudo ampy -p /dev/ttyUSB0 -b 115200 put main.py
# sudo ampy -p /dev/ttyUSB0 -b 115200 run main.py


pin = Pin(0, Pin.OUT)   # set GPIO0 (D3) to output to drive NeoPixels
neopixel = NeoPixel(pin, 12)   # create NeoPixel driver on GPIO0 for 8 pixels
#neopixel[0] = (255, 255, 255) # set the first pixel to white
#r, g, b = neopixel[0]         # get first pixel colors
#neopixel.write() # write data to all pixels

coords = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 1), (1, 2), (1, 3), (1, 4)],
    [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
]

matrix = [
#    0    1    2    3    4  
    'S', 'Ã', 'O', 'É', 'O', # 0
    'E', 'T', 'R', 'Ê', 'S', # 1
    'P', 'R', 'A', 'S', 'U', # 2
    'H', 'O', 'R', 'A', 'S', # 3
    'O', 'N', 'Z', 'E', 'G'  # 4
]

def get_sum_of_coords(coords):
    # coords = (6, 7) - basically the matrix position, and since the led strip is
    # a sequence of leds, the sum of the coords is the index of the led.
    return 5 * coords[0] + coords[1]

for word_coord in coords:
    for leds_to_activate in word_coord:
        print(get_sum_of_coords(leds_to_activate))

def random_color():
    colors = [
        (255,   0,   0), # red
        (  0, 255,   0), # green
        (  0,   0, 255), # blue
        (255, 255, 255)  # white
    ]
    #print(type(choice(colors)))

    return colors[getrandbits(2)]

for led in range(12):
    neopixel[led] = (0, 0, 0)

while True:
    for led in range(12):
        if led % 2 == 0:    
            #neopixel[led] = random_color() # set each led to a tuple representing r,g,b
            neopixel[led] = (255, 0, 0)
            print('LED ' + str(led) + ': ' + str(neopixel[led]))
            neopixel.write()  # only now will the updated values be shown
            #time.sleep(0.3)




"""
from adafruit website for raspberry pi:
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    pixels.show()
    time.sleep(1)

    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step

"""