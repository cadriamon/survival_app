import kivy
from cyoa_surv_pkg import area, gameplay, area_dictionary as AD
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock


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
        # self.journal = []


class Title(Screen):
    pass


class Load_Game(Screen):
    pass


class Manual(Screen):
    pass


class Setting(Screen):
    pass


class Difficulty(Screen):
    player_name = ObjectProperty(None)

    player = Player("", 0, 0, 0, "HOME")

    def easy_difficulty(self):
        self.player.name = self.player_name.text
        self.player.hp = 200
        self.player.hunger = 200
        self.player.thirst = 200


class Gameplay(Screen):
    playerStats = Label()
    storyText = Label()

    layout = GridLayout()

    def start_game(self):
        self.playerStats = Label(text="Name: " + Difficulty.player.name + " HP: " +
                                 str(Difficulty.player.hp), pos_hint={'center_x': .9, 'center_y': .9})
        self.add_widget(self.playerStats)
        self.storyText = Label(
            text=AD.desc[Difficulty.player.area], pos_hint={'center_y': .7})
        self.add_widget(self.storyText)
        Difficulty.player.hp += 50

    def area_1(self):
        self.remove_widget(self.playerStats)
        self.remove_widget(self.storyText)
        Difficulty.player.area = AD.area1[Difficulty.player.area]
        self.playerStats = Label(text="Name: " + Difficulty.player.name + " HP: " +
                                 str(Difficulty.player.hp), pos_hint={'center_x': .9, 'center_y': .9})
        self.add_widget(self.playerStats)
        Difficulty.player.hp += 50
        self.storyText = Label(
            text=AD.desc[Difficulty.player.area], pos_hint={'center_y': .7})
        self.add_widget(self.storyText)

    def area_2(self):
        self.remove_widget(self.playerStats)
        self.remove_widget(self.storyText)
        Difficulty.player.area = AD.area2[Difficulty.player.area]
        self.playerStats = Label(text="Name: " + Difficulty.player.name + " HP: " +
                                 str(Difficulty.player.hp), pos_hint={'center_x': .9, 'center_y': .9})
        self.add_widget(self.playerStats)
        Difficulty.player.hp += 50
        self.storyText = Label(
            text=AD.desc[Difficulty.player.area], pos_hint={'center_y': .7})
        self.add_widget(self.storyText)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
