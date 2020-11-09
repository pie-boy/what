from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

blue = (0,0,255)
green = (0,255,0)

x = 4
y = 4

piman = sense.set_pixel(x,y,blue)

while True:
     for event in sense.stick.get_events():
        
        # check if joystick is pressed
        if event.action == 'pressed':
            
            #check which direction has been pressed
            if event.direction == 'up':
                y = (y+1)
    