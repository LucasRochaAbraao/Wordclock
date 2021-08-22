#!/usr/bin/env python3
# coding=utf-8

#################################
#           WORDCLOCK           #
#      Lucas Rocha Abraao       #
#     lucasrabraao@gmail.com    #
#           20/08/2021          #
#################################

from datetime import datetime, timedelta

# TODO:
# - print to terminal time in words
# - função para ligar todas as leds
# - E pode ser qualquer um (choice entre opções)
# - da /horas/manhã/noite 10% de chance por hora (hora inteira)
# - se menos que 4 palavras, coloca o da noite/manhã/tarde (exceto meio dia/noite)
# - Erika eu te amo - botão e hora especial (código secreto - long press)
# - Draw stuff randomly for 5 minutes, or until button pressed. If
#   button pressed first, draw for 30 minutes or until button pressed again.


# Constants
MATRIX_W = 15 # X Pixels
MATRIX_H = 15 # Y Pixels

# Colors
RED     = [255, 0,   0  ]
LIME    = [0,   255, 0  ]
BLUE    = [0,   0,   255]
YELLOW  = [255, 255, 0  ]
FUCHSIA = [255, 0,   255]
AQUA    = [0,   255, 255]
WHITE   = [255, 255, 255]

# Birthday
BIRTH_MONTH = 8
BIRTH_DAY = 24

"""
sao é
tres cinco k
uma quatro vinte
duas oito
onze seis dez
nove quinze u (eu)
doze sete e
pra pras da meio noite
quinze vinte (te)
trinta e nove sete
uma oito duas
cinco dez seis
quatro tres e meia
horas dia e meio
Manhã tarde noite
"""

words_available = {
    # 1 2 3 4 5 6 7 8 9 10 11 12 15 20 HORAS
    0  : ['sao', 'é'],
    1  : ['três', 'cinco', 'k'],
    2  : ['uma', 'quatro', 'vinte'],
    3  : ['duas', 'oito'],
    4  : ['onze', 'seis', 'dez'],
    5  : ['nove', 'quinze', 'u'],
    6  : ['vinte', 'sete', 'e'],
    7  : ['pra', 'pras', 'da', 'meia', 'noite'],
    # 1 2 3 4 5 6 7 8 9 10 11 12 15 20 30 MINUTOS
    8  : ['quinze', 'vinte'],
    9  : ['trinta', 'e', 'nove', 'sete'],
    10 : ['uma', 'oito', 'duas'],
    11 : ['cinco', 'dez', 'seis'],
    12 : ['quatro', 'três', 'e', 'meio'],
    13 : ['horas', 'dia', 'e', 'meio', 'da'],
    14 : ['manhã', 'tarde', 'noite'],
}

matrix = [
    ['S', 'Ã', 'O', 'É', 'O', 'J', 'G', 'T', 'U', 'E', 'W', 'Z', 'N', 'X', 'A'], # 0
    ['T', 'R', 'Ê', 'S', 'K', 'P', 'C', 'I', 'N', 'C', 'O', 'M', 'K', 'Z', 'F'], # 1
    ['U', 'M', 'A', 'Q', 'U', 'A', 'T', 'R', 'O', 'P', 'V', 'I', 'N', 'T', 'E'], # 2
    ['D', 'U', 'A', 'S', 'D', 'H', 'W', 'Q', 'O', 'I', 'T', 'O', 'L', 'V', 'I'], # 3
    ['O', 'N', 'Z', 'E', 'Z', 'F', 'S', 'E', 'I', 'S', 'R', 'B', 'D', 'E', 'Z'], # 4
    ['N', 'O', 'V', 'E', 'J', 'N', 'U', 'Q', 'U', 'I', 'N', 'Z', 'E', 'U', 'K'], # 5
    ['W', 'R', 'F', 'V', 'I', 'N', 'T', 'E', 'Z', 'S', 'E', 'T', 'E', 'H', 'E'], # 6
    ['P', 'R', 'A', 'S', 'D', 'A', 'M', 'E', 'I', 'A', 'N', 'O', 'I', 'T', 'E'], # 7
    ['Y', 'F', 'Q', 'U', 'I', 'N', 'Z', 'E', 'O', 'S', 'V', 'I', 'N', 'T', 'E'], # 8
    ['T', 'R', 'I', 'N', 'T', 'A', 'E', 'N', 'O', 'V', 'E', 'S', 'E', 'T', 'E'], # 9
    ['U', 'M', 'A', 'A', 'V', 'O', 'I', 'T', 'O', 'S', 'Q', 'D', 'U', 'A', 'S'], # 10
    ['C', 'I', 'N', 'C', 'O', 'F', 'C', 'D', 'E', 'Z', 'S', 'E', 'I', 'S', 'Y'], # 11
    ['Q', 'U', 'A', 'T', 'R', 'O', 'T', 'R', 'E', 'S', 'E', 'M', 'E', 'I', 'O'], # 12
    ['H', 'O', 'R', 'A', 'S', 'D', 'I', 'A', 'E', 'M', 'E', 'I', 'O', 'D', 'A'], # 13
    ['M', 'A', 'N', 'H', 'Ã', 'T', 'A', 'R', 'D', 'E', 'N', 'O', 'I', 'T', 'E']  # 14
]


