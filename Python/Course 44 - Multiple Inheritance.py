#multiple inheritance = when a child class is derived from more than one parent class
#                       当一个子类派生自多个父类时

class Prey:

    def flee(self):
        print("this animal flees")


class Predator:

    def hunt(self):
        print("this animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

'''rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()'''