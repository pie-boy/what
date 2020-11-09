
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

while True:
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
    
    if press != 1013:
        bg = red
        sense.show_message("!PRESSURE LEVELS HIGH!", back_colour=red)
    
    #display message
    sense.show_message(message, scroll_speed = 0.075, back_colour = bg)
    
















