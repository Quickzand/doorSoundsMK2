import os, random, time, socket, datetime, requests
from pygame import mixer, time as pygameTime
import RPi.GPIO as GPIO
global recentlyPlayed;

DOOR_SENSOR_PIN = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN); 

# Connect to power on 17

SOUNDS_DIRECTORY = "./sounds/"

OPEN_SOUND = SOUNDS_DIRECTORY + "open.mp3"
CLOSE_SOUND = SOUNDS_DIRECTORY + "close.mp3"

isOpen = None

mixer.init()

print(mixer)

def playSound(soundFile):
    print("Playing " + soundFile)
    try:
        mixer.music.load(soundFile)
        mixer.music.set_volume(1)
        mixer.music.play()
    except Exception as e:
        print("Error playing sound: " + str(e))


def playOpenSound():
    playSound(OPEN_SOUND);

def playCloseSound():
    playSound(CLOSE_SOUND);


playOpenSound();
pygameTime.delay(1000) 
playCloseSound();
pygameTime.delay(1000)



oldIsOpen = False;

while(True):
    isOpen = not GPIO.input(DOOR_SENSOR_PIN);
    if(isOpen != oldIsOpen):
        if(isOpen):
            playOpenSound();
        else:
            playCloseSound();
        oldIsOpen = isOpen;
    time.sleep(0.1);
