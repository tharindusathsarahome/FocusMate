import time
from pygame import mixer

mixer.init()

def play_alarm(file_path, volume=0.7):
    mixer.music.load(file_path)
    mixer.music.set_volume(volume)
    mixer.music.play()

def stop_alarm():
    mixer.music.stop()

def spent(minutes, start_time):
    time_now = int(time.time())
    return 1 if time_now - start_time > minutes else 0
