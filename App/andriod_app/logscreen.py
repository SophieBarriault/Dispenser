class LogScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Push Notifications Log")
        layout.add_widget(label)
        # Add a scrollable view to display notifications
        self.add_widget(layout)
