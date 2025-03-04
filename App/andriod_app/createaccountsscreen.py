from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from accounts import create_account, check_account_exists 
class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = BoxLayout(orientation='vertical')

        # Text inputs for username and password
        self.username_input = TextInput(hint_text="Enter username", multiline=False)
        self.password_input = TextInput(hint_text="Enter password", multiline=False, password=True)
        
        # Label for feedback
        self.feedback_label = Label(text="")

        # Create Account button
        self.create_button = Button(text="Create Account")
        self.create_button.bind(on_press=self.create_account)

        # Add widgets to the layout
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.create_button)
        self.layout.add_widget(self.feedback_label)

        self.add_widget(self.layout)

    def create_account(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if not username or not password:
            self.feedback_label.text = "Username and password cannot be empty."
            return

        # Check if the account already exists
        if check_account_exists(username):
            self.feedback_label.text = "Username already exists. Please choose a different one."
            return

        # Create the account in accounts
        if create_account(username, password):
            self.feedback_label.text = f"Account for {username} created successfully!"
            # Optionally, redirect to LoginScreen or show a success message
            self.manager.current = 'login_screen'  # Change to your login screen's name
        else:
            self.feedback_label.text = "Failed to create account. Please try again."
