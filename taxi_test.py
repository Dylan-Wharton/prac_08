"""
CP1404/CP5632 Practical
Car class
"""
from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(fuel)
        self.name = name
        self.price_per_km = 1.23
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


def main():
    prius_1 = Taxi("Prius 1", 100)
    prius_1.drive(40)
    current_fare = prius_1.get_fare()
    print(current_fare)
    prius_1.start_fare()
    prius_1.drive(100)
    current_fare = prius_1.get_fare()
    print(current_fare)


main()
