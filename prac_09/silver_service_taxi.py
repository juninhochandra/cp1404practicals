from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def get_fare(self):
        return self.flagfall + self.price_per_km * self.current_fare_distance

    def start_fare(self):
        self.current_fare_distance = self.flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"