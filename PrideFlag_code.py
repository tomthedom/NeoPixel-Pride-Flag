# NeoPixel Pride Flag
# Author: Tom the Dom
# License: MIT

import time
from time import sleep
import board
import neopixel

# Data pin on your CircuitPy board
pixel_pin = board.A1

# The number of NeoPixels
num_pixels = 240 

# Time in seconds to show each flag
SHOWTIME = 60

# Time in seconds to blank pixels between flags
SLEEPTIME = 1

# The order of the pixel colors - RGB, GRB, RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.01, auto_write=False, pixel_order=ORDER
)

while True:
    # Classic Pride flag
    for c in range(0, num_pixels):
        if c in range(0, 40):
            pixels[c] = (118, 0, 137) # Patriarch Purple
        elif c in range(40, 80):
            pixels[c] = (0, 68, 255) # Blue
        elif c in range(80, 120):
            pixels[c] = (0, 129, 31) # La Salle Green
        elif c in range(120, 160):
            pixels[c] = (255, 239, 0) # Canary Yellow
        elif c in range(160, 200):
            pixels[c] = (224, 109, 7) # Orange
        elif c in range(200, 240):
            pixels[c] = (231, 0, 0) # Electric Red
        else:
            pixels[c] = (0,0,0)
    pixels.show()
    sleep (SHOWTIME)

    # Blank out all pixels
    pixels.fill((0,0,0))
    pixels.show()
    sleep (SLEEPTIME)

    # Transgender Pride flag
    for t in range(0, num_pixels):
        if t in range(0, 40):
            pixels[t] = (65, 175, 222) # Maya Blue
        elif t in range(40, 80):
            pixels[t] = (217, 148, 144) # Amaranth Pink
        elif t in range(80, 160):
            pixels[t] = (255, 255, 255) # White
        elif t in range(160, 200):
            pixels[t] = (217, 148, 144) # Amaranth Pink
        elif t in range(200, 240):
            pixels[t] = (65, 175, 222) # Maya Blue
        else:
            pixels[t] = (0,0,0)
    pixels.show()
    sleep (SHOWTIME)

    # Blank out all pixels
    pixels.fill((0,0,0))
    pixels.show()
    sleep (SLEEPTIME)

    # Pansexual Pride flag
    for p in range(0, num_pixels):
        if p in range(0, 80):
            pixels[p] = (5, 174, 255) # Blue Bolt
        elif p in range(80, 160):
            pixels[p] = (255, 218, 0) # Sizzling Sunrise
        elif p in range(160, 240):
            pixels[p] = (255, 20, 140) # Deep Pink
        else:
            pixels[t] = (0,0,0)
    pixels.show()
    sleep (SHOWTIME)

    # Blank out all pixels
    pixels.fill((0,0,0))
    pixels.show()
    sleep (SLEEPTIME)