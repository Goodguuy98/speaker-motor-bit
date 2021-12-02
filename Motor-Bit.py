#-----------Micropython docs-------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/index.html

#-----------Radio Tutorial---------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/radio.html

#-----------   Radio API  ---------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/radio.html


from microbit import *
import radio
import speech
import time

#The radio needs to be on to work.
radio.on()

#Set the group to 1
radio.config(group=1)

mode = "A"
display.show(mode)
def flip(val):
    #To prevent contradictary requests
    radio.config(group=2)

    #Set mode
    mode = val
    display.show(mode)

    radio.config(group=1)
    radio.send(val)

while True:

    request = radio.receive()
    if request:

        if request == "A": #and mode != "A":
            flip(request)

        elif request == "B": #and mode != "B":
            flip(request)
