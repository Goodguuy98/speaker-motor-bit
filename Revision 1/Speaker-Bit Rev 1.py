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

mode = "A"
display.show(mode)

def transition(val):
    #Make the 'mode' variable accessible
    global mode

    radio.send(val)

    #Give the Motor:bit some time to reply
    while True:

        #If a radio transmission is received, the mode swap is confirmed
        if radio.receive():

            mode = val
            display.show(mode)
            break


#Event loop.
while True:

#P0 PTM and P1 PTM ------------------------------

    #This will trigger if pin0 is pressed. (i.e, == 1)
    if pin0.is_touched():

        if mode == "A":
            speech.say("I'm Happy")

        elif mode == "B":
            speech.say("That's funny")

    if pin1.is_touched():

        if mode == "A":
            speech.say("I'm sad")

        elif mode == "B":
            speech.say("I need help")

#Onboard A and Onboard B---------------------

    if button_a.was_pressed():
        if mode != "A":
            transition("A")

    if button_b.was_pressed():
        if mode != "B":
            transition("B")
