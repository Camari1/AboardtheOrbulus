import pygame
from pygame import mixer

# This function progresses the story.
def next():
    answer = input("Press \"ENTER\" to continue...")
    if answer == '':
        pass

music_list = {1: "assets/Start_Music.mp3", 2: "assets/Odd.mp3"}


def play_music(number_list, volume, length=0.0):
    pygame.mixer.music.load(music_list[number_list])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1, length)


