from car import car
from customer import customer
from rental import rental

#create cars
car1 = car("C001","toyota","Innvoa",2022)
car2 = car("C002","Honda","Accord",2022)

#create customer

customer1 = customer("CU001","Mukul Sheware")
customer2 = customer("CU002","Sonali nimje")


#rent cars
customer1.rent_car(car1)
customer2.rent_car(car2)

#Display Rented cars for customer
print(f"{customer1.name}'s Rented cars:{[car.make for car in customer1.rented_cars]}")
print(f"{customer2.name}'s Rented cars:{[car.make for car in customer2.rented_cars]}")


#return car
customer1.return_car(car1)

#displayupdated rented cars for customer
print(f"{customer1.name}'s Updated Rented cars:{[car.make for car in customer1.rented_cars]}")
print(f"{customer2.name}'s Updated Rented cars:{[car.make for car in customer2.rented_cars]}")

#create rentals
rental1 = rental("R001",customer1,car1,rental_fee=500.0)
rental2 = rental("R002",customer2,car2,rental_fee=450.0)


#display 
print(f"Rented ID:{rental1.rental_id},Customer:{rental1.customer.name},car:{rental1.car.make},Rental Fee:INR{rental1.rental_fee}")
print(f"Rented ID:{rental2.rental_id},Customer:{rental2.customer.name},car:{rental2.car.make},Rental Fee:INR{rental2.rental_fee}")