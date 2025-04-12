from prac_09.unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar("Useless", 100, 30.0)

for _ in range(100):
    my_unreliable_car.drive(3)
    print(my_unreliable_car.fuel)