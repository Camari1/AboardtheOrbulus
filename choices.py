import colorama
from functions import*
from colorama import Fore, Style
from dialogues_lines import dialogue, choices_dialogue, alternate_storylines

colorama.init(autoreset=True)


# These are all the functions used to decide the choices for the players. The choices are ordered from end to the
# beginning of the story(that's why the choice order is increased rather than decreased). So the end of the code is
# the first players choice, and everything else goes in order. However, the main story (AboardtheOrbulus.py) is
# ordered from beginning to end.
def choice8():
    player_choose8 = input("What will you do?(Type a number)")

    while player_choose8 in "!@#$%^&*()_+-=?/\|,.><:;[]{}~`" or player_choose8 == "" or player_choose8.isalpha() or \
            int(player_choose8) > 2 or int(player_choose8) <= 0:
        player_choose8 = input("What will you do?\n*Please type a number, or a number listed above* ")
    else:
        if int(player_choose8) == 1:
            print("\nCREE:\nCome on, let's go!!!!\n")
            next()

            print("\n\x1B[3mThe group runs to the left at full speed. Crimson bolts still streak from behind them.\n")
            next()
  
            print(
                "\nSAM:\n\x1B[3mI have scanned ahead of us and have found that the shopping center is ahead of us. If "
                "you split up and hid we should be able to lose our pursuer.\n")
            next()

            print("\nCREE:\nAlright let's go!!\n")
            next()

            print(
                "\n\x1B[3mThe group continues down the hall running away from the infested mechanical menace. The "
                "team finally breaks into the shopping district.\n")
            next()

            print("\nCREE:\nSplit up and hide in different stores.\n")
            next()

            print(
                "\n\x1B[3mThe group scrambles into different directions with Sam following you. You picked one of the "
                "convenience stores and burst through the door right as the Magnus made its way into the shopping "
                "district.\n")
            next()

            print("\nCREE:\nDammit! I have to hide.\n")
            next()

            print(
                "\n\x1B[3mYou duck behind a counter right as a red light passes through the window of the store. "
                "Crawling on all fours, you make your way to a better hiding spot. The door opens as the electronic "
                "hum of the former machine guard's arm cannon enters the store first, followed shortly by the Magnus "
                "itself. The Magnus begins to walk around the store knocking over racks and jostling shelves. You "
                "hold your breath praying that the machine leaves soon. A red light shines on the wall in front of "
                "you indicating that the machine is now looking in your direction. Its metallic footsteps get closer "
                "and closer to you until it finally stops right in front of the shelf you are hiding behind. It "
                "sweeps the store one more time before leaving you the store. You let out a sigh of relief. Finally "
                "after what felt like hours you hear the machine leave the shopping district.\n")
            next()

            print("\n\x1B[3mYou access your local communications to contact the others.\n")
            next()

            print("\nCREE:\nEric, Jude are you guys there.\n")
            next()

            print("\n\x1B[3mYou start to hear static coming from communications.\n")

            print("\nERIC:\nI’m here\n")
            next()

            print("\nCREE:\nOk that's good, let's meet up in the center and plan ahead.\n")
            next()

        elif int(player_choose8) == 2:
            print("\nCREE:\nCome on, let's go!!!!\n")
            next()

            print("\n\x1B[3mThe group runs to the right at full speed. Crimson bolts still streak from behind them.\n")
            next()

            print(
                "\nSAM:\n\x1B[3mI have scanned ahead of us and found the bank ahead of us. We may not be able to lose "
                "our pursuer there but we can try.\n")
            next()

            print("\nCREE:\nIt’ll have to do.\n")
            next()

            print(
                "\n\x1B[3mThe group continues down the hall running away from the infested mechanical menace. The "
                "team finally breaks into the bank.\n")
            next()

            print("\nCREE:\nSam, see if there is anywhere for us to hide.\n")
            next()

            print("\nSAM:\n\x1B[3mScanning....\n")
            next()

            print("\n\x1B[3mThe drone’s red lights cover the bank in an attempt to find a hiding spot.\n")
            next()

            print("\nSAM:\n\x1B[3mI regret to report there is nowhere to hi....\n")
            next()

            print(
                "\n\x1B[3mThe drone is cut off by the sound of a blaster firing followed by the drone hitting the "
                "floor. Sam now has a large smoking hole in where its eyre used to be. The group whips around to see "
                "the 7ft tall machine closing in, its red eye gazing at the group. The team slowly backs away. The "
                "Magnus points its cannon at Eric and releases two crimson bolts that leave two holes in Eric’s "
                "chest. With a groan Eric hits the floor and dies.\n")
            next()

            print("\nJUDE:\nN-no Eric no. Oh god no.\n")
            next()

            print("\n\x1B[3mJude’s eyes are widened with fear.\n")
            next()

            print(
                "\n\x1B[3mThe black machine points its cannon at Jude and fires again. Jude’s body hits the ground "
                "kneeling and then falls over with a thud.\n")
            next()

            print(
                "\n\x1B[3mYour eyes widen with fear as you know what's going to come next. You look at the Magnus as "
                "it looks back at you, its crimson eyes gazing dead at you with the intent to kill. You close your "
                "eyes as the last thing you hear is the sound of blaster fire and feel the pain of your body being "
                "pierced.\n")
            next()
            items["death"] = 0

        if 0 < int(player_choose8) <= 2:
            save.append(int(player_choose8))


