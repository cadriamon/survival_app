import kivy
from cyoa_surv_pkg import area, gameplay, player as play, area_dictionary as ad
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


class Start_Game(Screen):
    player_name = ObjectProperty(None)

    pc = Player("", 0, 0, 0, "HOME")

    def easy_difficulty(self):
        self.pc.name = self.player_name.text
        self.pc.hp = 200
        self.pc.hunger = 200
        self.pc.thirst = 200


class Gameplay(Screen):
    playerStats = Label()
    storyText = Label()

    layout = GridLayout()

    def start_game(self):
        pass

    def update(self):
        self.remove_widget(self.playerStats)
        self.remove_widget(self.storyText)
        self.playerStats = Label(text="Name: " + Start_Game.pc.name + " HP: " +
                                 str(Start_Game.pc.hp), pos_hint={'center_x': .9, 'center_y': .9})
        self.add_widget(self.playerStats)
        self.storyText = Label(
            text=ad.desc[Start_Game.pc.area], pos_hint={'center_y': .7})
        self.add_widget(self.storyText)

    def area_1(self):
        Start_Game.pc.area = ad.area1[Start_Game.pc.area]
        self.update()

    def area_2(self):
        Start_Game.pc.area = ad.area2[Start_Game.pc.area]
        self.update()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
