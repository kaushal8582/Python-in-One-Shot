class Car:

  total_car =0

  def __init__(self, brand,model):
    self.__brand = brand
    self.__model =model
    Car.total_car+=1
  
  def get_brand(self):
    return self.__brand + "!"

  def full_name(self):
    return f"{self.__brand} {self.__model}"
  
  def fuel_type(self):
    return "Petrol or desiel"
  
  @staticmethod
  def general_description():
    return "Cars are menas of transport"
  
  @property
  def model(self):
    return self.__model


class ElectricCar(Car):
  def __init__(self, brand,model, batterySize):
    super().__init__(brand,model)
    self.batterySize = batterySize

  def fuel_type(self):
    return "Electric charge"



# my_Tesla = ElectricCar("Tesla","Modle K","1111kwh");

# print(isinstance(my_Tesla,ElectricCar)) // check instance or not 
# print(isinstance(my_Tesla,Car))

# print(my_Tesla.full_name())
# print(my_Tesla.get_brand());

# print(my_Tesla.fuel_type());

# my_Car = Car("Tata","safari");
# print(my_Car.model) // @property
# my_Car = Car("Tata","safari");
# my_Car = Car("Tata","safari");
# print(my_Car.fuel_type());

# print(Car.general_description())


# my_car = Car("Toyoto","corollo")

# print(my_car.full_name())


class Battery:
  def battery_info(self):
    return "This is battery"

class Engine:
  def engine_info(self):
    return "This is Engine"
  
class Electric_Car_Two(Battery,Engine,Car):
  pass
  

my_new_car = Electric_Car_Two("Suzuki","kaushal");

print(my_new_car.battery_info());
print(my_new_car.engine_info());
