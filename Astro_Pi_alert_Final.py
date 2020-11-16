
from sense_hat import SenseHat

sense = SenseHat()
sense.clear

## finding the temp :success:
#temp = sense.get_temperature()

#print(temp)
##

## finding pressure :success:
#pressure = sense.get_pressure() 

#print(pressure)
##

#interacting with sensor reuslts:

red = (255,0,0)
green = (0,255,0)

    #take reading from all sensors (make variables)
temp = sense.get_temperature()
press = sense.get_pressure()
    
    #round the variables to one decimal place
temp = round(temp,1)
press = round(press,1)

    
    #create a message
message = "Temp: " + str(temp) + " Pressure: " + str(press)
 
    
    # average ISS temp is 24 degrees - the following temperatures allow for some lee-way just in case of false alarms.
if temp > 20 and temp < 30:
    bg = green
else:
    bg = red
    sense.show_message("!!WARNING!!", back_colour=red)
    
#this is the pressure level on ISS, if it does not equal this at all times there will be trouble, therefore we use '!=' operation.
    if press != 1013:
        bg = red
        sense.show_message("!PRESSURE LEVELS abnormal!", back_colour=red)
    
    #display message
    sense.show_message(message, scroll_speed = 0.075, back_colour = bg)

##
#while True:
    #for event in sense.stick.get_events():

 # check if joystick is pressed
        #if event.action == 'pressed':
            
            #check which direction has been pressed
            #if event.direction == 'up':
                #sense.clear()
           # elif event.direction == 'down':
               # sense.clear()
           # elif event.direction == 'left':
            #    sense.clear()
           # elif event.direction == 'right':
            #    sense.clear()
          #  elif event.direction == 'middle':
             #   sense.clear()
       # elif event.action == 'released':
           # sense.clear()
        
# this doesn't work ... so let's try this vvv
##
def blue():
    sense.clear(0,0,255)
    
sense.stick.direction_down = blue

#although the reaction isnt immediate , this'll do...











