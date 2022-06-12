"""
This area.py module contains class and any functions for area object.
"""


class Area:
    def __init__(self, name: str, desc: str, hp: int, hunger: int, thirst: int, area1: str, area2: str,
                 search_desc: str, search_hp: int, search_hunger: int, search_thirst: int):
        """__init__ function initalizes a new area object

        Parameters
        ----------
        name
            name string paramenter represent area name
        desc 
            desc string parameter represents area description
        hp
            hp int parameter represents player hp adjustments in main.py
        hunger
            hunger int parameter represents player hunger adjustments in
            main.py
        thirst
            thirst_change int parameter represents player thirst adjustments in
            main.py 
        area1
            area1 str attribute parameter player's first area option in main.py
        area2
            area2 str attribute parameter player's second area option in main.py
        search_desc
            search_desc str parameter represents search description 
        search_hp
            search_hp int parameter represents player hp adjustments in main.py
            main.py when player searches
        search_hunger
            search_hunger int parameter represents player hunger adjustments in
            main.py when player searches
        search_thirst
            search_thirst int parameter represents player thirst adjustments in
            main.py when player searches

        Attributes
        ----------
        name
            name string attribute represent area name
        desc 
            desc string attribute represents area description
        hp
            hp int attribute represents player hp adjustments in main.py
        hunger
            hunger int attribute represents player hunger adjustments in
            main.py
        thirst
            thirst_change int attribute represents player thirst adjustments in
            main.py 
        area1
            area1 str attribute represents player's first area option in main.py
        area2
            area2 str attribute represents player's second area option in main.py
        search_desc
            search_desc str attribute represents search description 
        search_hp
            search_hp int attribute represents player hp adjustments in main.py
            main.py when player searches
        search_hunger
            search_hunger int attribute represents player hunger adjustments in
            main.py when player searches
        search_thirst
            search_thirst int attribute represents player thirst adjustments in
            main.py when player searches
        """
        self.name = name
        self.desc = desc
        self.hp_change = hp
        self.hunger_change = hunger
        self.thirst_change = thirst
        self.area1 = area1
        self.area2 = area2
        self.search_desc = search_desc
        self.search_hp = search_hp
        self.search_hunger = search_hunger
        self.search_thirst = search_thirst
