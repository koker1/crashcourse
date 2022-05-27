#method chaining = calling multiple methods sequentially
#                  顺序调用多个方法
#                  each call performs an action on the same object and returns self
#                  每次调用对同一个对象执行一个操作并返回 self

class Car:

    def turn_on(self):
        print("you start the engine")
        return self

    def drive(self):
        print("you drive the car")
        return self
    
    def brake(self):
        print("you step on the brakes")
        return self
    
    def turn_off(self):
        print("you turn off the engine")
        return self

car = Car()

'''car.turn_on()
car.drive()
car.brake()
car.turn_off'''

#method chaining
'''car.turn_on().drive().brake().turn_off()'''

#也可以写成
'''car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()'''
