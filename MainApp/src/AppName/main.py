from kivy.app import App
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.tab import MDTabsBase

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

    def build(self):
        self.theme_cls.them_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Gray"

        # screens
        main_tabs = GeneralOverViewScreen(name="GeneralOverViewScreen")
        main_tabs.ids.android_tabs.add_widget(timetableTab())
        main_tabs.ids.android_tabs.add_widget(journeyTab())
        main_tabs.ids.android_tabs.add_widget(checkInTab())
        main_tabs.ids.android_tabs.add_widget(securityTab())
        main_tabs.ids.android_tabs.add_widget(personalTab())
        main_tabs.ids.android_tabs.add_widget(boardingTab())

        # ScreenManager to switch different pages
        sm = ScreenManager()
        sm.add_widget(IntroScreen(name="IntroScreen"))
        sm.add_widget(main_tabs)

        return sm

if __name__ == "__main__":
    MainApp().run()
