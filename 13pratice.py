#intance method
class dominos:
    def __init__(self, name, price) :
        self.name = name
        self.price = price
    def cheeze(self):
        print(f"{self.name} cheeze")
              
my_dominos = dominos("pizza", "maxcian")
my_dominos.cheeze()


#class method

"""
class students:
  num_of_students = 0

def __init__(self, name):
  self.name = name
students.num_of_students += 1

@classmethod
def number_of_students(cls):
    return cls.num_of_students

s1 = students("sonu")
s2 = students("nikhil")
print(students.number_of_students())  

"""

#static method

class company:
   hike = 15000
   def __init__(self,name ,age):
      self.name= name
      self.age =age 

def infromaton(self):
   print(f"name: {self.name} ")
   print(f"age: {self.age} ")

@classmethod  
def my_hike(cls):
   print("infromation about hike is displayed here")

company1 = company("sonu", 20)
company.my_hike()
