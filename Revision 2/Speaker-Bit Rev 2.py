#-----------Micropython docs-------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/index.html

#-----------Radio Tutorial---------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/radio.html

#-----------   Radio API  ---------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/radio.html


from microbit import *
import radio
import speech

#Indicate device is powered on
display.show(Image.HAPPY)

#The radio needs to be on to work.
radio.on()

#Set the group to 1
radio.config(group=1)

#Dot Animation
dot1 = Image("00000:"
              "00000:"
              "90000:"
              "00000:"
              "00000")

dot2 = Image("00000:"
              "00000:"
              "90900:"
              "00000:"
              "00000")

dot3 = Image("00000:"
              "00000:"
              "90909:"
              "00000:"
              "00000")

dotAnim = [dot1, dot2, dot3]

def operation(phrase):
    #Operation in progress
    display.show(dotAnim, delay=400, wait=False, loop=True, clear=False)
    radio.send("Disp")

    #Request Rotation 1
    while True:


        request = radio.receive()

        #Request is returned
        if request:
            if request == "Done":
                #Confirm
                display.show(Image.YES)
                #State phrase
                speech.say(phrase)
                break

        #Reset functionality
        if pin_logo.is_touched():
            radio.send("Stop")
            reset()

    sleep(1000)
    #Operation in progress
    display.show(dotAnim, delay=400, wait=False, loop=True, clear=False)
    radio.send("Recu")

    #Request Rotation 2
    while True:

        request = radio.receive()

        if request:

            if request == "Done":
                #Confirm
                display.show(Image.YES)
                #Exit Function
                break

        if pin_logo.is_touched():
            radio.send("Stop")
            reset()


#Event loop.
while True:

#P0 PTM and P1 PTM ------------------------------

    #This will trigger if pin0 is pressed. (i.e, == 1)
    #if pin0.is_touched():
    if button_a.was_pressed():
        operation("Yes")

    #if pin1.is_touched():
    if button_b.was_pressed():
        operation("No")

#Onboard Pin
    if pin_logo.is_touched():
        radio.send("Stop")
        reset()
