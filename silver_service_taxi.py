from taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel, 1.23)
        self.name = name
        self.fuel = fuel
        self.price_per_km = 1.23 * fanciness
        self.fanciness = fanciness
        self.flagfall = 4.5

    def __str__(self):
        return "{}, fuel={}, odo={}, {}km on current fare, ${}/km plus flagfall of ${}".format(self.name, self.fuel, self.odometer, self.current_fare_distance, self.price_per_km, self.flagfall)

    def get_fare(self):
        return round(super().get_fare()+self.flagfall, 1)
