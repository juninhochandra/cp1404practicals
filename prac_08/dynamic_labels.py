from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Juninho", "Ernita", "Gracelynn", "Susanto"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        # self.create_widgets()
        for name in self.names:
            temp_button = Label(text=name)
            self.root.ids.main.add_widget(temp_button)
        return self.root

DynamicLabelsApp().run()