#Number of the cars availabel
cars = 100
#capacity of the car
space_in_car = 4.0
#Total number of drivers
drivers = 30
#Total number of passengers
passengers = 90
#The number of cars without drivers
cars_not_driven = cars - drivers
#The number of the cars which have driver
cars_driven = drivers
#How many people can be transported right now
carpool_capacity = cars_driven*space_in_car
#The number of people in each car on average
average_passengers_per_car = passengers/cars_driven

print("There are",cars,"cars available")
print("There are only",drivers,"drivers available")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
