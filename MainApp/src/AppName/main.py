from kivy.app import App
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.picker import MDDatePicker
from kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.tab import MDTabsBase
from datetime import datetime
from data_manager import DataManager

class IntroScreen(Screen):
    pass

class GeneralOverViewScreen(Screen):
    pass

# tabs

class timetableTab(BoxLayout , MDTabsBase):
    pass

class journeyTab(BoxLayout , MDTabsBase):
    pass

class checkInTab(BoxLayout , MDTabsBase):
    pass

class securityTab(BoxLayout , MDTabsBase):
    pass

class personalTab(BoxLayout , MDTabsBase):
    pass

class boardingTab(BoxLayout , MDTabsBase):
    pass


class MainApp(App):

    theme_cls = ThemeManager()
    title = "Main App"

    def show_date_picker(self):
        MDDatePicker(self.get_date).open()

    def get_date(self, date_obj):
        self.intro_screen.ids.flight_date_field.text = date_obj.strftime("%d/%m/%Y")

    def set_flight_information(self):
        flight_number = self.intro_screen.ids.flight_number_field.text
        flight_date = self.intro_screen.ids.flight_date_field.text
        print(self.data_manager.set_flight(flight_number,flight_date))

    def set_data(self):

        # get end time = departure time
        departure_time = self.data_manager.get_departure().strftime("%H:%M")

        # set or calculate the time
        self.main_tabs.ids.end_time_label.text = departure_time

    def build(self):

        self.data_manager = DataManager()

        self.theme_cls.them_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Gray"

        # screens
        self.intro_screen = IntroScreen(name="IntroScreen")

        self.main_tabs = GeneralOverViewScreen(name="GeneralOverViewScreen")
        self.main_tabs.ids.android_tabs.add_widget(timetableTab())
        self.main_tabs.ids.android_tabs.add_widget(journeyTab())
        self.main_tabs.ids.android_tabs.add_widget(checkInTab())
        self.main_tabs.ids.android_tabs.add_widget(securityTab())
        self.main_tabs.ids.android_tabs.add_widget(personalTab())
        self.main_tabs.ids.android_tabs.add_widget(boardingTab())

        # ScreenManager to switch different pages
        sm = ScreenManager()
        sm.add_widget(self.intro_screen)
        sm.add_widget(self.main_tabs)

        return sm

if __name__ == "__main__":
    MainApp().run()
