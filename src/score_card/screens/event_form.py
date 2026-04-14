from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import sqlite3

KV = """
<EventFormScreen>:
    canvas.before:
        Color:
            rgba: BG
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        padding: dp(40)
        spacing: dp(16)

        ScTitle:
            text: "New Event"

        ScLabel:
            text: "Enter event details"
            color: TEXT_HINT
            size_hint_y: None
            height: dp(30)

        TextInput:
            id: name_input
            hint_text: "Event Name"
            multiline: False
            size_hint_y: None
            height: dp(50)

        TextInput:
            id: date_input
            hint_text: "Date (YYYY-MM-DD)"
            multiline: False
            size_hint_y: None
            height: dp(50)

        TextInput:
            id: location_input
            hint_text: "Location"
            multiline: False
            size_hint_y: None
            height: dp(50)

        TextInput:
            id: notes_input
            hint_text: "Notes"
            size_hint_y: None
            height: dp(100)

        Widget:
            size_hint_y: 1

        ScButton:
            text: "Save Event"
            on_release: root.save_event()

        ScButton:
            text: "Back"
            on_release: root.manager.current = "menu"
"""


Builder.load_string(KV)


class EventForm(BoxLayout):
    def save_event(self):
        name = self.ids.name_input.text
        date = self.ids.date_input.text
        location = self.ids.location_input.text
        notes = self.ids.notes_input.text

        if not name or not date:
            print("Name and Date are required")
            return

        conn = sqlite3.connect("events.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                location TEXT,
                notes TEXT,
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)

        cursor.execute(
            "INSERT INTO events (name, date, location, notes) VALUES (?, ?, ?, ?)",
            (name, date, location, notes),
        )

        conn.commit()
        conn.close()

        print("Event saved!")

        self.ids.name_input.text = ""
        self.ids.date_input.text = ""
        self.ids.location_input.text = ""
        self.ids.notes_input.text = ""


class EventFormScreen(Screen):
    pass
