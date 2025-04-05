from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Oh yeah", 100, 2)

print(my_taxi)
print(my_taxi.get_fare())
my_taxi.drive(18)
assert my_taxi.get_fare() == 48.78