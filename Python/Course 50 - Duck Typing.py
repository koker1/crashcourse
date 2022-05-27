#Duck typing = concept where the class of an object is less important than the methods/attributes
#              对象的类不如方法/属性重要的概念
#              class type is not checked if minimum methods/attributes are present
#              如果存在最少的方法/属性，则不检查类类型
#              "If it walks like a duck, and it quacks like a duck, then it must be a duck"
#              “如果它走路像鸭子，叫起来像鸭子，那它一定是鸭子”

class Duck:

    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking")

class Chicken:

    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is clucking")

class Person:

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)