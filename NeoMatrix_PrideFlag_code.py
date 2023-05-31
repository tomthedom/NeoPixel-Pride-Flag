# NeoPixel NeoMatrix Pride Flag
# Author: Tom the Dom
# License: MIT

import board
from time import sleep
from rainbowio import colorwheel
import neopixel

# Data pin on your CircuitPy board
pixel_pin = board.D1

# The number of NeoPixels
num_pixels = 64

# Time in seconds to show each flag
SHOWTIME = 5

# Time in seconds to blank pixels between flags
SLEEPTIME = 0.5

# The order of the pixel colors - RGB, GRB, RGBW or GRBW.
ORDER = neopixel.GRB

# Define NeoPixel
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.01, auto_write=False, pixel_order=ORDER
)

# Define functions

def blank(wait):
    pixels.fill((0,0,0))
    pixels.show()
    sleep (wait)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(8, 56):
            rc_index = (i * 256 // 48) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        sleep(wait)

def classic_flag(wait):
        for c in range(0, num_pixels):
            if c in range(8, 16):
                pixels[c] = (231, 0, 0) # Electric Red
            elif c in range(16, 24):
                pixels[c] = (224, 109, 7) # Orange
            elif c in range(24, 32):
                pixels[c] = (255, 239, 0) # Canary Yellow
            elif c in range(32, 40):
                pixels[c] = (0, 129, 31) # La Salle Green
            elif c in range(40, 48):
                pixels[c] = (0, 68, 255) # Blue
            elif c in range(48, 56):
                pixels[c] = (118, 0, 137) # Patriarch Purple
            else:
                pixels[c] = (0,0,0)
        pixels.show()
        sleep (wait)

def transgender_flag(wait):
        for t in range(0, num_pixels):
            if t in range(8, 16):
                pixels[t] = (65, 175, 222) # Maya Blue
            elif t in range(16, 24):
                pixels[t] = (247, 134, 120) # Amaranth Pink
            elif t in range(24, 32):
                pixels[t] = (255, 255, 255) # White
            elif t in range(32, 40):
                pixels[t] = (247, 134, 120) # Amaranth Pink
            elif t in range(40, 48):
                pixels[t] = (65, 175, 222) # Maya Blue
            else:
                pixels[t] = (0,0,0)
        pixels.show()
        sleep (wait)

def pansexual_flag(wait):
        for p in range(0, num_pixels):
            if p in range(8, 24):
                pixels[p] = (255, 20, 140) # Deep Pink
            elif p in range(24, 40):
                pixels[p] = (255, 218, 0) # Sizzling Sunrise
            elif p in range(40, 56):
                pixels[p] = (5, 174, 255) # Blue Bolt
            else:
                pixels[p] = (0,0,0)
        pixels.show()
        sleep (wait)

def bisexual_flag(wait):
        for b in range(0, num_pixels):
            if b in range(8, 24):
                pixels[b] = (204, 1, 102) # Pink
            elif b in range(24, 32):
                pixels[b] = (185, 79, 180) # Purple
            elif b in range(32, 48):
                pixels[b] = (5, 46, 158) # Blue
            else:
                pixels[b] = (0,0,0)
        pixels.show()
        sleep (wait)

# Boot sequence

blank(1) # Blank out all pixels to show that reboot has taken place

rainbow_cycle(0)  # Color test rainbow cycle

blank(1) # Blank out all pixels to show that color test has finished

# Looping sequence

while True:

    classic_flag(SHOWTIME) # Classic Pride flag

    blank(SLEEPTIME) # Blank out all pixels

    transgender_flag(SHOWTIME) # Transgender Pride flag

    blank(SLEEPTIME) # Blank out all pixels
    
    pansexual_flag(SHOWTIME) # Pansexual Pride flag

    blank(SLEEPTIME) # Blank out all pixels

    bisexual_flag(SHOWTIME) # Bisexual Pride flag

    blank(SLEEPTIME) # Blank out all pixels