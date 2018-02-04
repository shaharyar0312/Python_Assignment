class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
      self.battery_size = battery_size
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
class Electric_car(Car):
    def __init__(self, make, model,year):
        """        Initialize attributes of the parent class.        Then initialize attributes specific to an electric car.        """
        super().__init__(make, model, year)
        self.battery = Battery()

elec_car = Electric_car('suzuki', 'wagon r', '2016')
elec_car.battery.upgrade_battery()
elec_car.battery.get_range()