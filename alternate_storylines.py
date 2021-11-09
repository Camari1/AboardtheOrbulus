import colorama
from colorama import Fore, Style
from functions import *
from choices import choice3

colorama.init(autoreset=True)


# These are the alternate storylines for the progression of the story. The previous choices that a player makes
# determines what storyline will occur. The progression of the alternate storylines are ordered from beginning to
# end, in which they occur. It also depends on the previous choices you have made to determine, if the certain
# storylines will run.
def alternate_stories_1():
    if save[0] == 1:
        print("\nCree:\nI don’t understand, my weapons are gone! Who stole them!\n")
        next()

        print(
            "\n\x1B[3mLooking through the glass casing you see a damaged and tampered wall. You see burnt outlines of "
            "a "
            "patched hole.\n")
        next()

        print("\nCree:\nThe space pirates took them! I guess I’ll take one of the normal weapons in the front.\n")
        next()

        print("\n\x1B[3mYou go back to the weaponry room to pick up a plasma repeater sidearm on the wall.\n")

    elif save[0] == 2:
        print(
            "\n\x1B[3mYour gun catches your image through its reflective surface. The gun was designed for extra "
            "gripping properties. The weapon is abstract in design, having a smooth,  obsidian-black customized "
            "casing surrounding it. You grab your weapon then leave the secret bunker.\n")


def alternate_stories_2():
    if save[1] == 1:
        print(
            "\nCREE:\nI don’t think that’s a good idea. We should stay together, we don’t know what we may be up "
            "against.\n")
        next()

        print(
            "\nJUDE:\nThe place is empty, and who would want to be in a place as disgusting as this. Plus, "
            "I have a weapon to protect me. If something sneaks out from behind me, I’ll shoot it straight in the "
            "head.\n")
        next()

        print("\nCREE:\nListen to my warning. We need to stay together, we cannot separate.\n")
        next()

        print(
            "\nCREE:\nWhen we were in the Starphaser, I saw something bigger than us peering through the window. I "
            "don’t know if it’s still here, but I don’t want one of my soldiers in danger if it is.\n")
        next()

        print("\nJUDE:\n…\n")
        next()

        print("\nJUDE:\nOK, I’ll stay at a close distance.\n")
        next()

        print(
            "\n\x1B[3mEric is looking at a door that has been forcibly pulled off its hinges. Eric enters through and "
            "finds a room somewhat lit by the thin rays of light coming from holes in the ceiling. Dust particles "
            "enter through the rays of light and vanish, particle by particle. One of the rays of light unveils the "
            "layer of darkness and captures the attention of Eric who spots something reflecting the light.\n")
        next()

        print("\nCREE:\nWhat do you see?\n")
        next()

        print("\nERIC:\nI don’t know yet.\n")
        next()

        print(
            "\n\x1B[3mEric picks up the item, and it is revealed that it is a name tag? A name tag of someone named "
            "‘Joseph William’.\n")
        next()

        print("\nERIC:\nIt’s a name tag.\n")
        next()

        print("\nJUDE:\nAs in a human name tag?\n")
        next()

        print("\nERIC:\nYes. Somebody was here.\n")
        next()

        print("\nCREE:\nYou think they still could be here?\n")
        next()

        print(
            "\nERIC:\nI think they still could be here. The name tag is still in good condition by the looks of it.\n")
        next()

        print("\nCREE:\nMaybe we are not alone on the ship after all.\n")
        next()

        print(
            "\n\x1B[3mYou leave the room and everyone follows you. You guys make your way to the end of the hallway "
            "and "
            "turn left into another hallway. You guys then see a corridor on the left and walk in that direction. At "
            "the "
            "end of the corridor is a room with four doors.\n")

    elif save[1] == 2:
        print(
            "\n\x1B[3mJude leaves the group and goes through the dark hallway. Eric follows behind Jude. You are "
            "somewhat hesitant to enter the doorway but enter anyway.\n")
        next()

        print(
            "\n\x1B[3mEric is looking at a door that has been forcibly pulled off its hinges. Eric enters through and "
            "finds a room somewhat lit by the thin rays of light coming from holes in the ceiling. Dust particles "
            "enter through the rays of light and vanish, particle by particle. One of the rays of light unveils the "
            "layer of darkness and captures the attention of Eric who spots something reflecting the light.\n")
        next()

        print("\nCREE:\nWhat are you looking at?\n")
        next()

        print("\nERIC:\nI don’t know yet.\n")
        next()

        print(
            "\n\x1B[3mEric picks up the item, and it is revealed that it is a name tag? A name tag of someone named "
            "Joseph William.\n")
        next()

        print("\nERIC:\nIt’s a name tag.\n")
        next()

        print("\nCREE:\nAs in a human name tag?\n")
        next()

        print("\nERIC:\nYes. Somebody was here.\n")
        next()

        print("\nCREE:\nYou think they still could be here?\n")
        print("\x1B[3m*ZZZ PEWWW!*\nUnexpectedly, the sound of electric coil beams goes off in the distance.\n")
        next()

        print("\nCREE:\nWhat was that?\n")
        next()

        print("\nERIC:\nJude, where are you?! We’re coming!\n")
        next()

        print("\nCREE:\nJude, tell us your location!\n")
        next()

        print("\nERIC:\nSam track Jude!\n")
        next()

        print("\nSAM\n\x1B[3mSorry… that is not a program that I possess.\n")
        next()

        print("\nERIC:\nWhy do we have this thing-\n")
        print("CREE:\nJude!\n")
        next()

        print(
            "\n\x1B[3mThe both of you run towards the sound of it. A sound of ringing begins to go off, "
            "like the whistling of a tea kettle.\n")
        next()

        print(f"\n\x1B[3m{Style.BRIGHT}*BeeEEE!! BeeEEE!!*\n")
        print("\x1B[3mYou both stop near the entrance of the room, to figure out where the noise is coming from.\n")
        next()

        print("\nERIC:\nI don’t understand! Where is the noise coming from?\n")
        next()

        print("\n\x1B[3mThe noise stops.\n")
        print("\x1B[3m*THUMmmm!!*\n")
        next()

        print("\nCREE:\nAre there more light rays than there used to be?...\n")
        next()

        print("\nERIC:\nWhat? How?\n")
        next()

        print(
            "\nCREE:\nI don’t know, but something is telling me that this ship is more active than I thought it was.\n")
        next()

        print(
            f"\n\x1B[3m{Style.BRIGHT}*ZZZ PEWWW!*" + "\nThe sound of electric coil beams goes off again in the "
                                                     "distance. Eric takes the name tag out of his pockets and tosses"
                                                     " it to one of the light rays.\n")
        next()

        print("\nERIC:\nWhere did it go?\n")
        next()

        print("\nCREE:\nTeleportation beams. Whatever touches the beams gets transported to a specific location.\n")
        print("Should you...")
        print(f"{Fore.LIGHTRED_EX}1)Wait until beams deactivate.")
        print(f"{Fore.LIGHTRED_EX}2)Escape the room by trying to avoid the beams.")
        print(f"{Fore.LIGHTRED_EX}3)Ask Albert to detect which beams are safe.")
        choice3()


