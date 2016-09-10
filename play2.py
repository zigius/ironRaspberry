from subprocess import Popen
import os, time, signal
from omxplayer import OMXPlayer
from time import sleep

track_dir = '/home/pi/tracks/'
id_to_path = {
    1: track_dir + "conor.mp3",
    2: track_dir + "SwordArt.mp3",
    3: track_dir + "landslide.mp3"
}

def get_path(id):
  return id_to_path.get(id)

def play_track(id):
    track_path = get_path(id)
    player = OMXPlayer(track_path)
    player.play()
    sleep(20)
    player.quit()
if __name__ == '__main__':
    play_track(2)
