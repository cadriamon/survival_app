"""
This gameplay.py module contains functions for gameplay.

Attributes
----------
search_bool : dict
    search_bool dictionary attribute contains boolean values that represent 
    whether an area has been searched or not. The keys represent the specific
    area. If the area has not been searched, the boolean flag is false, and 
    true if it has been searched.
"""
import time

search_bool = {
    "HOME": False,
    "GARAGE": False,
    "NEIGHBORS": False,
    "PARK": False,
    "BACKYARD": False,
    "NEIGHBORS BACKYARD": False,
    "HIGH SCHOOL": False,
    "SHOPPING CENTER": False,
    "CHURCH": False,
    "PARKING GARAGE": False,
    "GRAVEYARD": False,
    "DEEP GRAVEYARD": False,
    "MALL": False,
    "MOTEL": False,
    "COURTHOUSE": False,
    "COLLEGE": False,
    "WOODS": False,
    "POLICE STATION": False,
    "GYM": False,
    "LAKE": False,
    "MANSION": False,
    "MOUNTAIN": False,
    "CABIN": False,
    "BEACH": False,
    "BARS": False,
    "DOCK": False,
    "CONSTRUCTION AREA": False,
    "CRANE": False,
    "LIGHTRAIL": False,
    "HOSPITAL": False,
    "EMERGENCY ROOM": False,
    "DARK TUNNEL": False,
    "YACHT": False,
    "HELIPAD": False,
    "BOAT": False
}


def menu():
    """Menu function that prints out menu graphic text"""
    print("\n---Menu---")


def manual():
    """Manual function that prints out the tutorial or manual for the game."""
    print("\nHello! You are stuck in a zombie apocalypse! This is an original idea!" +
          "\n\nGOAL: Your goal is to leave the zombie infested city alive. After" +
          "\nnaming your character, you can choose a difficulty of easy, normal, and" +
          "\nhard which will affect your initial player stats of HP (hitpoints), hunger, " +
          "\nand thirst levels." +
          "\n\nTRAVEL: As you travel within the city, you must ensure your HP, hunger," +
          "\nand thirst levels never reach 0 or it is GAME OVER. Moving between areas",
          "\nwill reduce your hunger, thirst, sometimes your HP, or possibly cause an" +
          "\nunlucky a GAME OVER." +
          "\n\nSEARCH: You are given an option to SEARCH an area to sometimes find" +
          "\nfood and water if your situation is dire. Be warned, searching can" +
          "\nalso cause bad things to happen." +
          "\n\nGood luck survivor!")


def option(area1: str, area2: str, stats: str, journal: dict, desc: str, area: str, area_desc: str) -> str:
    """Option function that gives the player options to play the game.

    Function runs infinite while loop until a string value is returned 
    to the main.py file.

    Parameters
    ----------
    area1
        area1 string parameter represents the first area choice the player
        can travel to.
    area2
        area2 string parameter represents the second area choice the player
        can travel to.
    stats
        stats string parameter is imported from player object to display
        player object stats such as name, hp, hunger, thirstto player
    journal
        journal dictionary parameter is imported from player object
        to display stored journal values to player
    desc 
        desc string parameter is imported from area object to 
        display search description to player
    area
        area string parameter is imported from area object to
        display the current name of current area object from
        main.py
    area_desc
        area_desc string parameter is import from area object
        to display current area descrption from main.py

    Returns 
    -------
    str
        area1 string parameter if player inputs 1
        area2 string parameter if player inputs 2
        "SEARCH" string value if player inputs 3
    """
    while True:
        menu()
        print("1. Travel to", area1)
        print("2. Travel to", area2)
        print("3. Search area")
        print("4. Stats", )
        print("5. Read Journal")
        print("6. Area description")
        print("7. Instructions")
        option = input("Please select an option: ")
        if option == "1":
            print("\n")
            return area1
        elif option == "2":
            print("\n")
            return area2
        elif option == "3":
            if search_bool[area] == False:
                search_bool[area] = True
                print("\n")
                s = "You searched " + str(area) + ". "
                print(s)
                print(desc)
                add_journal(journal, s + desc)
                time.sleep(2)
                return "SEARCH"
            else:
                print("\nYou already searched this area.")
                time.sleep(1)
        elif option == "4":
            print(stats)
        elif option == "5":
            read_journal(journal)
        elif option == "6":
            print("\nDescription:\n" + area_desc)
            time.sleep(5.0)
        elif option == "7":
            manual()
        else:
            print("Invalid option.")


def check_hp(hp: int) -> bool:
    """check_hp function checks if player hp is below or equal 0

    Parameters
    ----------
    hp
        hp int paramter represents player object's hp

    Returns
    --------
        True if HP is below or equal to 0, False otherwise
    """
    if hp <= 0:
        return True
    else:
        return False


def check_hunger(hunger: int) -> bool:
    """check_hunger function checks if player hunger is below or equal 0

    Parameters
    ----------
    hunger
        hunger int paramter represent player object's hunger level

    Returns
    -------
        True if hunger is below or equal to 0, False otherwise
    """
    if hunger <= 0:
        return True
    else:
        return False


def check_thirst(thirst: int) -> bool:
    """check_thirst function checks if player thirst is below or equal 0

    Parameter
    ---------
    thirst
        thirst int paramter represents player object's thirst level

    Returns
    -------
        True if thirst is below or equal to 0, False otherwise
    """
    if thirst <= 0:
        return True
    else:
        return False


def change_area(area: str, journal: dict):
    """change_area function prints area change to player

    The text is printed to the player and appened to player journal
    Parameters
    ----------
    area
        area string parameter is imported from area object to
        display the current name of current area object from
        main.py
    journal
        journal dictionary parameter is imported from player object
        to display stored journal values to player

    Attributes
    ---------
    s : string
        s string variable holds printed text of area change
        that prints to player and appends to journal
    """
    print("\n")
    s = "You traveled to " + str(area) + "."
    print(s)
    add_journal(journal, s)
    time.sleep(2)


def add_journal(journal: dict, s: str):
    """add_journal function appends s value to journal dictionary

    Parameters
    ----------
    journal
        journal dictionary parameter is imported from player object
        to display stored journal values to player
    s : string
        s string paranter holds printed text to be appended to
        player journal
    """
    journal.append(s)


def read_journal(journal: dict):
    """read_journal function iterates through journal dictionary

    As it iterates, each entry is numbered and printed to player

    Parameters
    ----------
    journal
        journal dictionary parameter is imported from player object
        to display stored journal values to player
    """
    print("\n--Journal--")
    for j in range(0, len(journal), 1):
        print(str(j+1) + ". " + journal[j])
