class Car():
   def __init__(self,color,engine_displacement,distance,fuel_level,tank_capacity):
       self.color = color
       self.engine_displacement = engine_displacement
       self.distance = distance
       self.fuel_level = fuel_level
       self.tank_capacity = tank_capacity

   def reset_counter(self):
       self.distance=0

   def increase_counter(self,counter):
       self.distance += counter

   def refuel(self,amount):
       if(self.fuel_level >= self.tank_capacity):
           print("Tank is already full!")
       elif(self.fuel_level+amount <= self.tank_capacity):
           self.fuel_level += amount
           print(f"Added {amount}L. New fuel level: {self.fuel_level}")
       else:
           added = self.tank_capacity - self.fuel_level
           self.fuel_level = self.tank_capacity
           print(f"Tank is full. Added only {added}L")

car1 = Car(color="Red",engine_displacement=1.6,distance=10000,fuel_level=20,tank_capacity=50)
car2 = Car(color="Black",engine_displacement=3.5,distance=45000,fuel_level=50,tank_capacity=100)

print("Car1 color: ",car1.color)
print("Car2 color: ",car2.color)
car1.reset_counter()
print("\nCar1 counter: ",car1.distance)
car2.increase_counter(3000)
print("Car2 counter: ",car2.distance)
car2.refuel(60)