def get_time_phrase(hour, minute):

    #print(f'Hour: {hour}\nMinute: {minute} ')
    time_words = {
        1: [['uma'], [2 , [0, 1, 2]]],
        2: [['duas'], [3, [0, 1, 2, 3]]],
        3: [['três'], [1, [0, 1, 2, 3]]],
        4: [['quatro'], [2, [3, 4, 5, 6, 7, 8]]],
        5: [['cinco', 'cinco'], [1, [6, 7, 8, 9, 10]]],
        6: [['seis'], [4, [7, 8, 9, 10]]],
        7: [['sete'], [6, [9, 10, 11, 12]]],
        8: [['oito'], [3, [8, 9, 10, 11]]],
        9: [['nove'], [5, [0, 1, 2, 3]]],
        10: [['dez', 'dez'], [4, [12, 13, 14]]],
        11: [['onze'], [4, [0, 1, 2, 3]]],
        12: [['meio', 'meia'], []],
        13: [['uma'], []],
        14: [['duas'], []],
        15: [['três', 'quinze'], []],
        16: [['quatro'], []],
        17: [['cinco'], []],
        18: [['seis'], []],
        19: [['sete'], []],
        20: [['oito', 'vinte'], []],
        21: [['nove'], []],
        22: [['dez'], []],
        23: [['onze'], []],
        25: [['vinte e cinco', 'vinte e cinco'], []],
        30: [['meia', 'meia'], []],
        35: [['trinta e cinco', 'trinta e cinco'], []],
    }

    phrase = []
    
    if minute > 55:
        minute = 0
    # é 1h..., é meio dia..., é meia noite...
    if hour == 1 or hour == 12 or hour == 13 or hour == 0:
        phrase += ['é']
    else:
        phrase += ['são']

    if minute >= 40:
        hour += 1
        if hour == 24:
            hour = 0 #

    # HORA
    if hour == 0:
        phrase += ['meia noite']
        if minute == 0:
            return phrase
    elif hour == 23 and (minute > 55 or minute == 0):
        phrase = ['é meia noite']
        return phrase
    elif hour == 12:
        phrase += ['meio dia']
        if minute == 0:
            return phrase    
    elif hour == 11 and (minute > 55 or minute == 0):
        phrase = ['é meio dia']
        return phrase
    else:
        phrase += [f'{time_words[hour][0][0]}']

    # MINUTO
    if minute == 0 or minute == 60:
        phrase += ['horas']
        return phrase
    elif minute == 40:
        phrase.insert(1, 'vinte')
        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            phrase.insert(2, 'pra')
        else:
            phrase.insert(2, 'pras')
    elif minute == 45:
        phrase.insert(1, 'quinze')
        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            phrase.insert(2, 'pra')
        else:
            phrase.insert(2, 'pras')
    elif minute == 50:
        phrase.insert(1, 'dez')
        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            phrase.insert(2, 'pra')
        else:
            phrase.insert(2, 'pras')
    elif minute == 55:
        phrase.insert(1, 'cinco')
        if hour == 1 or hour == 12 or hour == 13 or hour == 0:
            phrase.insert(2, 'pra')
        else:
            phrase.insert(2, 'pras')
    else:
        phrase += ['e']
        phrase += [f'{time_words[minute][0][1]}']

    # Time of Day
    if hour > 0 and hour < 12:
        phrase += ['da manhã']
    elif hour >= 13 and hour < 19:
        phrase += ['da tarde']
    elif (hour >= 19 and hour < 23) or (hour == 23 and minute <= 59):
        phrase += ['da noite']
    return phrase

def main():    
    #time_reference = datetime.now() - timedelta(hours=5, minutes=-25)
    #time_reference.time()
    time_reference = datetime.now().time()
    current_minute = 5 * round(time_reference.minute/5)
    current_hour = time_reference.hour
    display_phrase = get_time_phrase(current_hour, current_minute)

    print(' '.join(display_phrase))
    print(time_reference)

if __name__ == '__main__':
    main()