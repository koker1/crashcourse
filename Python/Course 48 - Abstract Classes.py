#Prevents a user from creating an object of that class 
#防止用户创建该类的对象
#+ compels a user to override abstract methods in a child class
#+ 强制用户覆盖子类中的抽象方法

#abstract class = a class which contains one or more abstract methods.
#                 包含一个或多个抽象方法的类。
#abstract method = a method that has a declaration but does not have an implementation.
#                  有声明但没有实现的方法。

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("you drive the car")

    def stop(self):
        print("this car is stopped")

class Motorcycle(Vehicle):
    
    def go(self):
        print("you ride the motorcycle")
    
    def stop(self):
        print("this motorcycle is stopped")

'''vehicle = Vehicle()'''
car = Car()
motorcycle = Motorcycle()

'''vehicle.go()'''
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
