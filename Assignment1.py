class Car:
    def __init__(self, manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg, exterior_color, interior_color, accident, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine = engine
        self.transmission = transmission
        self.drivetrain = drivetrain
        self.mpg = mpg
        self.exterior_color = exterior_color
        self.interior_color = interior_color
        self.accident = accident
        self.price = price

    def paint(self, new_color):
        self.exterior_color = new_color
        print(f"The car has been painted {new_color}.")

    def repair(self, part, replacement):
        if part == "engine":
            self.engine = replacement
        elif part == "transmission":
            self.transmission = replacement
        elif part == "drivetrain":
            self.drivetrain = replacement
        else:
            print("Invalid part. Please choose 'engine', 'transmission', or 'drivetrain'.")
        print(f"The {part} has been replaced with {replacement}.")

    def reupholster(self, new_interior_color):
        self.interior_color = new_interior_color
        print(f"The interior has been reupholstered to {new_interior_color}.")

    def drive(self, miles):
        self.mileage += miles
        print(f"The car has been driven for {miles} miles. New mileage: {self.mileage} miles.")

    def modify_price(self, new_price):
        if new_price < 1:
            discount = self.price * new_price
            self.price -= discount
            print(f"The new discounted price is: ${self.price:.2f}.")
            confirm = input("Do you confirm this price (yes/no)? ").lower()
            if confirm == "yes":
                print("Price confirmed.")
            else:
                print("Price modification aborted.")
        else:
            self.price = new_price
            print(f"The new price has been set to ${self.price:.2f}.")

class Seller:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.inventory = []

    def buy(self, car):
        if car not in self.inventory:
            self.inventory.append(car)
            print(f"{car.manufacturer} {car.model} has been added to {self.name}'s inventory.")

    def sell(self, car):
        if car in self.inventory:
            self.inventory.remove(car)
            print(f"{car.manufacturer} {car.model} has been sold from {self.name}'s inventory.")
        else:
            print(f"The car is not available in {self.name}'s inventory.")
