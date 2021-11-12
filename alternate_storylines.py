import colorama
from choices import choice3
from functions import lines, save, items, item
from dialogues_lines import alternative_dialogues

colorama.init(autoreset=True)


# These are the alternate storylines for the progression of the story. The previous choices that a player makes
# determines what storyline will occur. The progression of the alternate storylines are ordered from beginning to
# end, in which they occur. It also depends on the previous choices you have made to determine, if the certain
# storylines will run.
def alternate_stories_1():
    if save[0] == 1:
      lines(alternative_dialogues, 0)
    elif save[0] == 2:
      lines(alternative_dialogues, 1)


def alternate_stories_2():
    if save[1] == 1:
      lines(alternative_dialogues, 2)

    elif save[1] == 2:
      lines(alternative_dialogues, 3)
      choice3()


def alternate_stories_3():
    if save[1] == 1:
      lines(alternative_dialogues, 4)

    elif save[1] == 2:
      lines(alternative_dialogues, 5)


def alternate_stories_4():
    if "infected" in item:
      lines(alternative_dialogues, 6)
    else:
      lines(alternative_dialogues, 7)


def alternate_stories_5():
    if save[1] == 2:
      lines(alternative_dialogues, 8)
    else:
      lines(alternative_dialogues, 9)


def alternate_stories_6():
    if "infected" in item:
      lines(alternative_dialogues, 10)
    else:
        pass


def alternate_stories_7():
    if "key" in item:
      lines(alternative_dialogues, 11)
    else:
      lines(alternative_dialogues, 12)
      items("shoot")


def alternate_stories_8():
    if "flint and matches" in item or "shoot" in item:
      lines(alternative_dialogues, 13)
      if "infected" in item:
        lines(alternative_dialogues, 14)
        if "map" in item:
          lines(alternative_dialogues, 15)
          items('end')
          lines(alternative_dialogues, 16)
        else:
          lines(alternative_dialogues, 17)
          items('end')
          lines(alternative_dialogues, 18)
      else:
        lines(alternative_dialogues, 19)
        items('end')
        lines(alternative_dialogues, 20)
    else:
      lines(alternative_dialogues, 21)
      if "infected" in item:
        lines(alternative_dialogues, 22)
        items('end')
        lines(alternative_dialogues, 23)
            
      else:
        lines(alternative_dialogues, 24)
        items('end')
        lines(alternative_dialogues, 25)

