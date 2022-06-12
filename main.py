import kivy
from cyoa_surv_pkg import player, area, gameplay, area_dictionary
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class Title(Screen):
    pass


class Load_Game(Screen):
    pass


class Manual(Screen):
    pass


class Setting(Screen):
    pass


class Difficulty(Screen):
    pass


class Gameplay(Screen):
    def main_menu(self):
        print("1. Start New Game")
        print("2. Instructions")
        print("3. Exit")
        option = input(
            "Welcome to Choose Your Own Adventure - Surival Edition! Please select an option: ")


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
