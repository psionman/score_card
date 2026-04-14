from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDDatePicker
from datetime import date


class NewEventScreen(Screen):
    selected_date = None
    status_message = ""

    def show_date_picker(self):
        def on_save(value, date_range):
            self.selected_date = value.strftime("%B %d, %Y")
            self.ids.date_button.text = self.selected_date

        def on_cancel():
            pass

        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=on_save, on_cancel=on_cancel)
        date_dialog.open()

    def save_event(self):
        self.status_message = "Event saved successfully! ✅"
        print("Event saved!")

    def go_back(self):
        self.manager.current = "menu"
