from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout 
from screens import WelcomeScreen, LoadingScreen, OCRScreen, LogScreen 
from Andriod_App import OCRApp 
import accounts 
from accounts import create_table 
from createaccountsscreen import CreateAccountScreen  # Import screen 


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.proceed_button = Button(text="Click to start!")
        self.proceed_button.bind(on_press=self.go_to_loading)

        self.layout.add_widget(self.proceed_button)

        self.add_widget(self.layout)

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
        self.manager.current = 'ocr_screen'  # Automatically go to OCR after loading 


#class LoginScreen(Screen):
    # Your LoginScreen code...
#    pass 



#class HomeScreen(Screen):
   # def __init__(self, **kwargs):
        #super().__init__(**kwargs)
        #self.layout = BoxLayout(orientation='vertical')
        #self.layout.add_widget(Label(text="Welcome to the home screen"))
        #self.add_widget(self.layout)




class OCRScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = OCRApp(label=Label(text="Initializing OCR"))
        self.add_widget(self.layout.build()) 

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(WelcomeScreen(name='welcome_screen'))
        sm.add_widget(LoadingScreen(name='loading_screen'))
        sm.add_widget(OCRScreen(name='ocr_screen'))

        return sm 




if __name__ == '__main__':
    MyApp().run() 
