import colorama
import pygame
from colorama import Fore, Style
from functions import next, items, play_music, play_sound
from choices import *
from alternate_storylines import *
from pygame import mixer

colorama.init(autoreset=True)
mixer.init()

# This will be used for the save function, by appending the player's input of choices to the list.
save = []
# This function is used for items in the story. If a player has an item in the dictionary,
# the items that they have could be useful in the future.
items = {}


def main():
    play_music(1, 0.60)
    print("Rising Shield Studios Presents...\n")
    print(f"{Fore.RED}Aboard the Orbulus")
    print(f"{Fore.RED}---------------------------------")
    next()

    print(
        "\n\x1B[3mIn the vast emptiness of space, you and your crew are aboard a spaceship, the Starphaser. The "
        "members of your crew are tasked with delivering triple helix energy rods, and other supplies to the colony "
        "planet Zeno, which is currently being prepared as another settlement for human life. You are “Cree”, "
        "the captain of this ship. You are the guidance for this crew, every decision you make determines everything "
        "- choose wisely…\n")
    next()
    play_music(2, 0.04, 60.0)
    print(
        "\n\x1B[3mFrom the cylindrical access terminal Andromeda’s pink, icosahedronal, holographic form flickered to "
        "life from the terminal.\n")
    next()

    print(
        "\nANDROMEDA:\n\x1B[3m*voice message*\nMessage from: Ambassador Morgans… Greetings, Captain Cree.I would like "
        "to thank you and your crew for taking up this task, I want you to lead the members on the Starphaser to "
        "Planet Zeno and deliver the triple helix energy rods. You only need to make sure they are delivered to the "
        "workers. They will make sure they are installed properly. Good luck out there.\n")
    next()

    print(
        "\n\x1B[3mThere are 13-15 people on the ship including 5 Magnus’, 2 Universal Service Droids(USDs), "
        "6 EEDs(Environmental Explorer Droids), and 3 MARs(Multi-Purpose Analysis Robots). In Section D of the ship ("
        "Lounge Area). Everyone is chattering amongst each other excited about the space mission.\n")
    next()

    print(
        "\nCREE: \nAlright listen, I want everyone to continue training for their positions. This is a critical "
        "mission. We must expand the locations for humanity. Andromeda, do we have any reading for where Planet Zeno "
        "may be located?\n")
    next()

    print(
        "\nANDROMEDA:\n*robotic*\n" + "\x1B[3mScanning…" + "\nThe newly registered Planet Zeno is located on the "
                                                           "Ionas system.\n")
    next()

    print("\nCREE:\nDo you have any reading about the distance from here?\n")
    next()

    print("\nANDROMEDA:" + "\n\x1B[3mScanning…" + "\nApproximately 1.7 million light-years away…\n")
    next()

    print(
        "\nCREE:\nAt the pace we are moving now, it will take us years to locate the planet… ANDROMEDA set the speed "
        "of the ship to 370 thousand light-years/ month.\n")
    next()

    print(
        "\n\x1B[3mThe Starphaser is drifting through space, and suddenly its speed begins to increase. A loud WHOOSH! "
        "sound cuts through the quietness of space, and the Starphaser DASHES like the speed of light, "
        "leaving nothing but the essence of transparent comet-like laser trails from behind, slowly dissipating.\n")
    next()

    print("\nJUDE:\nCaptain Cree, we are-\n")
    print(
        "\nANDROMEDA:" + f"\n\x1B[3m*{Style.BRIGHT}BEEP! BEEP! BEEP! BEEP!*" + "\n\x1B[3mDetecting…" + "\nUnknown "
                                                                                                       "space shuttle"
                                                                                                       " is located "
                                                                                                       "670 thousand "
                                                                                                       "light-years "
                                                                                                       "away. "
                                                                                                       "Probability "
                                                                                                       "of collision: "
                                                                                                       "69%.\n")
    next()

    print(
        "\n\x1B[3mThe Starphaser is set in speed, moving rapidly through space. Located ahead, in close proximity, "
        "is a pus-like putrid orange, bulbous overgrowth covering every inch of an unknown colony space shuttle; the "
        "ship looks rusty and dilapidated. The Starphaser becomes increasingly close to the shuttle.\n")
    print("Should you...")
    print(f"{Fore.LIGHTRED_EX}1) Stop your shuttle entirely, and wait for the mysterious shuttle to pass by")
    print(f"{Fore.LIGHTRED_EX}2) Slow down your shuttle, and try to inspect the mysterious shuttle")
    choice()
    next()

    print(
        "\nCREE:\nAndrew, I want you to be the leader of the ship until I return. I need a technician and medic with "
        "me. Jude, you’ll be our technician, Eric, you’ll be our medic, and I’ll bring Sam along. It’s time to find "
        "some answers…\n")
    next()

    print(
        "\n\x1B[3mThe team is in Section A of the ship: the Weaponry. You guys enter a room with a white fluorescent "
        "aroma. On the walls, there are blue hues of light illuminating 20 types of weaponry on display.\n")
    next()

    print(
        "\nCREE:\nHere, you guys choose the weapons that you will take with you. I’ll get my special weapons for "
        "combat. My weapons once took down a giant alien 20ft tall, the Enormeter.\n")
    next()

    print(
        "\n\x1B[3mYou tap a single spot on the wall, and a doorway reveals itself. You enter the secret bunker, "
        "and in the center of the room, there is a clear glass casing.\n")
    alternate_stories_1()
    next()

    print("\nCREE:\nEric you need to be able to carry medical equipment, make sure you grab a storage pack.\n")
    next()

    print(
        "\n\x1B[3mEric grabs a tiny microchip and presses a button on it. The microchip grows in length and expands "
        "to a full-size med-kit pack. Eric puts his medical equipment inside and presses the button again. The "
        "med-kit shrinks in size to a microchip.\n")
    next()

    print("\nJUDE:\nI’ll take one too.\n")
    next()

    print("\nCREE:\nOk ALBERT, how far is the shuttle?\n")
    next()

    print("\nALBERT:\n\x1B[3mScanning…\n45,200 miles years away\n")
    next()

    print("\nCREE:\nLet’s head out. Andromeda, deploy MAR-356.\n")
    next()

    print("\nANDROMEDA:\n\x1B[3mDeploying MAR-356...\n")
    next()

    print(
        "\n\x1B[3mOn the Starphaser a small hatch opens up, like the door to a submarine, and a small cube-shaped "
        "robot appears. It almost resembled a toaster. The robot has a center opening in the middle of it, "
        "which features its eyes and scanning function. Attached to the sides of the toaster-like machine is a long "
        "compartment for its arms. As you leave the Starphaser, the EEDs return to the ship.\n")
    next()

    print("\n\x1B[3mYour crew leaves the vagueness of space and approaches closer to the ominous shuttle.\n")
    next()

    print("\nJUDE:\nCaptain, I see an airlock at the top level on the left!\n")
    next()

    print("\nCREE:\nEveryone, follow Jude.\n")
    next()

    print("\n\x1B[3mYou and your crew get closer to the entryway of the shuttle.\n")
    next()

    print(
        "\n\x1B[3mThe crew approaches the airlock and Cree turns the airlock handle causing the door to let out a "
        "hiss, however, the door is covered in vines.\n")
    next()

    print("\nCREE:\nEric, help me budge open this door.\n")
    next()

    print("\nERIC:\nHere I come Cree.\n")
    next()

    print("\n\x1B[3mEric floats over to Cree and pulls out his coil shotgun\n")
    print("ERIC:\nStand back guys.\n")
    next()

    print(
        "\n\x1B[3m*ZZZZ! ZZZZ! ZZZZZ!*\nEric pulls the trigger as multiple streaks of lightning arc out from the "
        "copper barrel. The bolts shred the vines into heated green pieces that slowly float away. The door "
        "forcefully opens, and everyone stands alarmed, looking into the darkness.")

    print(
        "\n\x1B[3mThe group enters and Jude manually closes the door with a 'THUNK!' and locks it. The "
        "decontamination room activates and decontaminates the boarding group.\n")
    next()

    print(
        "\n\x1B[3mThe door opens revealing an empty and dark hallway. It’s dark, yet there is some light. Like the "
        "sporadic flashing street lights in the night of an alleyway. The atmosphere is clouded, almost like fog in "
        "the early morning. There’s not a single noise. Not in the emptiness of space, nor in the desolate hallways. "
        "They enter a dark room with 3 doors.\n")
    next()

    print("\nJUDE:\nDo we go in?\n")
    next()

    print("\nERIC:\nYes, we made it this far. Why stand here just to look, when we can explore?\n")
    next()

    print("\nCREE:\nDon’t be so hasty Eric, we need SAM to scan the area. SAM, scan our surroundings.\n")
    next()

    print("\nSAM:\n\x1B[3mApologies… I can only scan the room I'm in unless I have the map data for this area.\n")
    next()

    print("\nCREE:\nOk, don’t worry about it. Everyone, let’s just be vigilant.\n")
    next()

    print("\nJUDE:\nIt’s too dark in here, let me see if I can find the lights and fix them.\n")
    next()

    if len(save) == 2:
        alternate_stories_2()

    print("\nCREE:\n\x1B[3m*thinking*\nWhere should we go now?\n")
    next()

    if len(save) == 1:
        print("\nCREE:\nLet’s go to the Power Sector.\n")
        next()

        print("\n\x1B[3mEveryone enters through the doorway.\n")
        next()

        print("\nERIC:\nCaptain, shouldn't we be returning back to the Starphaser?\n")
        next()

        print(
            "\nCREE:\nWe have to change plans. We have to figure out what’s going on here. We have to find out what "
            "happened.\n")
        next()

        print(
            "\nCREE:\nI need to locate a holograph communication pod. I need to contact Christopher. He has to "
            "deliver the energy rods before Ambassador Morgans realizes that we have not completed our mission. But "
            "first, we need power.\n")
    else:
        alternate_stories_3()
    next()

    print(
        "\nJUDE:\nActually, we can send ALBERT back to the Starphaser. He can  be with Christopher to help direct the "
        "ship to Zeno.\n")
    next()

    alternate_stories_4()

    print("\nCREE:\nOkay, ALBERT, send the message.\n")
    next()

    print("\n\x1B[3mALBERT goes through one of the ventilation systems and leaves the crew.\n")
    next()

    print("\nERIC:\nWhy is this ship so huge? Where should we go next, Cree?\n")
    next()

    print("\nYou guys approach a divided hallway.")
    print("\nWhich way will you go?")
    print(f"{Fore.LIGHTRED_EX}1) Left")
    print(f"{Fore.LIGHTRED_EX}2) Diagonally Right")
    choice4()
    next()

    print("\nERIC:\nOk, so what’s the plan now?\n")
    next()

    print(
        "\n\x1B[3mThey travel to another section of the Orbulus. They enter a dark room that is slightly illuminated "
        "by an emergency blaring red light. Inside the room, there are semi-huge generators planted on the floor, "
        "circuit breaker boxes that are attached to seven poles, and electrical wires displayed on one side of the "
        "room’s walls. It is filled with everything that powers the ship.\n")
    next()

    print("\nJUDE:\nSAM, scan the room.\n")
    next()

    print("\nSAM:\n\x1B[3mScanning room…\nThe Emergency generator is online-\n")
    next()

    print("\nERIC:\nThat explains why some of the lights are on.\n")
    next()

    print("\nSAM:\n\x1B[3m-Main and secondary generators are offline. The units are missing power sources.\n")
    next()

    print("\nJUDE:\nPower sources…\n")
    next()

    print("\nJUDE:\nWe could find energy rods.\n")
    next()

    print("\nCREE:\nWe can explore and see if we can find one for the Main generator.\n")

    alternate_stories_5()

    print("\nCREE:\nOkay, let's go...")
    print(f"{Fore.LIGHTRED_EX}1)Go to the Left.")
    print(f"{Fore.LIGHTRED_EX}2)Go straight ahead.")
    choice5()

    print("\n\x1B[3mAs the group exits the tram, you venture down a stairway that goes deeper into the space ship.\n")
    next()

    print(
        "\n\x1B[3mYou guys enter a new floor that is spacious enough to have its own inside playground. The center of "
        "the floor is filled with long hovering dining tables. You have entered the Cafeteria. The room has various "
        "hallways that lead to different areas in the middle level.\n")
    next()

    print("\nCREE:\nLet's go to the Gym.\n")
    next()

    print("\n\x1B[3mIn the cafeteria you guys make a left into a hallway that leads to the gym.\n")
    next()

    print("\nERIC:\nJust as I suspected, empty.\n")
    next()

    print("\nCREE:\nWe’ll split up and look for clues.\n")
    next()

    print(
        "\n\x1B[3mYou go to one of the locker rooms. You examine the place, and you try to open the lockers with your "
        "gun.\n")
    next()

    print("\nShould you use your gun to unlock the locker?")
    print(f"{Fore.LIGHTRED_EX}1)Yes")
    print(f"{Fore.LIGHTRED_EX}2)No")
    choice6()

    print("\n\x1B[3mThere were no more items, and you went to the bathroom adjoining the locker room.\n")
    next()

    print("\n\x1B[3mYou go inside to look around the place, and you notice that one of the shower cubicles is wet.\n")
    next()

    print("\nCREE:\nFresh water droplets… interesting. \n")
    next()

    print("\n\x1B[3mOnce you guys have explored the gym, you go back to the cafeteria.\n")
    next()

    print(
        "\n\x1B[3mYou enter the enormous cafe. It's dark and there are small particles floating around. There are "
        "enormous vines that are sprawled everywhere covering the white hover tables, and the curved sleek white "
        "hover chairs. Surrounding the outside of the cafe are different food vendors that probably were used to "
        "serve food.\n")
    next()

    print("\nERIC:\nWoah this is a huge cafe.\n")
    next()

    print("\nJUDE:\nYeah I can’t imagine wha-\n")

    print("\n\x1B[3mJude stops her sentence as the group hears a metallic thunk.\n")
    next()

    print("\nCREE:\nWhat was that...?\n")
    next()

    print(
        "\n\x1B[3mThe group hears another metallic thunk. This time sounding closer than the previous thunk. The "
        "group crouches and hides behind different chairs.\n")
    next()

    print("\nCREE:\nSam can you scan the room to figure out if someone or something is there...\n")
    next()

    print("\nSAM:\n\x1B[3mAffirmative.\n")
    next()

    print(
        "\n\x1B[3mThe drone floats us above the group. Multiple red lights emit from the drone as it scans the room. "
        "The light morphs and forms around the different objects and surfaces of the room.\n")
    next()

    print("\nSAM:\n\x1B[3mI have identified the target as an ASG-Magnus.\n")
    next()

    print("\nERIC:\nOh so we have nothing to worry about we can just identify ourselves.\n")
    next()

    print("\nSAM:\n\x1B[3mHowever, it is covered in an unknown organic substance.\n")
    next()

    print("\nSAM:\n\x1B[3mThis is the same substance that was identified in the hanger.\n")
    next()

    print("\nJUDE:\nLet me see.\n")
    next()

    print(
        "\n\x1B[3mJude peeks from around the chair just a bit in order to see. At that moment a crimson red eye came "
        "from around the corner causing Jude to immediately whip her head back behind the chair, her eyes wide with "
        "fear and her breath becoming much heavier yet quiet for fear of being heard.\n")
    next()

    print("\n\x1B[3mYou bring SAM closer to cover your face.\n")
    next()

    print("\nCREE:\nSam can you communicate with the Magnus.\n")
    next()

    print("\nSAM:\n\x1B[3mNow attempting.\n")
    next()

    print(
        "\n\x1B[3mSam begins to send signals to the sleek black machine in an attempt to communicate with it.All the "
        "drone receives however, is static and what can only be described as insanity, and malicious intent.\n")
    next()

    print("\nSAM:\n\x1B[3mCommunication attempt failed. I only received a malicious attempt to kill and control.\n")
    next()

    print("\nCREE:\nOk we need to go, we can't stay here.\n")
    next()

    print("\nERIC:\nDon’t worry captain I got this.\n")
    next()

    print(
        "\n\x1B[3mEric pulls out his microchip pack. It expands and he is able to access his bag. Eric opens a med "
        "kit and dumps its contents into the bag. He then shrinks the pack back into its microchip form. Eric chucks "
        "the empty container behind the Magnus causing it to turn its body in the direction of the sound.\n")
    next()

    print("\nWhat should you do...")
    print(f"{Fore.LIGHTRED_EX}1) Fight")
    print(f"{Fore.LIGHTRED_EX}2) Run")
    choice7()

    print(
        "\n\x1B[3mThe group bolts from their hiding spot while the sound of arm cannon bolts and metallic thudding "
        "follows them. You guys enter the hallway, you have two ways to go.\n")
    print("Where should you go...\n")
    print(f"{Fore.LIGHTRED_EX}1) Left")
    print(f"{Fore.LIGHTRED_EX}2) Right")
    choice8()

    if "death" in items:
        print(
            f"{Fore.RED}You died from a Infected Magnus." + f"{Fore.MAGENTA}Thanks for playing " +
            f"{Fore.RED}\"Aboard The Orbulus\" " + f"{Fore.MAGENTA}!")
        print(
            f"{Fore.MAGENTA}Music created by\n " +
            f"{Fore.RED}\"FesliyanStudios(www.fesliyanstudios.com)\" " + f"{Fore.MAGENTA}\n"
            f"{Fore.RED}\"Sound Jay(https://www.soundjay.com/crowd-talking-1.html#google_vignette)\" " + f"{Fore.MAGENTA}\n"
            f"{Fore.RED}\"RobinHood76(https://freesound.org/people/thefilmbakery/downloaded_sounds/)\" " + f"{Fore.MAGENTA}\n"
            f"{Fore.RED}\"Syna-Max(https://freesound.org/people/Syna-Max/sounds/54984/)\" " + f"{Fore.MAGENTA}\n")

    else:
        print(
            "\n\x1B[3mYou hang up on the communications, and try to go meet back at the cafeteria. On your way back, "
            "in the corner of one of the convenience store you find an energy rod attached to a deceased Magnus. You "
            "pick up the rod.\n")
        next()
        print(
            "\n\x1B[3mYou and everyone else goes back to the Power Sector to the generator room. Cree takes the "
            "energy rod from her pocket, and inserts the rod into the Main Generator.\n")
        next()

        print(
            "\nInstantly, the generator makes a loud industrial sound, resembling almost like the sound of a "
            "overworked lawn mower. \n")
        next()

        print("\nERIC:\nThe lights are on. Everything is working.\n")
        next()

        print("\nJUDE:\nGreat! Now that we can see better, we won't be so lost.\n")
        next()

        print("\n\x1B[3mFrom the Power Sector, you guys make a left into a hallway that leads to the Medical Sector\n")
        next()

        print(
            "\nCREE:\nOk, let’s see if there’s some clues here. Look for documents. Look at experiments. Look for "
            "something that may be unusual.\n")
        next()

        print(
            "\n\x1B[3mEveryone splits up in the medical room, looking through file cabinets, looking on tables, "
            "and looking at the medic lab.\n")
        next()

        alternate_stories_6()

        print(
            "\n\x1B[3mYou open a file cabinet next to the medic lab. Inside the cabinet, there are folders listing "
            "employees. You come across multiple faces, all saying that they are deceased from an unknown "
            "invasion…except for one.\n")
        next()

        print("\n\x1B[3mYou pick up the file, and return it to the crew.\n")
        next()

        print(
            "\nCREE:\nHey, I checked some files. Everyone was deceased from an invasion, except for one, "
            "“Lily Green”. Look.\n")
        next()

        print("\nERIC:\nDo you think she’s still alive?\n")
        next()

        print("\nJUDE:\nPossibly. Or maybe nobody was alive to say that she died?\n")
        next()

        print(
            "\nCREE:\nYes, or maybe she just was not present on the ship when the invasion happened. Like what "
            "happened to my mother. She vanished from the Starphaser and no one has seen her since.\n")
        next()

        print("\nCREE:\nWherever she is, we have to find her.\n")
        next()

        print("\nJUDE:\nCaptain, I found something over here.\n")
        next()

        print("\nJUDE:\nIt’s a huge box, but it’s locked. I think it needs a key.\n")
        next()

        alternate_stories_7()

        print("\n\x1B[3mYou guys walk to a tram station that says “Housing”.\n")
        next()

        print(
            "\n\x1B[3mAfter a while the tram finally comes. But through the windows there are entities looming in "
            "them. Instantly, everyone pulls out their weapons.\n")
        next()

        print("\nCREE:\nGuys be careful.\n")
        next()

        print(
            "\n\x1B[3mThe door opens, and everyone is tense aiming their gun on the targets. Three figures appear, "
            "however these figures look human.\n")
        next()

        print("\nJUDE:\nAre you human?\n")
        next()

        print("\n\x1B[3mOne of them holds their arms up.\n")
        next()

        print("\nJOSEPH:\nYes, we’re human, and we can’t thank you enough.\n")
        next()

        print("\nERIC:\nWell that’s not a response I would hear when you’re being targeted at.\n")
        next()

        print("\nLILY:\nYes, we’re human.\n")
        next()

        print("\nCREE:\nReally? Considering the circumstances, I did not think it was possible.\n")
        next()

        print("\n\x1B[3mEveryone begins to lower their weapon.\n")
        next()

        print("\nERIC:\nHow come you guys made it alive?\n")
        next()

        print(
            "\nLILY:\nWe were making our way to housing on the tram when all of a sudden the power went out and the "
            "tram became stuck.\n")
        next()

        print(
            "\nJOSEPH:\nLuckily I was able to break open one of the windows to get us out. Ever since the power went "
            "out, we just tried living without power.\n")
        next()

        print("\nCREE:\nHow come you did not go to the power sector?\n")
        next()

        print(
            "\nJOSEPH:\nWe did, but there was no power source when we went there. We saw that one of the creatures "
            "had it on them, but that was a big risk to take.\n")
        next()

        print(
            "\nJUDE:\nCome with us, since you guys know much about what’s going on. You can help us. When we make it "
            "out alive, we'll bring you to our colony.\n")
        next()

        print("\nJACKSON:\nThat sounds great. I that we have to look over every corner to make sure we survive.\n")
        next()

        print("\nJOSEPH:\nWait, you have the weapons.\n")
        next()

        print("\nJoseph goes up to Eric holding the special weapons.\n")
        next()

        print(
            "\nJOSEPH: Ever since this invasion happened, we've been making weapons to kill this infected. "
            "Unfortunately, the team started dwindling down, until I became the only one left on the team. "
            "Unfortunately, I couldn't open the capsule it was in, because our leader had it on him.\n")
        next()

        print("\nCREE:\nSo could these weapons kill everything on the ship?\n")
        next()

        print(
            "\nJOSEPH:\nPossibly, or it could make them weaker, or it could not work it all. No one really knows...\n")
        next()

        print("\nERIC:\nWell, we have to try.\n")
        next()

        print("\n\x1B[3mEric walks away from the tram, and goes back to the four doors.")
        next()

        print("\nERIC:\nCome on, it's time to stop this thing once and for all.\n")
        next()

        print(
            "\n\x1B[3mYou guys make it into the Hangar Tram, and exit. You guys enter a room filled with vines "
            "covering every inch of the place. The slimy vines are practically the room’s walls. In the center of "
            "this room is a giant plant-like entity rooted on the ground, the Molgra.\n")
        next()

        print("\nCREE:\nThis is our target! Attack!\n")
        next()

        alternate_stories_8()


if __name__ == "__main__":
    main()
