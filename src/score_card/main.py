import os
import sys

# Must be before any kivy imports when testing on desktop
from kivy.config import Config

if os.environ.get("KIVY_BUILD") != "android":
    Config.set("graphics", "width", "360")
    Config.set("graphics", "height", "780")
    Config.set("graphics", "dpi", "160")
    Config.set("graphics", "resizable", "0")

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from database import init_db
from screens.menu import MenuScreen
from screens.event_list import EventListScreen
from screens.event_form import EventFormScreen
from screens.board_list import BoardListScreen
from screens.board_form import BoardFormScreen


class ScoreCardApp(App):
    title = "Score Card"
    icon = "images/icon.png"

    def build(self):
        init_db()

        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(EventListScreen(name="event_list"))
        sm.add_widget(EventFormScreen(name="event_form"))
        sm.add_widget(BoardListScreen(name="board_list"))
        sm.add_widget(BoardFormScreen(name="board_form"))
        return sm


ScoreCardApp().run()
