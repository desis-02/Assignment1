Purpose: The purpose of this project is to create a virtual management system for a network of used car dealerships. The system allows for the tracking of cars in each dealership's inventory. This system can perform various operations, such as painting, repairing, or updating cars, as well as tracking their movement between sellers.

Car Class
The Car class represents individual cars and their attributes. Each car has the following properties:
manufacturer: The brand of the car (e.g., Toyota, Ford).
model: The specific model of the car (e.g., Camry, F-150).
year: The manufacturing year of the car.
mileage: The current mileage of the car.
engine: The type of engine in the car (e.g., 2.0L 4-cylinder).
transmission: Type of transmission (e.g., manual, automatic).
drivetrain: The type of drivetrain (e.g., FWD, RWD, AWD).
mpg: Fuel efficiency in miles per gallon.
exterior_color: The exterior color of the car.
interior_color: The interior color of the car.
accident: Boolean flag indicating whether the car has been involved in an accident.
price: The selling price of the car.
Methods in the Car Class:
paint(new_color): Changes the exterior color of the car.
repair(part, replacement): Repairs or replaces key components (engine, transmission, drivetrain).
reupholster(new_interior_color): Changes the interior color of the car.
drive(miles): Adds mileage to the car's total mileage.
modify_price(new_price): Adjusts the car price. If the value is less than 1, the price is discounted by a percentage.

Seller Class
The Seller class represents a seller or a dealership with an inventory of cars.
name: The name of the seller (dealership).
rating: A rating system for the dealership.
inventory: A list to hold the cars currently in the seller’s inventory.
Methods in the Seller Class:
buy(car): Adds a car to the seller’s inventory.
sell(car): Removes a car from the seller’s inventory.

Limitations
Repair Method: The repair method is limited to specific parts (engine, transmission, drivetrain). More flexibility can be added in future iterations to handle other parts.
Modify_Price: The price modification asks for confirmation when discounting a price. In future iterations, this process could be streamlined or automated.
Inventory System: Currently, sellers' inventories are separate from each other. A future update could allow for a shared inventory across multiple sellers.
