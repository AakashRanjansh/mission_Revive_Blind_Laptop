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


key_function = {
    'k+1': pcscreenonly,
    'k+2': duplicate,
    'k+3': extenddisplay,
    'k+4': startsecondscreen,
    'k+5': launchpcremotereceiver,
}


while True:
    for key, function in key_function.items():
        if is_pressed(key):
            function()
