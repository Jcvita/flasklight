"""
Helper functions for flask server at app.py
"""

import time
import board
import neopixel

num_lights = 600
npboard = board.D18
order = neopixel.RGB

lights = neopixel.NeoPixel(npboard, num_lights, pixel_order=order, auto_write=False) #RPI board

previous_display = ['']

def alert(rgb: tuple):
    lights.fill(rgb)
    time.sleep(.2)
    lights.fill(0, 0, 0)
    time.sleep(.2)
    lights.fill(rgb)
    time.sleep(.2)
    lights.fill(0, 0, 0)
    time.sleep(.2)
    return_to_previous(f'{rgb} alert')
    print(f'Alert color {rgb}')

def fill(rgb: tuple):
    previous_display = ['fill', rgb]
    lights.fill(rgb)
    print(f'Fill color {rgb}')


def razer_rainbow(speed: float):
    previous_display = ['razer_rainbow', speed]
    #TODO razer rainbow
    print(f'Razer rainbow with speed {speed}')

def return_to_previous(current: str):
    if previous_display[0] == 'razer_rainbow':
        razer_rainbow(previous_display[1])
    elif previous_display[0] == 'fill':
        fill(previous_display[1])
    else:


    print(f'Finished {current}, reverting to {previous_display}')

