from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from kivy.core.window import Window #used to quit/close window

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = BoxLayout()
        # Add your code below to add the two Buttons
        btn_setting = Button(text = "Settings", on_press = self.change_to_setting)
        self.layout.add_widget(btn_setting)
        btn_quit = Button(text = "Quit", on_press = self.quit_app)
        self.layout.add_widget(btn_quit)
        self.add_widget(self.layout)

    def change_to_setting(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
        self.manager.current = 'settings'

    def quit_app(self, value):
        App.get_running_app().stop()
        Window.close()


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = BoxLayout()
        # Add your code below to add the label and the button
        lbl_settings = Label(text = "Settings Screen")
        self.layout.add_widget(lbl_settings)
        btn_backtomenu = Button(text = "Back to Menu", on_press = self.change_to_menu)
        self.layout.add_widget(btn_backtomenu)
        self.add_widget(self.layout)

    def change_to_menu(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
        self.manager.current = "menu"


class SwitchScreenApp(App):
    def build(self):
            sm = ScreenManager()
            ms = MenuScreen(name='menu')
            st = SettingsScreen(name='settings')
            sm.add_widget(ms)
            sm.add_widget(st)
            sm.current = 'menu'
            return sm


SwitchScreenApp().run()