def alternate_stories_3():
    if save[1] == 1:
        print("\nCREE:\nLet’s go to the Power Sector.\n")
        next()

        print("\n\x1B[3mEveryone enters through the doorway.\n")
        next()

        print("\nERIC:\nCaptain, shouldn't we be returning back to the Starphaser?\n")
        next()

        print("\nCREE:\nWe have to change plans. We have to figure out what’s going on here.\n")
        next()

        print("\n\x1B[3mYou pull out the name tag that they found.\n")
        next()

        print(
            "\nCREE:\nClearly, there were people, and perhaps there are people still on this ship. We have to find "
            "out what happened.\n")

    elif save[1] == 2:
        print("\nCREE:\nQuick! Everyone this way!\n")
        next()

        print(
            "\n\x1B[3mEveryone dashes in the Power Sector door. The horde of monsters continues to flow through the "
            "halls like a wave catching up to your movements. Once everyone has made it inside, you close the door "
            "and lock it. The monsters stay lingering behind the door.\n")
        next()

        print("\nERIC:\nWhew… that was something.\n")
        next()

        print("\nJUDE:\nIt was unusual. Cree, what were those things?\n")
        next()

        print(
            "\nCREE:\nI don’t know, but we have to cancel our trip to planet Zeno. There’s way too much here that we "
            "need answers to.\n")
        next()
    print("\nCREE:\nI need to locate a holograph communication pod. I need to contact Christopher. He has to deliver "
        "the energy rods before Ambassador Morgans realizes that we have not completed our mission. But first, "
        "we need power.\n")


