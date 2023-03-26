# NeoPixel Pride Flag
# Author: Tom the Dom
# License: MIT

import board
import neopixel
from time import sleep

# Data pin on your CircuitPy board
pixel_pin = board.A1

# The number of NeoPixels (preferably a multiple of 6)
num_pixels = 240

# Width of flag (num_pixels divided by 6, rounded down)
WIDTH = num_pixels // 6

# Define positions of each flag segment break
W1 = WIDTH
W2 = WIDTH * 2
W3 = WIDTH * 3
W4 = WIDTH * 4
W5 = WIDTH * 5
W6 = WIDTH * 6

# Time in seconds to show each flag
SHOWTIME = 60

# Time in seconds to blank pixels between flags
SLEEPTIME = 1

# The order of the pixel colors - RGB, GRB, RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.02, auto_write=False, pixel_order=ORDER
)

while True:
    # Transgender Pride flag
    for t in range(0, num_pixels):
        if t in range(0, W1):
            pixels[t] = (65, 175, 222) # Maya Blue
        elif t in range(W1, W2):
            pixels[t] = (247, 134, 120) # Amaranth Pink
        elif t in range(W2, W4):
            pixels[t] = (255, 255, 255) # White
        elif t in range(W4, W5):
            pixels[t] = (247, 134, 120) # Amaranth Pink
        elif t in range(W5, W6):
            pixels[t] = (65, 175, 222) # Maya Blue
        else:
            pixels[t] = (0,0,0)
    pixels.show()
    sleep (SHOWTIME)

    # Blank out all pixels
    pixels.fill((0,0,0))
    pixels.show()
    sleep (SLEEPTIME)

    # Classic Pride flag
    for c in range(0, num_pixels):
        if c in range(0, W1):
            pixels[c] = (118, 0, 137) # Patriarch Purple
        elif c in range(W1, W2):
            pixels[c] = (0, 68, 255) # Blue
        elif c in range(W2, W3):
            pixels[c] = (0, 129, 31) # La Salle Green
        elif c in range(W3, W4):
            pixels[c] = (255, 239, 0) # Canary Yellow
        elif c in range(W4, W5):
            pixels[c] = (224, 109, 7) # Orange
        elif c in range(W5, W6):
            pixels[c] = (231, 0, 0) # Electric Red
        else:
            pixels[c] = (0,0,0)
    pixels.show()
    sleep (SHOWTIME)

    # Blank out all pixels
    pixels.fill((0,0,0))
    pixels.show()
    sleep (SLEEPTIME)

    # Pansexual Pride flag
    for p in range(0, num_pixels):
        if p in range(0, W2):
            pixels[p] = (5, 174, 255) # Blue Bolt
        elif p in range(W2, W4):
            pixels[p] = (255, 218, 0) # Sizzling Sunrise
        elif p in range(W4, W6):
            pixels[p] = (255, 20, 140) # Deep Pink
        else:
            pixels[p] = (0,0,0)
    pixels.show()
    sleep (SHOWTIME)

    # Blank out all pixels
    pixels.fill((0,0,0))
    pixels.show()
    sleep (SLEEPTIME)
