from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.pickers import MDDockedDatePicker

from models.event import load_events, save_events, create_event


class NewEventScreen(Screen):
    status_message = StringProperty("")
    selected_date = StringProperty("")

    def show_date_picker(self):
        picker = MDDockedDatePicker()
        picker.bind(on_save=self.on_date_selected, on_cancel=lambda *a: None)
        picker.open()

    def on_date_selected(self, instance, value, date_range):
        self.selected_date = value.strftime("%Y-%m-%d")
        self.ids.date_button.text = self.selected_date

    def save_event(self):
        name = self.ids.name_input.text.strip()
        location = self.ids.location_input.text.strip()
        notes = self.ids.notes_input.text.strip()

        if not name:
            self.status_message = "Event name is required"
            return
        if not self.selected_date:
            self.status_message = "Date is required"
            return

        events = load_events()
        events.append(create_event(name, self.selected_date, location, notes))
        save_events(events)

        self.status_message = "Event saved!"
        self.clear_form()

    def clear_form(self):
        self.selected_date = ""
        self.ids.date_button.text = "Select Date"
        for field in ("name_input", "location_input", "notes_input"):
            self.ids[field].text = ""

    def go_back(self):
        self.status_message = ""
        self.clear_form()
        self.manager.current = "menu"