def alternate_stories_4():
    if "infected" in items:
        print(
            "\nCREE:Good idea…ALBERT, record this message to Christopher, then go back to the Starphaser to deliver "
            "this message: Hello, Christopher as captain of the ship, I’m leaving you the task to make sure those "
            "energy rods get delivered. Jude, Eric, and I are still searching the Orbulus for new information. This "
            "ship may be abandoned, but we have to-\n")
        next()

        print("\nCREE:\nAhhhh!\n")
        next()

        print(
            "\n\x1B[3mAn increasingly sharp pain begins to form on your forearm. The pain was so intense that it felt "
            "as though acid was running through your veins.\n")
        next()

        print("\nERIC:\nCaptain! Are you alright?\n")
        next()

        print("\n\x1B[3mYou take a deep breath, and the pain slowly decreases.\n")
        next()

        print('\nCREE:\nYes, I’m fine.\n')
        next()

        print("\nCREE:\nWe have to know if there are people here that need to be saved.\n")
        next()
    else:
        print(
            "\nCREE:\nGood idea…ALBERT, record this message to Christopher, then go back to the Starphaser to deliver "
            "this message: Christopher as captain of the Starphaser, I’m leaving you the task to make sure those "
            "energy rods get delivered. Jude, Eric, and I are still searching the Orbulus for new information. To "
            "find out more information about this infestation.\n")
        next()


def alternate_stories_5():
    if save[1] == 2:
        print(
            "\n\x1B[3mEveryone leaves the room, and returns back to the door they entered from. You slightly open the "
            "door, so slight that even the sharpest knife in the world could not produce something so thin.\n")
        next()

        print(
            "\n\x1B[3mThe halls are silent. You open the door a bit more and see that the weird creatures have "
            "disappeared. But where to?\n")
    else:
        print("\nEveryone leaves the room, and returns to the door they entered from.\n")
        next()


def alternate_stories_6():
    if "infected" in items:
        print("\n\x1B[3mYou go to the medic lab, and examine your arm.\n")
        next()

        print("\nCREE:\nWhat is happening?\n")
        next()

        print("\n\x1B[3mYour arm has an open wound, and is not in pain.\n")
        next()

        print("\nCREE:\nI can’t leave my arm like this.\n")
        next()

        print(
            "\n\x1B[3mYou grab an automatic stitching machine, and place your arm underneath it. The machine scans "
            "the wound, then proceeds to execute. The machine goes over your wound and begins piercing under the skin "
            "and through.\n")
        next()

        print("\nCREE:\nWhy can't I feel anything?\n")
        next()

        print(
            "\n\x1B[3mThe wound becomes fully stitched, but there isn’t any pain. You quickly pull your sleeve down, "
            "and go back to look for clues. \n")
        next()
    else:
        pass


def alternate_stories_7():
    if "key" in items:
        print("\n\x1B[3mYou realize that you found a key in the Security Room from before.\n")
        next()

        print("\nCREE:\nI have a key.\n")
        next()

        print("\n\x1B[3mYou take out the key and put it inside the keyhole.\n")
        next()

        print(
            "\n\x1B[3mYou unlock the lock and the box opens! Inside there is a huge gun weapon and a peculiar looking "
            "smoke bomb.. It looks brand new as if it was just invented.\n")
        next()

        print("\n\x1B[3mYou guys grab the weapons and take it with you.\n")
    else:
        print("\nCREE:\nWe don't have a key to open it. We just have to leave it there-\n")
        print("\nERIC:\nEveryone, stand back.\n")
        next()

        print(
            "\n\x1B[3mEric pulls out his weapon and aims at the lock on the box. The blast is loud, "
            "echoing throughout the ship. The box is open.\n")
        next()

        print(
            "\n\x1B[3mInside there is a huge gun weapon and a peculiar looking smoke bomb. It looks brand new as if "
            "it was just invented. You guys grab the weapons and take it with you.\n")
        next()
        items["shoot"] = 0


