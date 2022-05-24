from microbit import *
import radio
import neopixel

#Klip Motor Control Code-------------------------------------------------------
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
#----------------------------------------------------------------------

# Create a new instance of the Klip Motor class
klip = KitronikKlipMotor

#The radio needs to be on to work.
radio.on()

#Set the group to 1
radio.config(group=1)

#Confirm device is on
display.show(Image.CONFUSED)

def rotation(movement):

    display.show(Image.ANGRY)

    # Drive Motor 1 at given direction
    klip.motorOn(klip, "Motor1", movement, 50)

    #Wait for x miliseconds
    sleep(540)

    #Turn off
    klip.motorOff(klip, "Motor1")

    radio.send("Done")

while True:

    request = radio.receive()
    if request:

        #Rotation for display
        if request == "Disp":
            rotation("forward")

        #Roatation for return
        if request == "Recu":
            rotation("reverse")
