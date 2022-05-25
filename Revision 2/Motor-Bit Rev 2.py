# Write your code here :-)
#-----------Micropython docs-------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/index.html

#-----------Radio Tutorial---------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/radio.html

#-----------   Radio API  ---------------
#https://microbit-micropython.readthedocs.io/en/v2-docs/radio.html

from microbit import *
import radio
import neopixel

#https://github.com/KitronikLtd/micropython-microbit-kitronik-klip-motor/blob/master/kitronikklipmotor.py-------------------------------------
class KitronikKlipMotor:
    # Function to control the turning on of motors
    # Each motor can have different direction and speed
    def motorOn(self, motor, direction, speed):

        if speed > 100:
            speed = 100
        elif speed < 0:
            speed = 0
        speed = speed * 10
        if motor == "Motor1":
            if direction == "forward":
                pin15.write_analog(speed)
                pin16.write_digital(0)
            elif direction == "reverse":
                pin16.write_analog(speed)
                pin15.write_digital(0)
        elif motor == "Motor2":
            if direction == "forward":
                pin13.write_analog(speed)
                pin14.write_digital(0)
            elif direction == "reverse":
                pin14.write_analog(speed)
                pin13.write_digital(0)

    # Function to control the turning off of motors
    def motorOff(self, motor):
        if motor == "Motor1":
            pin15.write_digital(0)
            pin16.write_digital(0)
        elif motor == "Motor2":
            pin13.write_digital(0)
            pin14.write_digital(0)
#----------------------------------------------------------------------------------------------------------------------------------------------

# Create a new instance of the Klip Motor class
klip = KitronikKlipMotor

#The radio needs to be on to work.
radio.on()

#Set the group to 1
radio.config(group=1)

#Confirm device is on
display.show(Image.CONFUSED)

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

def rotation():

    #Indicate rotation stage
    display.show(1)

    # Drive Motor 1 forward at 100% speed
    klip.motorOn(klip, "Motor1", "forward", 50)

    #Wait 1 second then turn off
    sleep(2000)
    klip.motorOff(klip, "Motor1")

    display.show(Image.YES)

    #Wait for Speaker:Bit to request turn back
    while True:
        radio.send("Done1")

        request = radio.receive()
        if request:

            if request == "Retu":

                #Indicate rotation stage
                display.show(2)

                # Drive Motor 1 backward at 100% speed for 1s, then turn off
                klip.motorOn(klip, "Motor1", "reverse", 50)

                #Wait 1 second then turn off
                sleep(2000)
                klip.motorOff(klip, "Motor1")

                #Confirm Completion
                display.show(Image.YES)

                sleep(500)
                radio.send("Done2")

            elif request == "Stop":
                reset()

while True:

    request = radio.receive()
    if request:

        #A rotation must take place
        if request == "Disp":
            rotation()

        #Micro:Bit has been requested to reset
        elif request == "Stop":
            reset()
