import math
import spotipy
from config import config
from spotipy.oauth2 import SpotifyOAuth
from pywinauto.findwindows    import find_window
from win32gui import SetForegroundWindow
from pywinauto import Application
import os
import win32gui
config = config()

client_id = config.client_id
client_secret = config.client_secret
redirect_uri = config.redirect_uri

class SpotifyControl:
    def __init__(self):
        #self.username = username
        self.scope = "user-modify-playback-state user-read-private user-read-playback-state user-read-recently-played " \
        "user-read-playback-state user-top-read user-read-email"
        auth_manager = SpotifyOAuth(scope=self.scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
        self.sp = spotipy.Spotify(auth_manager=auth_manager)
        self.getUsername()


    def pauseplay(self):
        playback = self.sp.current_playback()
        if playback is None:
            self.sp.start_playback()
        else:
            playback = playback.get("is_playing")
        if playback is True:
            self.sp.pause_playback()
        else:
            self.sp.start_playback()

    def next(self):
        self.sp.next_track()

    def back(self):
        if self.elapsedTime(False) <= 3:
            self.sp.previous_track()
        else:
            self.sp.seek_track(0)

    def email(self):
        return self.sp.me().get("email")

    def getUsername(self):
        return self.sp.me().get("display_name")

    def elapsedTime(self, isList):
        ms = self.sp.current_playback()
        if ms is not None:
            ms = ms.get("progress_ms")
            sec = round(ms / 1000)
            if not isList:
                return sec
            else:
                min = math.floor(sec / 60)
                sec = sec % 60
                return [min, sec]
        else:
            return None

    def makeForeground(self):
        w = win32gui
        t = w.GetWindowText(w.GetForegroundWindow())
        com = "tasklist /fi \"imagename  eq Spotify.exe \" /fo \"list\""
        var = os.popen(com).read()
        if var.count("Spotify.exe") > 0:
            nameList=var.split(":")
            pidStr = nameList[2]
            pid = int(pidStr.split(" ")[10].split("\n")[0])
        app = Application().connect(process=pid)
        app.top_window().set_focus()
        return t

    def setForeground(self, name):
        SetForegroundWindow(find_window(title=name))
        return None

    def increaseVolume(self):
        volume = self.sp.current_playback().get("device").get("volume_percent")
        self.sp.volume(volume + 5)

    def lowerVolume(self):
        volume = self.sp.current_playback().get("device").get("volume_percent")
        self.sp.volume(volume - 5)




