from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    taxis = [Taxi("Prius", 100, 1.2), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    current_taxi = taxis[0]
    total_cost = 0
    menu_choice = input("q)uit, c)hoose taxi, d)rive").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            taxi_number = 0
            for taxi in taxis:
                print("{} - {}".format(taxi_number, taxi))
                taxi_number += 1
            taxi_choice = int(input("Choose taxi:"))
            current_taxi = taxis[taxi_choice]

        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far?"))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
            total_cost += trip_cost
        print("Bill to date: ${:.2f}".format(total_cost))
        menu_choice = input("q)uit, c)hoose taxi, d)rive").lower()
    print("Total trip cost: ${:.2f}\nTaxis are now:".format(total_cost))
    taxi_number = 0
    for taxi in taxis:
        print("{} - {}".format(taxi_number, taxi))
        taxi_number += 1

main()
