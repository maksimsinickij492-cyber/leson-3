#print("hello")

#name = "maks"
#print(name)

#age = 12
#+print(12)



class Student:
    def __init__(self,name="Невідомий",height=160):
        self.name = name
        self.height = height

    def grow(self,cm):
        self.height += cm
        print(f"{self.name} виріс, зріст {self.height}")

    def __str__(self):
        return f"Студент {self.name},його зріст - {self.height}"



bob = Student("Bob",150)
kate = Student("kate",167)
bob.grow(10)
print(bob)


print(bob.name)