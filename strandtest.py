# main.py -- put your code here!

"""Animations for use on micropython board, tested on pyboardv11 with stm32f04 chip.
Animation code based on rpi_ws281x library from jgarff and with the compilation for micropython from JanBednarik.
Questions to programm LED Strips ask me a.hoch90@gmail.com""" 

from ws2812 import WS2812
import time
led_count = 14       #Set number of pixels
spi_bus_number = 1   #Connect "X8" MOSI to LED Strip Data Signal (DIN)
chain = WS2812(spi_bus_number, led_count)
data = []
color_val = tuple(x for x in range(led_count))

for colors in color_val:
    data.append((0,0,0))


def colorWipe(data, color, wait_ms=50):
    for i in range(led_count):
        data[i]= (color[0], color[1], color[2])
        chain.show(data)
        time.sleep(wait_ms / 1000.0)


def wheel(pos):  
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)


def rainbow(data, wait_ms=2, iterations=1):
    for j in range(256 * iterations):
        for i in range(led_count):
            data[i] = wheel((i + j) & 255)
            chain.show(data)
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(data, wait_ms=20, iterations=5):
    for j in range(256 * iterations):
        for i in range(led_count):
            data[i] =wheel((int(i * 256 / led_count) + j) & 255)
            chain.show(data)
        time.sleep(wait_ms / 1000.0)

   
while True:
    colorWipe(data, (255, 0, 0))  # Red wipe
    colorWipe(data, (0, 255, 0))  # Blue wipe
    colorWipe(data, (0, 0, 255))  # Green wipe
    colorWipe(data, (0, 0, 0))  # Green wip
    rainbow(data)
    rainbowCycle(data)
