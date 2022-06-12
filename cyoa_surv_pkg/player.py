"""
This player.py module contains class and functions for player object.
"""


class Player:
    def __init__(self, name: str, hp: int, hunger: int, thirst: int, area: str):
        """__init__function that instantiates player object for main.py game

        Parameters
        ---------
        name
            name string parameter represent name of playeer object
        hp 
            hp int paramter represents the hp level of player object
        hunger
            hunger int paramter represents the hunger level for player object
        thirst
            thirst int paramter represents the thirst level for player object

        Attributes 
        ----------
        name
            name string attribute represent name of playeer object
        hp 
            hp int attribute represents the hp level of player object
        hunger
            hunger int attribute represents the hunger level for player object
        thirst
            thirst int attribute represents the thirst level for player object
        journal
            journal dict attribute builds empty dictionary for player journal
        """
        self.name = name
        self.hp = hp
        self.hunger = hunger
        self.thirst = thirst
        self.area = area
        self.journal = []

    def player_stats(self) -> str:
        """player_stats function formats and returns player object info

        If any of player HP, hunger, or thirst levels are below 0, it just 
        displays the stat as 0 instead of the negative integer.

        Attributes
        ----------
        s : string
            s string attribute holds formatted player information

        Returns
        -------
        string
            Returns s string attribute

        """
        if self.hp < 0:
            self.hp = 0
        if self.hunger < 0:
            self.hunger = 0
        if self.thirst < 0:
            self.thirst = 0
        s = ("\n--Stats--" + "\nName: " + self.name + "\nHP: " + str(self.hp) +
             "\nHunger: " + str(self.hunger) + "\nThirst: " + str(self.thirst))
        return s

    def change_area(self, area: str):
        """change_area function changes current player object area attribute

        Parameters
        -----------
        area
            area string parameter represents area object name
            to change curret player object area attribute to
        """
        self.area = area

    def change_hp(self, hp: int):
        """change_hp adjusts hp based on parameter and formats printed text

        The value of HP will affect the printed statement to player.

        Parameters
        ----------
        hp
            hp int paramter represents the amount to be changed
            to current player object. Can be any real integer

        """
        if hp < 0:
            print("\nYou lost:", hp, "HP")
        elif hp > 0:
            print("\nYou gained:", hp, "HP")
        else:
            print("\nNo change in HP.")
        self.hp += hp

    def change_hunger(self, hunger: int):
        """change_hunger adjusts hunger based on parameter and formats printed text

        The value of hunger will affect the printed statement to player.

        Parameters
        ----------
        hunger
            hunger int paramter represents the amount to be changed
            to current player object. Can be any real integer

        """
        if hunger < 0:
            print("\nYou lost:", hunger, "hunger")
        elif hunger > 0:
            print("\nYou gained:", hunger, "hunger")
        else:
            print("\nNo change in hunger.")
        self.hunger += hunger

    def change_thirst(self, thirst):
        """change_thirst adjusts thirst based on parameter and formats printed text

        The value of thirst will affect the printed statement to player.

        Parameters
        ----------
        thirst
            thirst int paramter represents the amount to be changed
            to current player object. Can be any real integer

        """
        if thirst < 0:
            print("\nYou lost:", thirst, "thirst")
        elif thirst > 0:
            print("\nYou gained:", thirst, "thirst")
        else:
            print("\nNo change in thirst.")
        self.thirst += thirst
