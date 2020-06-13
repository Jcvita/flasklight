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

def alert(rgb: tuple):
    lights.fill(rgb)
    time.sleep(.2)
    lights.fill(rgb)
    return f"Alert with color {rgb}"