def choice7():
    player_choose7 = input("What will you do?(Type a number)")

    while player_choose7 in "!@#$%^&*()_+-=?/\|,.><:;[]{}~`" or player_choose7 == "" or player_choose7.isalpha() or \
            int(player_choose7) > 2 or int(player_choose7) <= 0:
        player_choose7 = input("What will you do?\n*Please type a number, or a number listed above* ")
    else:
        if int(player_choose7) == 1:
            print("\nCREE:\nEVERYBODY OPEN FIRE!!!!\n")
            next()

            print(
                "\n\x1B[3mAll at once everyone activates their weapons and opens fire on the machine. Red and green "
                "balls of plasma rapidly fly out and explode against their target, while coils of lighting arc out "
                "from Eric’s coil shotgun. After a while the shooting stops and there is a cloud of smoke where the "
                "Magnus once stood.\n")
            next()

            print("\nERIC:\nDid we get it?\n")
            next()

            print("\nCREE:\nI think so.\n")
            next()

            print("\nJUDE:\nWhat a relief.\n")
            next()

            print(
                "\n\x1B[3mSuddenly the smoke is filled with a red light as the machine turns around to face the "
                "group. Its red eye seething with the urge to kill. The Magnus raises its arm cannon at the group and "
                "proceeds to let crimson red bolts fly.\n")
            next()

            print("\nCREE:\nEVERYONE RUN!!!!!!\n")
            next()
            items["fight"] = 0

        elif int(player_choose7) == 2:
            print("\nCREE:\nEVERYONE RUN!!!!!!\n")
            next()
            items["run"] = 0
        if 0 < int(player_choose7) <= 2:
            save.append(int(player_choose7))


def choice6():
    player_choose6 = input("What will you do?(Type a number)")

    while player_choose6 == "" or player_choose6.isalpha() or int(player_choose6) > 2 or int(player_choose6) <= 0:
        player_choose6 = input("What will you do?\n*Please type a number, or a number listed above* ")
    else:
        if int(player_choose6) == 1:
            print("\n\x1B[3mYou shoot the lock, and the locker opens.  Inside, there is flint and matches.\n")
            next()

            print("\n\x1B[3mYou grab them, and leave the locker, and try looking for more items.\n")
            items["flint and matches"] = 0
            next()

        elif int(player_choose6) == 2:
            print("\n\x1B[3mYou put your gun away. You turn back to the other lockers to find more items.\n")
            next()
        if 0 < int(player_choose6) <= 2:
            save.append(int(player_choose6))


def choice5():
    player_choose5 = input("What will you do?(Type a number)")

    while player_choose5 in "!@#$%^&*()_+-=?/\|,.><:;[]{}~`" or player_choose5 == "" or player_choose5.isalpha() or \
            int(player_choose5) > 2 or int(player_choose5) <= 0:
        player_choose5 = input("What will you do?\n*Please type a number, or a number listed above* ")

    else:
        if int(player_choose5) == 1:
            print("\nCREE:\nto the left.\n")
            next()

            print("\n\x1B[3mAs the group exits a tram, you guys go down a stairway that leads to a room. \n")
            next()

            print("\n\x1B[3mIn the room, there are multiple vents that lead to different areas on the ship.\n")
            next()

            print("\n\x1B[3mOn the wall, there is a map showing where the ventilation leads to.\n")
            next()

            print("\nCREE:\nJude, take the map. This can help us with directions.\n")
            items["map"] = 0
            next()

            print("\n\x1B[3mYou look at the map, then you guys go back to examine the other doors.\n")
            next()

            print("\nCREE:\nLet's go to the Hangar Tram next.\n")
            next()

            print(
                "\n\x1B[3mYou and your crew approach the door, and you try pushing the door handle down, but the door "
                "is locked.\n")
            next()

            print("\n\x1B[3mYou guys go back and go to the Main Hall Tram.\n")
            next()
        elif int(player_choose5) == 2:
            pass
    if 0 < int(player_choose5) <= 2:
        save.append(int(player_choose5))


