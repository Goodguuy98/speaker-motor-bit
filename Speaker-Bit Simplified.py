#-----------Micropython docs-------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/index.html

#-----------Radio Tutorial---------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/radio.html

#-----------   Radio API  ---------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/radio.html


from microbit import *
import radio
import speech

#The radio needs to be on to work.
radio.on()

#Set the group to 1
radio.config(group=1)

def operation(phrase):
    radio.send("Disp")

    #Wait for a reply
    while True:
        request = radio.receive()
        if request:
            if request == "Done":
                #State phrase
                speech.say(phrase)
                break

    #Begin rotating backward
    radio.send("Retu")

    #Wait for rotation to complete
    while True:
    request = radio.receive()
    if request:
        if request == "Done":
            #Exit Function
            break


#Event loop.
while True:

#P0 PTM and P1 PTM ------------------------------

    #This will trigger if pin0 is pressed. (i.e, == 1)
    if pin0.is_touched():
        operation()

    if pin1.is_touched():
        operation("No")

#Onboard Pin

    if pin_logo.is_touched():
        radio.send("Stop")
        reset()

