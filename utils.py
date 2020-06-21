"""
Helper functions for flask server at app.py
"""

import time
import board
import neopixiel
import threading
import random

num_lights = 600
npboard = board.D18
order = neopixel.RGB

lights = neopixel.NeoPixel(npboard, num_lights, pixel_order=order, auto_write=False) #RPI board


class AlertDaemon(object):
    def __init__(self, previous, color: tuple):
        self.color = color

    def alert(self):
        lights.fill(self.color)
        time.sleep(.2)
        lights.fill(0, 0, 0)
        time.sleep(.2)
        lights.fill(self.color)
        time.sleep(.2)
        lights.fill(0, 0, 0)
        time.sleep(.2)
        print(f'Alert color {rgb}')



class PartyDaemon(object):
    def __init__(self, frequency):
        self.frequency = frequency
        self._running = True

    def _stop(self):
        self._running = False

    def party(self):
        while self._running:
            lights.fill(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            time.sleep(1 / self.frequency)


class RainbowCycleDaemon(object):
    def __init__(self, frequency):
        self.frequency = frequency
        self._running = True
    
    def _stop(self):
        self._running = False

    def rainbow(self):
        start = 0
        while self._running:
            for x in range(num_lights):
                lights[(x + start) % 600] = hsv_to_rgb(x % 360, .99, .99)  
            if start == 600:
                start = 0
            start += 1
            time.sleep(self.frequency)


def hsv_to_rgb(h: int, s: float, v: float):
    """
    convert hsv format to rgb format
    
    https://www.rapidtables.com/convert/color/hsv-to-rgb.html
    """
    c = v * s
    x = c * (1 - abs((h/60) % 2 - 1))
    m = v - c
    
    if h < 61:
        (rp, gp, bp) = (c, x, 0)
    elif 61 < h < 121:
        (rp, gp, bp) = (x, c, 0)
    elif  121 < h < 181:
        (rp, gp, bp) = (0, c, x)
    elif 181 < h < 241:
        (rp, gp, bp) = (0, x, c)
    elif 241 < h < 301:
        (rp, bp, gp) = (x, 0, c)
    else:
        (rp, pb, gp) = (c, 0, x)
    
    return ((rp + m)*255, (gp + m)*255, (bp + m)*255)



def do_action(**kwargs):
    act = kwargs['action'] 

    r = RainbowCycleDaemon(kwargs['speed'])
    p = PartyDaemon(kwargs['party_frequency'])
    a = AlertDaemon(kwargs['alert_color']
    rt = threading.Thread(target=r.rainbow, daemon=True, name='rainbow')
    pt = threading.Thread(target=p.party, daemon=True, name='party')
    at = threading.Thread(target=a.alert, daemon=True, name='alert')


    if act == 'rainbow':
        p._stop()
        pt.join()
        
        rt.start()
    if act == 'party':
        r._stop()
        rt.join()

        pt.start()
    if act == 'fill':
        p._stop()
        r._stop()
        pt.join()
        rt.join()

        fill(kwargs['fill_color'])
    if act == 'alert':
        last = threading.current_thread().name
        
        at.start()
        at.join()


        do_action({'action': last})



def fill(rgb: tuple):
    lights.fill(rgb)
    print(f'Fill color {rgb}')