def choice4():
    player_choose4 = input("What will you do?(Type a number)")

    while player_choose4 in "!@#$%^&*()_+-=?/\|,.><:;[]{}~`" or player_choose4 == "" or player_choose4.isalpha() or \
            int(player_choose4) > 2 or int(player_choose4) <= 0:
        player_choose4 = input("What will you do?\n*Please type a number, or a number listed above* ")

    else:
        if int(player_choose4) == 1:
            print(
                "\n\x1B[3mThe Group heads down the dark hallway to the left. As they approach the split in the "
                "hallway they can see two signs,”Maintenance Trans Station” and “Break Room”.\n")
            next()

            print(
                "\nERIC:\nWe probably don’t need to go into the break room. If anything, this maintenance tram "
                "station should help us with our objective.\n")
            next()

            print("\nCREE:\nAgreed.\n")
            next()

            print("\n\x1B[3mThe group heads to the left towards the tram station.\n")
            next()

            print("\nJUDE:\nWoah! This place is huge.\n")
            next()

            print(
                "\n\x1B[3mIn front of you is a tram station. Above the doors are four different signs. Main Floor "
                "Tram, Power Sector Tram, Ventilation Tram, Hangar Tram.\n")
            next()

            print("\nJUDE:\nI Think we should head to the power sector.\n")
            next()

            print("\nCREE:\nWe could.\n")
            next()

            print("\nERIC:\nBut we should head to the main floor and get more information.\n")
            next()

            print(
                "\nSAM:\nI suggest that we should head to the security sector and gain more information then make a "
                "decision.\n")

        elif int(player_choose4) == 2:
            print(
                "\n\x1B[3mThe group heads down the dark hallway until they get to the room at the end of it. Cree "
                "opens the door and there is a giant terminal and two empty chairs in the room.\n")
            next()

            print("\nCREE:\nSam, can you gather data from that main terminal?\n")
            next()

            print("\nSAM:\n\x1B[3mI can.\n")
            next()

            print(
                "\n\x1B[3mThe grey drone floats over to the console. It begins interfacing with the "
                "terminal.\n")
            next()

            print("\nSAM:\n\x1B[3mData download complete.\n")
            next()

            print("\nCREE:\nGreat, what can you tell us?\n")
            next()

            print(
                "\nSAM:\n\x1B[3mI have determined that is the maintenance sector. However, I do not have data on the "
                "rest of the ship and its condition. The only way to obtain this data is to access it from the "
                "security sector.\n")
            next()

            print("\nCREE:\nI see.\n")
            next()

            print("\nJUDE:\nSam, do you know where the security sector is?\n")
            next()

            print(
                "\nSAM:\n\x1B[3mI did not find any data on the location of the security sector, however, there is a "
                "tram station located to the left of us.\n")

    if 0 < int(player_choose4) <= 2:
        save.append(int(player_choose4))


