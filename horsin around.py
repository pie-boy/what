from sense_hat import SenseHat

sense = SenseHat()
sense.clear

guitar = (230,255,230)
tuba = (255,0,220)

sense.show_message("just coz u feel it, doesn't mean it's their", scroll_speed = 0.07, back_colour = guitar, text_colour = tuba)