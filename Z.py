from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
cyan = (0,255,255)
magenta = (255,0,255)
black = (50,150,50)
white = (255,255,255)

sense.show_letter("u", blue)
sleep(.5)
sense.show_letter("r", green)
sleep(.5)
sense.show_letter("s", cyan)
sleep(.5)
sense.show_letter("o", black)
sleep(.5)
sense.show_letter("t", yellow)
sleep(.5)
sense.show_letter("h", white)
sleep(.5)
sense.show_letter("i", red)
sleep(.5)
sense.show_letter("c", magenta)