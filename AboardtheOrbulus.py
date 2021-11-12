import pygame
import colorama
from art import text2art
from pygame import mixer
from colorama import Fore, Style
from dialogues_lines import dialogue
from functions import item, play_music, save, lines
from choices import choice, choice4, choice5, choice6, choice7, choice8
from alternate_storylines import alternate_stories_1, alternate_stories_2, alternate_stories_3,  alternate_stories_4, alternate_stories_5, alternate_stories_6, alternate_stories_7, alternate_stories_8

colorama.init(autoreset=True)
mixer.init()

def main():
    play_music(1, 0.60)
    print("Rising Shield Studios Presents...\n")
    print(Fore.RED + text2art("Aboard The Orbulus", font="small") + Style.RESET_ALL)
    
    play_music(2, 0.04, 60.0)
    lines(dialogue, 0)
    choice()

    lines(dialogue, 1)

    alternate_stories_1()
    
    lines(dialogue, 2)

    if len(save) == 2:
      alternate_stories_2()

    lines(dialogue, 3)

    if len(save) == 1:
      lines(dialogue, 4)
    else:
      alternate_stories_3()

    lines(dialogue, 5)

    alternate_stories_4()

    lines(dialogue, 6)
    choice4()

    lines(dialogue, 7)

    lines(dialogue, 8)
    choice5()
    
    alternate_stories_5()

    lines(dialogue, 9)
    choice6()

    lines(dialogue,10)
    choice7()

    lines(dialogue, 11)
    choice8()

    if 'end' in item:
      lines(dialogue, 12)
      
    else:
      lines(dialogue, 13)

      alternate_stories_6()

      lines(dialogue, 14)

      alternate_stories_7()

      lines(dialogue, 15)

      alternate_stories_8()

if __name__ == "__main__":
    main()
