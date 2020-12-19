from SpotifyControl import SpotifyControl
import keyboard
import pythoncom
from threading import Semaphore
from Hotkeys import Hotkeys
import os
import sys
from config import config

from main import checker

config = config()
username = config.username
print("username: " + username)

spot = SpotifyControl()
title = None
class Keylogger:
    global title
    def __init__(self):
        self.semaphore = Semaphore(0)

    def callback(self, event):
        global title
        pythoncom.CoInitialize()
        hk = Hotkeys()
        name = event.name
        keys = hk.hotkeys

        for hotkey in keys:
            if len(keys.get(hotkey)) == 1:
                if name == keys.get(hotkey)[0]:
                    if hotkey == "foregroundKey":
                       if title is None:
                         title = spot.makeForeground()
                       else:
                         title = spot.setForeground(title)
                    elif hotkey == "backKey":
                        spot.back()
                    elif hotkey == "nextKey":
                        spot.next()
                    elif hotkey == "pauseKey":
                        spot.pauseplay()
                    elif hotkey == "volumeUpKey":
                        spot.increaseVolume()
                    elif hotkey == "volumeDownKey":
                        spot.lowerVolume()
            elif len(keys.get(hotkey)) == 2:
                temp = keys.get(hotkey)
                first = temp[0]
                second = temp[1]
                if name == second and keyboard.is_pressed(first):
                    if hotkey == "foregroundKey":
                       if title is None:
                         title = spot.makeForeground()
                       else:
                         title = spot.setForeground(title)
                    elif hotkey == "backKey":
                        spot.back()
                    elif hotkey == "nextKey":
                        spot.next()
                    elif hotkey == "pauseKey":
                        spot.pauseplay()
                    elif hotkey == "volumeUpKey":
                        spot.increaseVolume()
                    elif hotkey == "volumeDownKey":
                        spot.lowerVolume()
            elif len(keys.get(hotkey)) == 3:
                temp = keys.get(hotkey)
                first = temp[0]
                second = temp[1]
                third = temp[2]
                if name == third and keyboard.is_pressed(first) and keyboard.is_pressed(second):
                    if hotkey == "foregroundKey":
                       if title is None:
                         title = spot.makeForeground()
                       else:
                         title = spot.setForeground(title)
                    elif hotkey == "backKey":
                        spot.back()
                    elif hotkey == "nextKey":
                        spot.next()
                    elif hotkey == "pauseKey":
                        spot.pauseplay()
                    elif hotkey == "volumeUpKey":
                        spot.increaseVolume()
                    elif hotkey == "volumeDownKey":
                        spot.lowerVolume()











    def start(self):
        # start the keylogger
        keyboard.on_press(callback=self.callback)
        self.semaphore.acquire()


    def end(self):
        sys.exit(0)

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()
