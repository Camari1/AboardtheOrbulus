import pygame
from pygame import mixer

# This function progresses the story.
def next():
    answer = input("Press \"ENTER\" to continue...")
    if answer == '':
        pass
    
# This function is used for items in the story. If a player has an item in the dictionary,
# the items that they have could be useful in the future.
item = {}
def items(name):
    item[name] = 0 
    return item

# This will be used for the save function, by appending the player's input of choices to the list.
save = []
def save_list(choice_number):
    save.append(choice_number)
    return save
    
music_list = {1: "assets/Start_Music.mp3", 2: "assets/Odd.mp3"}
def play_music(number_list, volume, length=0.0):
    pygame.mixer.music.load(music_list[number_list])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1, length)

# This is a function that takes a certain list in the dialogues_lines.py file, and executes the dialogue and narration in the list.
def lines(list_name, story_number_list):
    for stories in list_name[story_number_list]:
        print(stories)
        next()