def alternate_stories_8():
    if "flint and matches" in items or "shoot" in items:
        print("\nSuddenly, you hear loud screeches coming from the stairs you just entered.\n")
        print(f"\x1B[3m{Style.BRIGHT}**RAhhhh Rahhhhh**\n")
        next()

        print(
            "\n\x1B[3mThe creatures are called the 'Svis Drone'. It's a creature with an elongated and dry mouth that "
            "nearly stretches to its chest. Its eyes bulge out of its eye sockets. It has ghostly pale and brittle "
            "flesh and has muscle tissue-like vines growing and weaving through its skin, like long strings of "
            "attached stitches hanging off its body.\n")

        print(
            "\n\x1B[3mThe screeches become more intense, and suddenly 20 Svis Drones come running into the room. You "
            "and your crew pull out your weapons, and start shooting.\n")
        next()

        print("\nCREE:\nEveryone, keep fighting. Try not to let them injure you.\n")
        next()

        print(
            "\n\x1B[3mThe crew is in the middle of the source’s room, fighting against the creatures that continue to "
            "come.\n")
        next()
        if "infected" in items:
            print("\n\x1B[3mEveryone starts to fight the monsters.\n")
            next()

            print("\nCREE:\nGuys I need that Special Gun. I’m going to end this thing once and for all.\n")
            next()

            print("\n\x1B[3mWhile everyone continues to fight, Eric throws the weapon on the ground in a haste.\n")
            next()

            print("\n\x1B[3mYou go to the spot where the weapon is and grab on to it tightly.\n")
            next()

            print("\nCREE:\nAAHHHhh!\n")
            next()

            print("\n\x1B[3mThe increasing pain begins to form again on your arm.\n")
            next()

            print("\nCREE:\nNo, not now!\n")
            next()

            print("\n\x1B[3mYou continue  fighting the horde, but you feel so much pain. You drop the weapon.\n")
            next()

            print(
                "\n\x1B[3mYou check your arm, and suddenly, you see that your veins have become even more green than "
                "before. The same color shade as emeralds.\n")
            next()

            print(
                "\n\x1B[3mEric goes up to one of the vents by climbing the vines on the walls and opens the vent. He "
                "has the special smoke bomb in his hands.\n")
            next()

            print("\n\x1B[3m*ZZZ BSSHHH*\n")
            next()

            print("\n\x1B[3mThe blast comes from you. The weapon and Eric fall to the ground.\n")
            next()

            print("\nJUDE:\nERIC!\n")
            next()

            print(
                "\n\x1B[3mJude goes over to try getting the weapon, but there are too many zombies surrounding her.\n")
            next()

            print(
                "\n\x1B[3mYou make your way to the smoke bomb. And everything starts to be less hostile towards you, "
                "as if they recognize you as their own.\n")
            next()

            print("\n\x1B[3mYou take the weapon, and you leave it with you.\n")
            next()

            print(
                "\n\x1B[3mThe rest of the crew members continue to fight the sporadic horde, and you return back to "
                "normal.\n")
            next()

            print("\nCREE:\nERIC!\n")
            next()

            print("\nCREE:\nHow could I do this?\n")
            next()

            print("\n\x1B[3mYou begin to become tearful as you realize what you have done.\n")
            next()

            print(
                "CREE:\nEveryone, run away from here! Stay away from me! Protect yourself. Find an escape pod and "
                "leave.\n")
            next()

            print("\nJude:But Captain, we can't leave you like this.\n")
            next()

            print("\nCREE:\nJust leave, I’m already infected…\n")
            next()

            print("\n\x1B[3mJude and everyone else leaves as the horde continues to chase them.\n")
            next()

            print(
                "\n\x1B[3mYou and the Molgra are still in the room. You feel as though the source is manipulating "
                "you. Nothing is in your control anymore. You and the Molgra are whole.\n")
            next()

            print(
                "\n\x1B[3mSuddenly, your body is paler than it’s ever been. You notice that the veins are protruding "
                "through your skin, and it starts to peel through your skin. The veins have become vines. The vines "
                "wrap over your body. You have now become a subject of the Molgra.\n")
            next()

            print("\n\x1B[3mYou leave the room and find other hordes over the ship.\n")
            next()
            if "map" in items:
                print(
                    "\n\x1B[3mMeanwhile, Jude holds on to the map to look for the escape pod while a copious amount "
                    "of pale, cold, and slender creatures chase after them.\n")
                next()

                print("\nLily:\nWe can’t go back now. The hordes are too close.\n")
                next()

                print(
                    "\nJUDE:\nWe can’t just leave her like that? Is there any other materials here to help defeat the "
                    "source?\n")
                next()

                print("\nJoseph:\nShe is already infected, there’s no way of saving her.\n")
                next()

                print("\nJUDE:\n…\n")
                next()

                print("\n\x1B[3mThey locate the escape pods and enter it just in time to close the door.\n")
                next()

                print("\n\x1B[3mJoseph presses the eject button, and the pod leaves the ship.\n")
                next()

                print("\n\x1B[3mThey eject out in space, and it is quiet and isolated.\n")
                next()

                print("\n\x1B[3mJude directs the pod to the Starphaser. \n")
                next()

                print(
                    "\n\x1B[3mThe Orbulus continues to ominously drift in space, covered in the substance that took "
                    "away their captain…\n")
                next()

                print(
                    f"{Fore.MAGENTA}Your crew made it out alive, except for Eric. You are infected. Thanks for playing "
                    + f"{Fore.RED}\"Aboard The Orbulus\" " + f"{Fore.MAGENTA}!")
                print(
                    f"{Fore.MAGENTA}Music created by\n " +
                    f"{Fore.RED}\"FesliyanStudios(www.fesliyanstudios.com)\" " + f"{Fore.MAGENTA}\n"
                    f"{Fore.RED}\"Sound Jay(https://www.soundjay.com/crowd-talking-1.html#google_vignette)\" " + f"{Fore.MAGENTA}\n"
                    f"{Fore.RED}\"RobinHood76(https://freesound.org/people/thefilmbakery/downloaded_sounds/)\" " + f"{Fore.MAGENTA}\n"
                    f"{Fore.RED}\"Syna-Max(https://freesound.org/people/Syna-Max/sounds/54984/)\" " + f"{Fore.MAGENTA}\n")
            else:
                print("\n\x1B[3mEveryone runs frantically in different directions searching for the escape pods.\n")
                next()

                print("\nJUDE:\nWhere do we go?\n")
                next()

                print("\nJOSEPH:\nThis ship is huge, I don't remember where the escape pods are.\n")
                next()

                print("\nJACKSON:\nSomebody has to remember!\n")
                next()

                print("\n\x1B[3mThe creatures continue to chase after them as they continue to run.\n")
                next()

                print("\nJUDE: Oh no! We've reached a dead end.\n")
                next()

                print("\nLILY:\nEveryone, turn around and shoot!\n")
                next()

                print(
                    "\n\x1B[3mEveryone turns around a shoots at the multitude of creatures piling on top of each "
                    "other. Everyone becomes surrounded by the creatures as they consume your crew's body. They were "
                    "not able to make it out of the Orbulus.\n")
                next()

                print(
                    "\n\x1B[3mThe Orbulus continues to ominously drift in space, covered in the substance that took "
                    "away a team of heroes…\n")
                next()

                print(
                    f"{Fore.MAGENTA}You made it alive, but you are infected. Your entire crew died. Thanks for playing "
                    + f"{Fore.RED}\"Aboard The Orbulus\" " + f"{Fore.MAGENTA}!")
                print(
                    f"{Fore.MAGENTA}Music created by\n " +
                    f"{Fore.RED}\"FesliyanStudios(www.fesliyanstudios.com)\" " + f"{Fore.MAGENTA}\n"
                    f"{Fore.RED}\"Sound Jay(https://www.soundjay.com/crowd-talking-1.html#google_vignette)\" " + f"{Fore.MAGENTA}\n"
                    f"{Fore.RED}\"RobinHood76(https://freesound.org/people/thefilmbakery/downloaded_sounds/)\" " + f"{Fore.MAGENTA}\n"
                    f"{Fore.RED}\"Syna-Max(https://freesound.org/people/Syna-Max/sounds/54984/)\" " + f"{Fore.MAGENTA}\n")
        else:
            print("\nCREE:\nEric use the special weapon.\n")
            next()

            print(
                "\n\x1B[3mEric grabs the weapon and aims it at the Molgra. He shoots the weapon, but the weapon is "
                "not firing yet.\n")
            next()

            print("\nEric:\nThe gun needs to charge to it's full capacity to fire!\n")
            next()

            print("\nCREE: Everyone keep shooting at the Molgra until the weapon fires.\n")
            next()

            print("\n\x1B[3mSuddenly, you hear loud screeches coming from the stairs you just entered.\n")
            print(f"\x1B[3m{Style.BRIGHT}**RAhhhh Rahhhhh**\n")
            next()

            print(
                "\n\x1B[3mThe creatures are called the 'Svis Drone'. It's a creature with an elongated and dry mouth "
                "that nearly stretches to its chest. Its eyes bulge out of its eye sockets. It has ghostly pale and "
                "brittle flesh and has muscle tissue-like vines growing and weaving through its skin, "
                "like long strings of attached stitches hanging off its body.\n")
            next()

            print(
                "\n\x1B[3mThe screeches become more intense, and suddenly 20 Svis Drones come running into the room. "
                "You and your crew pull out your weapons, and start shooting.\n")

            print("\nLILY:\nThere's too many of them. How long do we have!\n")
            next()

            print("\nERIC:\nThe gun is only half way charged! Keep covering! \n")
            next()

            print("\nCREE:\nEric pass me the special smoke bomb! I think I can slow them down!\n")
            next()

            print(
                "\n\x1B[3mYou go towards Eric and grab the special smoke bomb. You go to one of the walls next to a "
                "vent,and climb up the vines.")
            next()

            print("\nCREE: Here goes!\n")
            next()

            print(
                "\n\x1B[3mYou release the bomb and throw it down the vent. Instantly a cloud of smoke begins to form "
                "everywhere. The smoke is so clouded that you can not see anything, as if everything around you is "
                "made of smoke. The smoke travels everywhere around the ship.\n")
            next()

            print(
                "\n\x1B[3mThe screeching of the creatures start to decrease in sound, and suddenly there is no noise "
                "at all.\n")
            next()

            print("\nERIC: EVERYONE STAND BACK!\n")
            next()

            print(f"\x1B[3m{Style.BRIGHT}*BEEEEEEEEEEM*\n")
            print(
                "\nA loud blasting sound cuts through the silence and Eric aims at the spot where he was aiming at "
                "the Molgra.\n")
            next()

            print("\n\x1B[3mThe Molgra makes a disturbed noise as it slowly loses control of its captives.\n")
            next()

            print(
                "\n\x1B[3mSuddenly, the thick smoke dissipates. All that is left is a floor covered in deceased pale "
                "creatures, and an empty space where there used to be the Molgra.\n")
            next()

            print("\nJOSEPH:\nIs that it? Did we defeat it?\n")
            next()

            print("\nERIC:\nI think so.\n")
            next()

            print("\n\x1B[3mEveryone looks exhausted and relieved.\n")
            next()

            print("\n\x1B[3mEveryone goes to the terminal.\n")
            next()

            print("\nCREE: We should head back to the Starphaser. Can you direct the ship to it? \n")
            next()

            print("\nJOSEPH:\nNebula, locate the Starphaser.\n")
            next()

            print("\nNEBULA:\n\x1B[3mLocating...\nStarphaser is 45 light years away.\n")
            next()

            print("\nJOSEPH:\nOk, travel to the Starphaser.\n")
            next()

            print(
                "\n\x1B[3mThe Orbulus is spotless and the infestation is over. It is drifting in space, returning to "
                "the Starphaser.\n")
            next()

            print(
                f"{Fore.MAGENTA}You and your crew made it out alive. Thanks for playing " +
                f"{Fore.RED}\"Aboard The Orbulus\" " + f"{Fore.MAGENTA}!")
            print(
                f"{Fore.MAGENTA}Music created by\n " +
                f"{Fore.RED}\"FesliyanStudios(www.fesliyanstudios.com)\" " + f"{Fore.MAGENTA}\n"
                f"{Fore.RED}\"Sound Jay(https://www.soundjay.com/crowd-talking-1.html#google_vignette)\" " + f"{Fore.MAGENTA}\n"
                f"{Fore.RED}\"RobinHood76(https://freesound.org/people/thefilmbakery/downloaded_sounds/)\" " + f"{Fore.MAGENTA}\n"
                f"{Fore.RED}\"Syna-Max(https://freesound.org/people/Syna-Max/sounds/54984/)\" " + f"{Fore.MAGENTA}\n")
    else:
        print(
            "\n\x1B[3mYou guys go after the Molrga. Eric starts shooting at the monster, and everyone else does the "
            "same. Your weapons seem to be ineffective.\n")
        next()

        if "infected" in items:
            print("\nCREE:\nQuick Eric use the special weapon.\n")
            next()

            print(
                "\n\x1B[3mSuddenly, one of the vines on the walls detaches and wraps around Eric's legs. Eric is "
                "hanging upside down and the Molgra consumes him. The weapon drops to the floor next to the Molgra.\n")
            next()

            print("\nJUDE:\nERIC!\n")
            next()

            print("\n\x1B[3mYou go towards the weapon next to the Molgra.\n")
            next()

            print("\n\x1B[3mYou go to the spot where the weapon is and grab on to it tightly.\n")
            next()

            print("\nCREE:\nAAHHHhh!\n")
            next()

            print("\n\x1B[3mThe increasing pain begins to form again on your arm.\n")
            next()

            print("\nCREE:\nNo, not now!\n")
            next()

            print(
                "\n\x1B[3mYou check your arm, and suddenly, you see that your veins have become even more green than "
                "before. The same color shade as emeralds.\n")
            next()

            print("\n\x1B[3m*ZZZ BSSHHH*\n")
            next()

            print("\n\x1B[3mThe blast comes from you. Jude falls to the ground.\n")
            next()

            print("\nJoseph:\nJude!\n")
            next()

            print("\n\x1B[3mJoseph goes over to try getting the weapon but you shoot him as well.\n")
            next()

            print(
                "\n\x1B[3mAnd everything starts to be less hostile towards you, as if they recognize you as their "
                "own.\n")
            next()

            print("\n\x1B[3mYou take the weapon, and you leave it with you.\n")
            next()

            print("\n\x1B[3mYou return back to normal.\n")
            next()

            print("\nCREE:\nERIC! JUDE! JOSEPH!\n")
            next()

            print("\nCREE:\nHow could I do this?\n")
            next()

            print("\n\x1B[3mYou begin to become tearful as you realize what you have done.\n")
            next()

            print(
                "CREE:\nEveryone, run away from here! Stay away from me! Protect yourself. Find an escape pod and "
                "leave. I’m already infected…\n")
            next()

            print("\n\x1B[3mLily and Jackson leave.\n")
            next()

            print(
                "\n\x1B[3mYou and the Molgra are still in the room. You feel as though the source is manipulating "
                "you. Nothing is in your control anymore. You and the Molgra are whole.\n")
            next()

            print(
                "\n\x1B[3mSuddenly, your body is paler than it’s ever been. You notice that the veins are protruding "
                "through your skin, and it starts to peel through your skin. The veins have become vines. The vines "
                "wrap over your body. You have now become a subject of the Molgra.\n")
            next()

            print("\n\x1B[3mYou leave the room and find other hordes over the ship.\n")
            next()

            print("\n\x1B[3mEveryone runs frantically in different directions searching for the escape pods.\n")
            next()

            print("\nLILY:\nWhere do we go?\n")
            next()

            print("\nJACKSON:\nThis ship is huge, I don't remember where the escape pods are.\n")
            next()

            print("\nSuddenly, you hear loud screeches coming from the stairs you just entered.\n")
            print(f"\x1B[3m{Style.BRIGHT}**RAhhhh Rahhhhh**\n")
            next()

            print("\n\x1B[3mThe screeches become more intense, and suddenly 10 hordes come running into the hallway.\n")

            print("\n\x1B[3mThe creatures continue to chase after them as they continue to run.\n")
            next()

            print("\nJACKSON: Oh no! We've reached a dead end.\n")
            next()

            print("\nLILY:\nWE just have to turn around and shoot!\n")
            next()

            print(
                "\n\x1B[3mEveryone turns around a shoots at the multitude of creatures piling on top of each other. "
                "Everyone becomes surrounded by the creatures as they consume your crew's body. They were not able to "
                "make it out of the Orbulus.\n")
            next()

            print(
                "\n\x1B[3mThe Orbulus continues to ominously drift in space, covered in the substance that took away "
                "a team of heroes…\n")
            next()

            print(
                f"{Fore.MAGENTA}You made it alive, but infected. Your entire crew died. Thanks for playing " +
                f"{Fore.RED}\"Aboard The Orbulus\" " + f"{Fore.MAGENTA}!")
            print(
                f"{Fore.MAGENTA}Music created by\n " +
                f"{Fore.RED}\"FesliyanStudios(www.fesliyanstudios.com)\" " + f"{Fore.MAGENTA}\n"
                f"{Fore.RED}\"Sound Jay(https://www.soundjay.com/crowd-talking-1.html#google_vignette)\" " + f"{Fore.MAGENTA}\n"
                f"{Fore.RED}\"RobinHood76(https://freesound.org/people/thefilmbakery/downloaded_sounds/)\" " + f"{Fore.MAGENTA}\n"
                f"{Fore.RED}\"Syna-Max(https://freesound.org/people/Syna-Max/sounds/54984/)\" " + f"{Fore.MAGENTA}\n")
        else:
            print("\nCREE:\nEric use the special weapon.\n")
            next()

            print(
                "\n\x1B[3mEric grabs the weapon and aims it at the Molgra. He shoots the weapon, but the weapon is "
                "not firing yet.\n")
            next()

            print("\nEric:\nThe gun needs to charge to it's full capacity to fire!\n")
            next()

            print("\nCREE: Everyone keep shooting at the Molgra until the weapon fires.\n")
            next()


            print("\n\x1B[3mSuddenly, you hear loud screeches coming from the stairs you just entered.\n")
            print(f"\x1B[3m{Style.BRIGHT}**RAhhhh Rahhhhh**\n")
            next()

            print(
                "\n\x1B[3mThe screeches become more intense, and suddenly 20 hordes come running into the room. You "
                "and your crew pull out your weapons, and start shooting.\n")

            print("\nLILY:\nThere's too many of them. How long do we have!\n")
            next()

            print("\nERIC:\nThe gun is only half way charged! Keep covering! \n")
            next()

            print("\nCREE:\nEric pass me the special smoke bomb! I think I can slow them down!\n")
            next()

            print(
                "\n\x1B[3mYou go towards Eric and grab the special smoke bomb. You go to one of the walls next to a "
                "vent,and climb up the vines.")
            next()

            print("\nCREE: Here goes!\n")
            next()

            print(
                "\n\x1B[3mYou release the bomb and throw it down the vent. Instantly a cloud of smoke begins to form "
                "everywhere. The smoke is so clouded that you can not see anything, as if everything around you is "
                "made of smoke. The smoke travels everywhere around the ship.\n")
            next()

            print(
                "\n\x1B[3mThe screeching of the creatures start to decrease in sound, and suddenly there is no noise "
                "at all.\n")
            next()

            print("\nERIC: EVERYONE STAND BACK!\n")
            next()

            print(f"\x1B[3m{Style.BRIGHT}*BEEEEEEEEEEM*\n")
            print(
                "\nA loud blasting sound cuts through the silence and Eric aims at the spot where he was aiming at "
                "the Molgra.\n")
            next()

            print("\n\x1B[3mThe Molgra makes a disturbed noise as it slowly loses control of its captives.\n")
            next()

            print(
                "\n\x1B[3mSuddenly, the thick smoke dissipates. All that is left is a floor covered in deceased pale "
                "creatures, and a empty space where there used to be the Molgra.\n")
            next()

            print("\nJOSEPH:\nIs that it? Did we defeat it?\n")
            next()

            print("\nERIC:\nI think so.\n")
            next()

            print("\n\x1B[3mEveryone looks exhausted and relieved.\n")
            next()

            print("\n\x1B[3mEveryone goes to the terminal.\n")
            next()

            print("\nCREE: We should head back to the Starphaser. Can you direct the ship to it? \n")
            next()

            print("\nJOSEPH:\nNebula, locate Starphaser.\n")
            next()

            print("\nNEBULA:\n\x1B[3mLocating...\nStarphaser is 45 light years away.\n")
            next()

            print("\nJOSEPH:\nOk, travel to the Starphaser.\n")
            next()

            print(
                "\n\x1B[3mThe Orbulus is spotless and the infestation is over. It is drifting in space, returning to "
                "the Starphaser.\n")
            next()

            print(
                f"{Fore.MAGENTA}You and your crew made it out alive. Thanks for playing " +
                f"{Fore.RED}\"Aboard The Orbulus\" " + f"{Fore.MAGENTA}!")
            print(
                f"{Fore.MAGENTA}Music created by\n " +
                f"{Fore.RED}\"FesliyanStudios(www.fesliyanstudios.com)\" " + f"{Fore.MAGENTA}\n"
                f"{Fore.RED}\"Sound Jay(https://www.soundjay.com/crowd-talking-1.html#google_vignette)\" " + f"{Fore.MAGENTA}\n"
                f"{Fore.RED}\"RobinHood76(https://freesound.org/people/thefilmbakery/downloaded_sounds/)\" " + f"{Fore.MAGENTA}\n"
                f"{Fore.RED}\"Syna-Max(https://freesound.org/people/Syna-Max/sounds/54984/)\" " + f"{Fore.MAGENTA}\n")
