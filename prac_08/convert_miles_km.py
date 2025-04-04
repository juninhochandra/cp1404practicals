from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesToKilometres(App):
    result = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def validate_input(self):
        try:
            number = float(self.root.ids.input_number.text)
            self.convert_miles_to_km()
        except ValueError:
            self.result = "0.0"

    def handle_increment(self, num):
        try:
            number = float(self.root.ids.input_number.text)
            self.root.ids.input_number.text = str(number + num)
        except ValueError:
            self.root.ids.input_number.text = str(num)
        self.convert_miles_to_km()

    def convert_miles_to_km(self):
        self.result = str(float(self.root.ids.input_number.text) * MILES_TO_KM)

MilesToKilometres().run()