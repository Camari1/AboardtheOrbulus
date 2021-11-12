import colorama
from colorama import Fore, Style
from functions import save_list, lines, items
from dialogues_lines import choices_dialogue

colorama.init(autoreset=True)


# These are all the functions used to decide the choices for the players. The choices are ordered from end to the
# beginning of the story(that's why the choice order is increased rather than decreased). So the end of the code is
# the first players choice, and everything else goes in order. However, the main story (AboardtheOrbulus.py) is
# ordered from beginning to end.
def choice8():
    player_choose8 = ""

    while player_choose8 != "1" or player_choose8 != "2":
        player_choose8 = input(Fore.RED + "What will you do?\n*Please type a number, or a number listed above* " + Style.RESET_ALL)
        if player_choose8 == "1":
          lines(choices_dialogue, 0)
          save_list(int(player_choose8))
          break
        elif player_choose8 == "2":
          lines(choices_dialogue, 1)
          items("end")
          save_list(int(player_choose8))
          break


def choice7():
    player_choose7 = ""

    while player_choose7 != "1" or player_choose7 != "2":
        player_choose7 = input(Fore.RED + "What will you do?\n*Please type a number, or a number listed above* " + Style.RESET_ALL)
        if player_choose7 == "1":
          lines(choices_dialogue, 2)
          items("fight")
          save_list(int(player_choose7))
          break
        elif player_choose7 == "2":
          lines(choices_dialogue, 3)
          items("run")
          save_list(int(player_choose7))
          break


def choice6():
    player_choose6 = ""

    while player_choose6 != "1" or player_choose6 != "2":
        player_choose6 = input(Fore.RED + "What will you do?\n*Please type a number, or a number listed above* " + Style.RESET_ALL)
        if player_choose6 == "1":
          lines(choices_dialogue, 4)
          items("flint and matches")
          save_list(int(player_choose6))
          break
        elif player_choose6 == "2":
          lines(choices_dialogue, 5)
          save_list(int(player_choose6))
          break


def choice5():
    player_choose5 = ""

    while player_choose5 != "1" or player_choose5 != "2":
        player_choose5 = input(Fore.RED + "What will you do?\n*Please type a number, or a number listed above* " + Style.RESET_ALL)
        if player_choose5 == "1":
          lines(choices_dialogue, 6)
          items("map")
          save_list(int(player_choose5))
          break
        elif player_choose5 == "2":
          save_list(int(player_choose5))
          pass
          break
    

def choice4():
    player_choose4 = ""

    while player_choose4 != "1" or player_choose4 != "2":
        player_choose4 = input(Fore.RED + "What will you do?\n*Please type a number, or a number listed above* " + Style.RESET_ALL)
        if player_choose4 == "1":
          lines(choices_dialogue, 7)
          save_list(int(player_choose4))
          break
        elif player_choose4 == "2":
          lines(choices_dialogue, 8)
          save_list(int(player_choose4))
          break


def choice3():
    player_choose3 = ""

    while player_choose3 != "1" or player_choose3 != "2" or player_choose3 != "3":
        player_choose3 = input(Fore.RED + "What will you do?\n*Please type a number, or a number listed above* " + Style.RESET_ALL)
        if player_choose3 == "1":
          lines(choices_dialogue, 9)
          items('key')
          save_list(int(player_choose3))
          break
        elif player_choose3 == "2":
          lines(choices_dialogue, 10)
          items("infected")
          save_list(int(player_choose3))
          break
        elif player_choose3 == "3":
          lines(choices_dialogue, 11)
          save_list(int(player_choose3))
          break


def choice2():
    player_choose2 = ""

    while player_choose2 != "1" or player_choose2 != "2":
        player_choose2 = input(Fore.RED + "What will you do?\n*Please type a number, or a number listed above* " + Style.RESET_ALL)
        if player_choose2 == "1":
          lines(choices_dialogue, 12)
          save_list(int(player_choose2))
          break
        elif player_choose2 == "2":
          lines(choices_dialogue, 13)
          save_list(int(player_choose2))
          break


def choice():
    player_choose1 = ""

    while player_choose1 != "1" or player_choose1 != "2":
        player_choose1 = input(Fore.RED + "What will you do?\n*Please type a number, or a number listed above* " + Style.RESET_ALL)
        if player_choose1 == "1":
          lines(choices_dialogue, 14)
          save_list(int(player_choose1))
          break
        elif player_choose1 == "2":
          lines(choices_dialogue, 15)
          save_list(int(player_choose1))
          choice2()
          break