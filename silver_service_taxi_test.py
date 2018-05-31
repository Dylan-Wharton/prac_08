from silver_service_taxi import SilverServiceTaxi


def main():
    Hummer = SilverServiceTaxi("Hummer", 100, 2)
    Hummer.drive(18)
    current_fare = Hummer.get_fare()
    print(current_fare)
    print(Hummer)


main()
