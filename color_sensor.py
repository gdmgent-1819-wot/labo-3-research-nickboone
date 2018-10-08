#!/usr/bin/env python

import sys
import time
from sense_hat import SenseHat
import flotilla
sense_hat = SenseHat()

print("""
Reading Colour values.

Press CTRL+C to exit.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding module...")
def main(color,x,y):
    print(color.red,
            color.green,
            color.blue,
            )
    for x in range(0,8):
        for y in range(0,8):
            sense_hat.set_pixel(x,y,color.red ,color.green,color.blue)
    

try:
    while True:
        x= 0
        y= 0
        color = dock.first(flotilla.Colour)
        time.sleep(1)
        main(color,x,y)
        time.sleep(2)
        sense_hat.clear()
            
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
