from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
INVALID_TAXI = "Invalid taxi choice"
DRIVE_HOW_FAR = "Drive how far? "

def main():
    taxis = get_taxis()
    bill = 0.0
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available")
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ")
            try:
                taxi_choice = int(taxi_choice)
                if -1 < taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print(INVALID_TAXI)
            except ValueError:
                print(INVALID_TAXI)
        elif choice == "d":
            if current_taxi:
                distance = get_distance()

                current_taxi.start_fare()
                current_taxi.drive(distance)

                trip_cost = current_taxi.get_fare()
                bill += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def get_taxis():
    taxis = []
    prius = Taxi("Prius", 100)
    taxis.append(prius)
    limo = SilverServiceTaxi("Limo", 100, 2)
    taxis.append(limo)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    taxis.append(hummer)
    return taxis

def display_taxis(taxis):
    for i,taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def get_distance():
    distance = input(DRIVE_HOW_FAR)
    valid_distance = False
    while not valid_distance:
        try:
            distance = int(distance)
            if distance >= 0:
                valid_distance = True
            else:
                distance = input(DRIVE_HOW_FAR)
        except ValueError:
            distance = input(DRIVE_HOW_FAR)
    return distance

main()