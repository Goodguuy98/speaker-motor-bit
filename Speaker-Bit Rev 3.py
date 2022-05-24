from microbit import *
import radio
import speech

#Indicate device is powered on
display.show(Image.HAPPY)

mode = "A"

#The radio needs to be on to work.
radio.on()

#Set the group to 1
radio.config(group=1)

#The speaker also should be on
speaker.on()

#Max power!
set_volume(255)

#Happy Emotion-------------------------------------------------------------------------
happy1 = Image('00000:'
            '09090:'
            '00000:'
            '90009:'
            '09990')

happy2 = Image('00000:'
            '09090:'
            '00000:'
            '99999:'
            '09990')

happy = [happy1, happy2]
#-------------------------------------------------------------------------------------
#Sad Emotion--------------------------------------------------------------------------
sad1 = Image('00000:'
            '09090:'
            '00000:'
            '09990:'
            '90009')

sad2 = Image('00000:'
            '09090:'
            '00000:'
            '09990:'
            '99999')

sad = [sad1, sad2]
#--------------------------------------------------------------------------------------
#Angry Emotion-------------------------------------------------------------------------
angry1 = Image('90009:'
            '09090:'
            '00000:'
            '99999:'
            '90909')
angry2 = Image('90009:'
            '09090:'
            '00000:'
            '99999:'
            '99999')

angry = [angry1, angry2]
#-------------------------------------------------------------------------------------
#Wink Emotion-------------------------------------------------------------------------
wink1 = Image('00000:'
            '09099:'
            '00000:'
            '90009:'
            '09990')

wink2 = Image('00000:'
            '09099:'
            '00000:'
            '99999:'
            '09990')

wink = [wink1, wink2]

def request(req):
    radio.send(req)

    while True:
        if radio.receive():
            break
        
        if pin_logo.is_touched():
            reset()

def speak(phrase, expression, fanfare):

    display.show(expression[0])
    audio.play(fanfare)

    sleep(1000)
    display.show(expression, delay=150, wait=False, loop=True, clear=False)
    speech.say(phrase)
    display.show(expression[0])
    sleep(1000)

#Event loop.
while True:

    display.show(mode)

#P0 PTM and P1 PTM ------------------------------

    #This will trigger if pin0 is pressed. (i.e, == 1)
    if pin0.is_touched():
        request("Disp")

        if mode == "A":
            speak("Hello, my name is MicroBit.", happy, Sound.HAPPY)
        elif mode == "B":
            speak("It is raining outside.", sad, Sound.SAD)

        request("Recu")

    #if pin1.is_touched():
    if pin1.is_touched():
        request("Disp")

        if mode == "A":
            speak("Things are going great.", wink, Sound.HELLO)
        elif mode == "B":
            speak("What did you just say to me?", angry, Sound.SLIDE)

        request("Recu")
        
    if pin_logo.is_touched():
        reset()

#Modes ---------------------------

    if button_a.was_pressed():
        mode = "A"

    if button_b.was_pressed():
        mode = "B"