def choice3():
    player_choose3 = input("What will you do?(Type a number)")

    while player_choose3 in "!@#$%^&*()_+-=?/\|,.><:;[]{}~`" or player_choose3 == "" or player_choose3.isalpha() or \
            int(player_choose3) > 3 or int(player_choose3) <= 0:
        player_choose3 = input("What will you do?\n*Please type a number, or a number listed above* ")

    else:
        if int(player_choose3) == 1:
            print("\nCREE:\nJust stay put, we’ll wait until the beams deactivate.\n")
            next()

            print("\nERIC:\nWe can’t wait here forever, Jude could be in danger.\n")
            print(f"\n\x1B[3m{Style.BRIGHT}*zzz pewww! zzz pewww!*\n")
            next()

            print("\n\x1B[3mEric does not listen to your order and tries to leave.\n")
            next()

            print("\nCREE:\nEric, stay put!\n")
            next()

            print(
                "\n\x1B[3mEric quickly, but cautiously, steps over, under, to right, or the left of the beams. Making "
                "sure that each step he makes won’t be his last.\n")
            next()

            print(
                "\n\x1B[3mYou notice that the beams don’t seem like they will go away anytime soon. So, you slowly "
                "and cautiously step over your first beam.  \n")
            next()

            print(
                "\nERIC:\nTo be safe, don’t touch any of the light rays, you never know which ones may be the "
                "teleportation beams.\n")
            next()

            print(
                "\n\x1B[3mEric stops suddenly, and you are behind him. In front of him, there are 5 beams: one coming "
                "straight down from the ceiling, one coming from the left diagonally, one coming from the right "
                "diagonally, and two horizontal beams parallel to each other.\n")
            next()

            print(
                "\nERIC:\nThere are too many beams blocking the doorway. And I don’t know which beam is light and "
                "which beam teleports you.\n")
            next()

            print(
                "\nCREE:\nJust try to get around them. See if you can see if some of the beams are coming from a "
                "hole.\n")
            print("\n\x1B[3m*ZZZ PEWWW! ZZZ PEWWW! ZZZ PEWWW!*\n")
            next()

            print(
                "\nERIC:\nOK! Two beams are just light. The one from the ceiling and I think the one that’s coming "
                "from the right diagonally. I can try to leap in between the two horizontal beams on the right "
                "side.\n")
            next()

            print(
                "\n\x1B[3mEric pauses and examines the horizontal beams to make sure he leaps at a correct angle. He "
                "leaps halfway through. His body starts to shine, and with the blink of an eye, "
                "his body disappears.\n")
            next()

            print("\nCREE:\nERIC!\n")
            next()

            print(
                "\n\x1B[3mYou follow the same path that Eric made, determined to make sure you leap at a perfect "
                "angle. You leap.\n")
            next()

            print(f"\n\x1B[3m{Style.BRIGHT}*ZZZ PEWWWW! ZZZ PEWWW!\n")
            next()

            print(
                "\n\x1B[3mYou see the doorway getting closer to your sight, then the doorway starts to become blurry, "
                "and everything starts to shine bright. You start to see something different: a dark room with "
                "pipelines everywhere. You fall to the ground.\n")
            next()

            print("\nERIC:\nWe have to go back, Jude is still back there.\n")
            next()

            print("\nCREE:\nI know we are going to find Jude. But first, where are we?\n")
            next()

            print(
                "\nERIC:\nI don’t know. It looked around and it seemed to just be a room of pipes. But I did see an "
                "entrance, we are not trapped here.\n")
            next()

            print("\nCREE:\nGreat! Let’s go back.\n")
            next()

            print(
                "\n\x1B[3mEric shows you the exit door, and you guys are in another empty hallway, and at the end, "
                "there are split directions: left and right.\n")
            next()

            print("\nERIC:\nWhere do we go?\n")
            next()

            print("\nCREE:\nLet’s just go to the end of the hallway and go left.\n")
            next()

            print(
                "\n\x1B[3mBoth of you go to the end of the hallway and turn left. Everything looks similar: empty "
                "hallways leading to many rooms.\n")
            next()

            print(
                "\nERIC:\nWe’re never going to find her. And I don’t even hear the gunshots anymore. We could be "
                "further than before.\n")
            next()

            print("\nCREE:\nDon’t be doubtful. We have to keep our heads high.\n")
            next()

            print(
                "\n\x1B[3mYou guys make it to the end of another hallway and turn left. You guys continue down the "
                "hallway.\n")
            next()

            print("\nCREE:\nLook, something useful.\n")
            next()

            print("\n\x1B[3mA doorway reads “Security Room”.\n")
            next()

            print("\nCREE:\nThere might be surveillance cameras to see where Jude could be.\n")
            next()

            print(
                "\n\x1B[3mYou enter the room, and Eric follows behind you. The room is covered in green muscle "
                "tissue-like vines.\n")
            next()

            print("\nERIC:\nWhat is the substance all over the ship?\n")
            next()

            print("\nCREE:\nWhatever it is, it seemed to have wiped everything off of it.\n")
            next()

            print("\nCREE:\nAHA! A surveillance monitor. Help me turn it on.\n")
            next()

            print("\n\x1B[3mThe two of you both push buttons to try to turn it on.\n")
            next()

            print("\nERIC:\nThese controls are different from the ones on the Starphaser.\n")
            next()

            print("\nCREE:\nIt might just be the power. The monitor is not turning on at all.\n")
            next()

            print("\nERIC:\nHey, but there is something in here. Look.\n")
            next()

            print(
                "\n\x1B[3mEric points to an ancient and rotten skeleton underneath the table of controls. Eric "
                "goes up to the skeleton’s hollow and dark eyes and examines the body.\n")
            next()

            print("\nERIC:\nOne of the skeleton's hands is clenched tight.\n")
            next()

            print("\nCREE:\nOpen it, there might be something in it.\n")
            next()

            print(
                "\n\x1B[3mEric cautiously lifts the arm of the skeleton, and the green pus-like, muscle tissue-like "
                "thick vines attach to it. Eric continues to lift the arm, trying to avoid the disgusting substance "
                "attached to it. He breaks off the arm.\n")
            next()

            print("\n\x1B[3mEric opens the delicate fingers, and inside the non-existent palm of its hand is a key.\n")
            next()

            print("\nCREE:\nA key? We’ll bring it with us.\n")
            next()

            print("\nEric takes the key out of its hands and gives it to you.\n")
            items['key'] = 0
            next()

            print(
                "\n\x1B[3mSuddenly, soft but gradually loud noises start coming from the hallway. You pull out your "
                "weapon.\n")
            next()


            print("\nALBERT and SAM:\n\x1B[3m*beep boop*\n")
            next()

            print(
                "\nCREE:\nOK! It’s just you two. Wait, where did you guys come from? Show us the direction to the "
                "beam room.\n")
            next()

            print(
                "\n\x1B[3mALBERT and SAM leave the room and go through the hallway. They make a LEFT into another "
                "hallway, then they make a RIGHT to another hallway.\n")
            print("\x1B[3m*zzz pewww!*\n")
            next()

            print("\nERIC:\nI can hear the Coil Shotgun again.\n")
            next()

            print("\n\x1B[3mNext, they make another RIGHT.\n")
            print(f"\x1B[3m{Style.BRIGHT}*zzz pewww! zzz pewww!*\n")
            next()

            print("\n\x1B[3mThen, they make a LEFT, and finally, they make a RIGHT.\n")
            next()

            print("\nSAM:\n\x1B[3m*beep boop*\nThis is where we started…\n")
            next()

            print(
                "\n\x1B[3mEveryone exits out of the hallway that was on the right of the teleportation beam room. "
                "Then, everyone stands quiet, listening closely, trying to hear the sound of the Coil Shotgun…\n")
            print(f"\x1B[3m{Style.BRIGHT}*Zzz Pewww! Zzz Pewww!*\n")
            next()

            print("\nCREE:\nCome on, she went down the hallway.\n")
            next()

            print("\n\x1B[3mEveryone rushes to the end of the hallway.\n")
            print(f"\x1B[3m{Style.BRIGHT}*ZZZ PEWWW! ZZZ PEWWW! ZZZ PEWWW!*\n")
            next()

            print("\nCREE:\nThe sound is coming from the right.\n")
            next()

            print(
                "\n\x1B[3mEveryone dashes to the right. Then, everyone makes another right halfway through the "
                "hallway. At the end of that hallway, a glimpse of Jude is seen, and she is shooting at something.\n")
            next()

            print("\nCREE & ERIC:\nJUDE!\n")
            next()

            print(
                "\n\x1B[3mYou and Eric catch a glimpse of many somewhat disturbingly human entities. Their "
                "permanently dry and decayed bodies leap out of a corner, with a horrific expression. Their elongated "
                "and dry mouths stretch nearly to their chests; their mouths stretch nearly the same length as their "
                "heads, and their eyes bulge out of their eye sockets, like a skeleton with eyes, but without any "
                "eyelids. Their ghostly pale and brittle flesh has muscle tissue-like vines growing and weaving "
                "through their skins, like long strings of stitches hanging off their bodies.\n")
            next()

            print("\nJUDE:\nI need backup!\n")
            next()

            print("\n\x1B[3mYou and Eric get right into battle; instinctively running towards Jude to help.\n")

        elif int(player_choose3) == 2:
            print(
                "\nCREE:\nKeep moving, just avoid every light ray that you see. Any one of them could be a "
                "teleportation beam.\n")
            next()

            print(
                "\n\x1B[3mYou and Eric quickly, but cautiously, step over, under, to the right or the left of the "
                "beams, making sure that each step you both make won’t be your last.\n")
            print("\x1B[3m*Zzz Pewww! Zzz Pewww!*\n")
            next()

            print(
                "\n\x1B[3mEric stops suddenly, and you are behind him. In front of Eric, there are 5 beams: one "
                "coming straight down from the ceiling, one coming from the left diagonally, one coming from the "
                "right diagonally, and two horizontal beams parallel to each other.\n")
            next()

            print("\nCREE:\nCan you tell which beam is a light beam, and which one teleports you?\n")
            next()

            print(
                "\nERIC:\nLet me see… I see that the beam on the ceiling is just light, and I think the diagonal beam "
                "on the left is just light too. I can try to leap in between the two horizontal beams on the left "
                "side. \n")
            print(f"\x1B[3m{Style.BRIGHT}*zzz pewww! zzz pewww!*\n")
            next()

            print("\nERIC:\nOkay! I’m going.\n")
            next()

            print(
                "\nEric pauses and examines the horizontal beams to make sure he leaps at a correct angle. He leaps "
                "halfway through. His body starts to shine, and with the blink of an eye, his body disappears.\n")
            next()

            print("\nCREE:\nERIC!\n")
            next()

            print(
                "\n\x1B[3mYou notice that Eric’s choice was the wrong decision. So, you do not use Eric’s method. You "
                "decide to go on the left side, but you go underneath the beam closest to the ground.\n")
            next()

            print("\nCREE:\nOk... here goes…\n")
            next()

            print(
                "\n\x1B[3mWith the many beams surrounding you, you take yourself to the ground. Like limboing, "
                "you anxiously make your way lower and lower to the ground until you are flat on the ground.\n")
            next()

            print("\nCREE:\nOk…\n")
            next()

            print(
                "\n\x1B[3mYou slowly breathe, each breath that you exhale becomes heavier and unsteady. As if you are "
                "holding your breath underwater. The only thing that you move is your arms. You lift your arms "
                "slightly off the ground, but keep your hands laid on the ground’s surface.\n")
            print(f"\x1B[3m{Style.BRIGHT}*ZZZ PEWWW!*\n")
            next()

            print(
                "\n\x1B[3mYou take your arms and you push your arms in the direction opposite the direction you are "
                "facing. You slowly, but sure make your way underneath the beam. The beam is slightly above your "
                "body, and you try to make sure your body is firmly flat on the ground. You continue to push yourself "
                "under the beam until finally, you make your way through. You get up quickly and run to the exit "
                "door.\n")
            print(f"\x1B[3m{Style.BRIGHT}*zzz pewww! zzz pewww!*\n")
            next()

            print("\nCREE:\nI have to find Eric! Now two of my troops are gone!\n")
            next()

            print("\nCREE:\nAlbert and SAM, go around the shuttle and look for Eric. I’ll look for Jude.\n")
            next()

            print(
                "\n\x1B[3mThe two of them are both in the same entrance hallway, and they go to the end of the "
                "hallway.\n")
            print("\x1B[3m*ZZZ PEWWW! ZZZ PEWWW!\n")
            next()

            print("\nCREE:\nThe Coil Shotgun sound is coming from the right side.\n")
            next()

            print("\n\x1B[3mThe robots go to the hallway on the left and You go to the hallway on the right.\n")
            print(f"\x1B[3m{Style.BRIGHT}*ZZZ PEWWW! ZZZ PEWWW! ZZZ PEWWW!*\n")
            next()

            print("\nCREE:\nThe shots are coming from the right. I must be close, the shots are becoming louder.\n")
            next()

            print(
                "\n\x1B[3mYou enter an adjacent hallway on the right, and there you see Jude shooting at something!\n")
            print(f"\x1B[3m{Style.BRIGHT}*ZZZ PEWWWWW!*\n")
            next()

            print("\nCREE:\nJUDE!\n")
            next()

            print(
                "\n\x1B[3mYou run towards Jude, approaching to make sure she is safe, but something unprecedented "
                "happens…\n")
            next()

            print(
                "\n\x1B[3mYou are halfway through the hallway, and something you thought was human launches at you. \n")
            next()

            print(
                "\n\x1B[3mIts permanently dry and decayed body leaps out of a corner, with a horrific expression. Its "
                "elongated and dry mouth stretches nearly to its chest; its mouth stretches nearly the same length as "
                "its head, and its eyes bulge out of its eye sockets, like a skeleton with eyes, but without any "
                "eyelids. Its ghostly pale and brittle flesh has muscle tissue-like vines growing and weaving through "
                "its skin, like long strings of attached stitches hanging off its body.\n")
            next()

            print(
                "\n\x1B[3mYou instinctively reach to grab your gun from your weapon belt, but the creature firmly "
                "locks you in its cold and slimy hands and pushes you onto the ground.\n")
            next()

            print("\nCREE:\nJUDE! I need backup!\n")
            next()

            print("\nJUDE:\nI can’t stop now!\n")
            print(f"\x1B[3m{Style.BRIGHT}*ZZZ PEWWW! ZZZ PEWWW!*\n")
            next()

            print(
                "\n\x1B[3mAs you lay on the ground with the monster screeching and aggressively attacking your body, "
                "trying to devour your face, you slightly catch a glimpse of the many other hordes of this creature "
                "in front of Jude.\n")
            next()

            print(
                "\n\x1B[3mThen, in front of you, an incision opens from the torso of the monster, and a long wet vine "
                "comes out and pierces you in your arm.\n")
            next()
            items["infected"] = 0

            print(
                "\n\x1B[3mAs you continue to struggle to get this creature off of you with one hand, with your other "
                "hand you finally manage to obtain your gun.\n")
            next()

            print("\n\x1B[3mYou pull your gun up towards the creature and it knocks it out of your hand.\n")
            next()

            print(
                "\n\x1B[3mThe monster continues to keep you stuck on the floor, like a fly stuck in a flytrap. You "
                "continue to fight, and you still have a pocket knife with you, so you stab the creature on its "
                "torso, and it screeches, retreating away from you.\n")
            next()

            print("\nQuickly, it dashes towards Jude…\n")
            next()

            print("\nCREE:\nJude, one of them is behind you!\n")
            next()

            print("\nYou get up from the ground and run towards the creature.\n")
            print(f"\x1B[3m{Style.BRIGHT}*BANG! BANG!*\n")
            next()

            print("\n\x1B[3mThere’s a long energy blast ray that comes from behind Jude, and also from behind you.\n")
            next()

            print(
                "\n\x1B[3mEric stands behind everyone and everything, His arms extended outwards as a Plasma Ray Gun "
                "extended out from it.\n")
            next()

            print("\nERIC:\nCome on, we have to help Jude!\n")
            print("\x1B[3m*ZZz peww!*\n")
            next()

            print("\nJUDE:I’m out of ammo! And these hordes are everywhere!\n")
            next()

            print(
                "\nYou go to the spot where the creature knocked your gun out of your hand. Your gun is held in your "
                "hands and you help Eric fend off the horde.\n")
            next()

        elif int(player_choose3) == 3:
            print("\nCREE:\nALBERT, scan to detect light beams.\n")
            next()

            print("\nALBERT:\n\x1B[3mSorry… that is not a program that I possess.\n")
            next()

            print("\nERIC:\nWhy is he with us, again?\n")
            print(f"\x1B[3m{Style.BRIGHT}*zzz pewww! zzz pewww!*\n")
            next()

            print("\nALBERT:\n\x1B[3mMAR-356… activate teleportation beam scanner.\n")
            next()

            print("\nMAR-356(SAM):\n\x1B[3mSearching for teleportation beams…\n")
            next()

            print(
                "\nSAM:\n\x1B[3mLocated teleportation beams… There are 10 teleportation beams. Should I deactivate "
                "the beams?\n")
            next()

            print("\n\x1B[3m*zzz pewww! zzz pewww!*\n")
            print("ERIC:\nYes!\n")
            next()

            print("\nSAM:\n\x1B[3mDeactivating beams in 3…2…1…\n")
            next()

            print("\n\x1B[3mAll the teleportation beams in the room deactivate, and you guys run outside the room.\n")
            print(f"\x1B[3m{Style.BRIGHT}*ZZZ PEWWW! ZZZ PEWWW! ZZZ PEWWW!*\n")
            next()

            print("\nCREE:\nCome on, she went down the hallway.\n")
            next()

            print("\n\x1B[3mEveryone rushes to the end of the hallway.\n")
            print(f"\x1B[3m{Style.BRIGHT}*ZZZ PEWWW! ZZZ PEWWW! ZZZ PEWWW!*\n")
            next()

            print("\nCREE:\nThe sound is coming from the right.\n")
            next()

            print(
                "\n\x1B[3mEveryone dashes to the right. Then, everyone makes another right halfway through the "
                "hallway. At the end of that hallway, a glimpse of Jude is seen, and she is shooting at something.\n")
            next()

            print(
                "\n\x1B[3mYou and Eric catch a glimpse of many somewhat disturbingly human entities. Their "
                "permanently dry and decayed bodies leap out of a corner, with a horrific expression. Their elongated "
                "and dry mouths stretch nearly to their chests; their mouths stretch nearly the same length as their "
                "heads, and their eyes bulge out of their eye sockets, like a skeleton with eyes, but without any "
                "eyelids. Their ghostly pale and brittle flesh has muscle tissue-like vines growing and weaving "
                "through their skins, like long strings of stitches hanging off their bodies.\n")
            next()

            print("\nJUDE:\nI need backup!\n")
            next()

            print("\n\x1B[3mYou and Eric get right into battle, instinctively running towards Jude to help.\n")
            next()

            print("\n\x1B[3mYou and Eric help Jude fend off the creatures.\n")
            next()

            print("\n\x1B[3mSAM switches to combat mode and starts shooting at the horde.\n")
            print(f"\x1B[3m{Style.BRIGHT}*ZZz peww!*\n")
            next()

            print("\nJUDE:\nI’m out of ammo!\n")
            next()
    print("\n\x1B[3mOne by one they turn across a corner running and TOWERING over each other, like an ocean wave.\n")
    print(f"\x1B[3m{Style.BRIGHT}*DDPHEWW!\nBANG!\nDDPHEWW!\nBANG!*\n")
    next()

    print(
        "\n\x1B[3mYou, Eric, and SAM continue to shoot at the strange entities until you guys start to realize that "
        "they are not stopping.\n")
    next()

    print("\nCREE:\nWe just have to run!\n")
    next()

    print(
        "\n\x1B[3mYou lower your gun and you run back, everyone else follows you.The creatures start to pile up even "
        "higher, knocking each other out the way, shaking the hallways chasing after you guys. As you guys run, "
        "you continue to aim and shoot.\n")
    next()

    print(
        "\nYou guys make a left into another hallway, and then you guys turn left into a long corridor. At the end of "
        "this corridor, there is a room with four doors to choose from.\n")
    if 0 < int(player_choose3) <= 3:
        save.append(int(player_choose3))


