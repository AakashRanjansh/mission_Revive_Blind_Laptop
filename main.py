from keyboard import is_pressed
from os import system
from playsound import playsound
from pyvolume import custom

custom(percent=100)


def pcscreenonly():
    system('DisplaySwitch /internal')
    playsound('Aa1.mp3')


def duplicate():
    system('DisplaySwitch /clone')
    playsound('Aa2.mp3')


def extenddisplay():
    system('DisplaySwitch /extend ')
    playsound('Aa3.mp3')


def startsecondscreen():
    system('DisplaySwitch /external')
    playsound('Aa4.mp3')


def launchpcremotereceiver():
    system("PCRemoteReceiver.exe")
    playsound('Aa5.mp3')


while True:
    if is_pressed('k+1'):
        pcscreenonly()
    elif is_pressed('k+2'):
        duplicate()
    elif is_pressed('k+3'):
        extenddisplay()
    elif is_pressed('k+4'):
        startsecondscreen()
    elif is_pressed('k+5'):
        launchpcremotereceiver()
