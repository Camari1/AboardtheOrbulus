import pygame
from pygame import mixer


# This function progresses the story.
def next():
    answer = input("Press \"ENTER\" to continue...")
    if answer == '':
        pass


# This will be used for the save function, by appending the player's input of choices to the list.
save = []
# This function is used for items in the story. If a player has an item in the dictionary,
# the items that they have could be useful in the future.
items = {}

music_list = {1: "assets/Start_Music.mp3", 2: "assets/Odd.mp3"}


def play_music(number_list, volume, length=0.0):
    pygame.mixer.music.load(music_list[number_list])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1, length)