def choice2():
    player_choose2 = input("What will you do?(Type a number) ")

    while player_choose2 in "!@#$%^&*()_+-=?/\|,.><:;[]{}~`" or player_choose2 == "" or player_choose2.isalpha() or \
            int(player_choose2) > 2 or int(player_choose2) < 0:
        player_choose2 = input("What will you do?\n*Please type a number, or a number listed above* ")
    else:
        if int(player_choose2) == 1:
            print("\nCree:\nYes, I’ll activate the ship’s EED.\n")
            next()

            print(
                "\n\x1B[3mOn the outside of the ship four spherical drones are ejected from the side of the ship. "
                "They simultaneously open up and began scanning the ship.\n")
            next()

            print(
                "\n\x1B[3mA cyber, rectangular monitor extends directly from the ceiling and displays an overview of "
                "the Orbulus outside.\n")
            next()

            print("\nERIC:\nWhat’s on it?\n")
            next()

            print("\nCREE:\nI have no idea, I’ve never seen anything like it before…\n")
            next()

            print("\nERIC:\nALBERT(EED-38), zoom in more on the ship.\n")
            next()

            print("\nCREE:\n Hey, only " + "\x1B[3mI" + " can activate it-\n")

            print("\nALBERT:" + "\n\x1B[3mActivating…\n" + "Zoom In…\n")
            next()

            print(
                "\n\x1B[3mThe shuttle has shield-like windows on each level: the basement level, the middle level, "
                "and the top level. Through the middle compartment, you notice something looming through the opaque "
                "windows - something larger than mankind itself. The shadow of it stands idle as everything around "
                "the window is surrounded by the darkness of space - standing as if it senses what’s looking at it…\n")
            next()

            print("\nCREE:" + "\n\x1B[3m*gasp*\n" + "ALBERT, zoom out.\n")
            next()

            print("\nJUDE:\nWhere do you think it came from?\n")
            next()

            print("\nCREE:\nI have no idea, but we have to find out… Andromeda how close is the ship?\n")
            next()

        elif int(player_choose2) == 2:
            print("\nCree:\nNo, there’s no point. Let’s just focus on our mission.\n")
            next()

            print("\nChristopher:\nBut what if they have directions to the planet we’re looking for?\n")
            next()

            print("\nCREE:\nI said no, that’s my final decision, and that’s your order.\n")
            next()

            print(
                "\nCREE:\nWe have no information about this new shuttle, and investigating that ship could put us in "
                "great jeopardy.\n")
            next()

            print(
                "\n\x1B[3mYou think about the decision for a bit longer. You recognize the danger of the situation, "
                "but need to find more answers for where the new planet is located. Your curiosity is taking control "
                "of you, you have to know what the space shuttle is and where it came from.\n")
            next()

            print("\nCREE:\nGosh…\n")
            next()

            print("\nCREE:\nI can’t believe I’m saying this…\n")
            next()

            print("\nCREE:\nAndromeda, how far is the shuttle from us?\n")
            next()

    print("\n\x1B[3mThere is a moment of silence on the Starphaser as Andromeda takes a moment to calculate\n")
    next()

    print("\nAndromeda:\n\x1B[3mThe Orbulus is…\n34,356 miles away.\n")
    next()
    print(
        "\nCREE:\nOk, the ship is still pretty close. We could see if the people on the shuttle could have any hints "
        "for the new planet’s location.\n")

    if 0 < int(player_choose2) <= 2:
        save.append(int(player_choose2))


def choice():
    player_choose1 = input("What will you do?\n*Please type a number, or a number listed above* ")

    while player_choose1 in "!@#$%^&*()_+-=?/\|,.><:;[]{}~`" or player_choose1 == "" or player_choose1.isalpha() or \
            int(player_choose1) > 2 or int(player_choose1) <= 0:
        player_choose1 = input("What will you do?\n*Please type a number, or a number listed above* ")

    if player_choose1 == "1":
       lines(choices_dialogue, 15)
       save_list(player_choose1)

    elif player_choose1 == "2":
        lines(choices_dialogue, 16)
        save_list(player_choose1)
        choice2()
