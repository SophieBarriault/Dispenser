from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Welcome to the App")
        button = Button(text="Proceed to Loading")
        button.bind(on_press=self.go_to_loading)
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_loading(self, instance):
        self.manager.current = 'loading_screen'

class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Loading...")
        layout.add_widget(label)
        self.add_widget(layout)

    def on_enter(self):
        self.manager.current = 'login_screen'  # Automatically go to login after loading

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Login")
        layout.add_widget(label)
        # Add login form elements here (Username, Password, etc.)
        self.add_widget(layout)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome_screen'))
        sm.add_widget(LoadingScreen(name='loading_screen'))
        sm.add_widget(LoginScreen(name='login_screen'))
        return sm

if __name__ == '__main__':
    MyApp().run()
