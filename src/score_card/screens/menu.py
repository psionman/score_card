import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import style

HERE = os.path.dirname(os.path.abspath(__file__))
Builder.load_file(os.path.join(HERE, "..", "kv", "menu.kv"))


class MenuScreen(Screen):
    pass
