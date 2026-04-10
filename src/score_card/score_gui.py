import os
if os.environ.get("KIVY_BUILD") != "android":
    # Only apply on desktop — ignored on real device
    from kivy.config import Config
    Config.set("graphics", "width", "360")
    Config.set("graphics", "height", "780")
    Config.set("graphics", "dpi", "416")
    Config.set("graphics", "resizable", "0")

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from screens.new_event import NewEventScreen


KV_FILES = [
    "kv/main_menu.kv",
    "kv/new_event.kv",
    # "kv/list_events.kv",
    # "kv/event.kv",
]

class MenuScreen(Screen):
    pass

class EventScreen(Screen):
    pass

class ScoreCardApp(MDApp):
    icon = "src/score_card/images/favicon.png"

    def build(self):
        self.theme_cls.theme_style = "Dark"          # Try "Dark" if you prefer
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.material_style = "Rounded"     # or "Sharp"


        # Force background (very important in 2.0)
        # self.theme_cls.bg_color = [0.98, 0.98, 0.98, 1]
        # self.theme_cls.bg_color = [0, 0, 0, 1]
        self.theme_cls.bg_color = [0.07, 0.07, 0.07, 1]

        self.theme_cls.theme_text_color = "Primary"   # helps globally
        self.theme_cls.text_color = [0.95, 0.95, 0.98, 1]   # almost white

        for kv in KV_FILES:
            Builder.load_file(kv)
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(NewEventScreen(name="new_event"))
        return sm
