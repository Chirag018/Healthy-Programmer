from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        inputs = input()
        if inputs == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 10*60
    exsecs = 30*60
    eyessecs = 40*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time")
            musiconloop('water.mp3', 'stop')
            init_water = time()
            log_now("Drank Water at")
        if time() - init_eyes > eyessecs:
            print("Eye exercise time")
            musiconloop('eyes.mp3', 'stop')
            init_eyes = time()
            log_now("Eye exercise  at")
        if time() - init_exercise > exsecs:
           print("Exercise time")
           musiconloop('physical.mp3', 'stop')
           init_exercise = time()
           log_now("Exercise time at")
