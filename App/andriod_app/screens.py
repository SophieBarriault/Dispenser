from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
import pytesseract

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Welcome to the App")
        proceed_button = Button(text="Proceed to Loading")
        
        proceed_button.bind(on_press=self.go_to_loading)

        layout.add_widget(label)
        layout.add_widget(proceed_button)
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
        self.manager.current = 'ocr_screen'  # Automatically go to OCR after loading

class OCRScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button = Button(text="Upload Image for OCR")
        button.bind(on_press=self.choose_file)
        layout.add_widget(button)
        self.add_widget(layout)

    def choose_file(self, instance):
        filechooser = FileChooserIconView()
        filechooser.bind(on_selection=self.on_file_selected)
        popup = Popup(title="Choose an image", content=filechooser, size_hint=(0.8, 0.8))
        popup.open()

    def on_file_selected(self, filechooser, selected):
        if selected:
            image_path = selected[0]
            text = pytesseract.image_to_string(image_path)
            print(text)  # Handle extracted text here
            self.manager.current = 'log_screen'  # Navigate to the log screen

class LogScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Push Notifications Log")
        self.add_widget(label)
 