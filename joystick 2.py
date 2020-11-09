from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    for event in sense.stick.get_events():
        
        # check if joystick is pressed
        if event.action == 'pressed':
            
            #check which direction has been pressed
            if event.direction == 'up':
                sense.show_letter('u')
            elif event.direction == 'down':
                sense.show_letter('d')
            elif event.direction == 'left':
                sense.show_letter('l')
            elif event.direction == 'right':
                sense.show_letter('r')
            elif event.direction == 'middle':
                sense.show_letter('m')
        elif event.action == 'released':
            sense.clear()
                


                

                