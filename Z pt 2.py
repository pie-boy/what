from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

def pick_random_colour():
    random_red = randint(0,255)
    random_green = randint(0,255)
    random_blue = randint(0,255)
    return (random_red,random_green,random_blue)

sense.show_letter("a", pick_random_colour())
sleep(.5)
sense.show_letter("y", pick_random_colour())
sleep(.5)
sense.show_letter("o", pick_random_colour())
sleep(.5)
sense.show_letter(",", pick_random_colour())
sleep(.5)
sense.show_letter("h", pick_random_colour())
sleep(.5)
sense.show_letter("u", pick_random_colour())
sleep(.5)
sense.show_letter("n", pick_random_colour())
sleep(.5)
sense.show_letter("t", pick_random_colour())