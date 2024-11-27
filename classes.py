# class paper:
#     def __init__(self, texture, width, length, type_, material, use):
#         self.texture = texture
#         self.width = width
#         self.length = length
#         self.type_ = type_
#         self.material = material
#         self.use = use
#     def write(self):
#         print("writing...")
#     def draw(self):
#         paper.draw = "draw" + "love"
#         print("drawing...")
#     def color(self):
#         print("coloring...")
#
# user = paper("hard", 2, 5, "wood", "love", "draw")
# print(user.texture)
#
# user.draw()

# class student:
#     grade = 85 #Class Attribute
#     update = 10
#     def __init__(self, age): #Constructor
#         self.age = age #instance attribute
#     def new_grade(self): #method inside class
#         student.grade += self.update
#         return student.grade
# Tom = student(20)
# Tom.new_grade() #call method
# print(Tom.grade) #once error is resolved, prints 95

# class Food:
#     def __init__(self, temp, rate, num_ingredients):
#         self.temp = temp
#         self.rate = rate
#         self.num_ingredients = num_ingredients
# class Drink(Food):
#     def __init__(self, drink_name):
#         super().__init__()
#         self.drink_name = drink_name
#
# drink1 = Drink("soda")
# print(drink1.drink_name)
#
#
# class Animal:
#     def __init__(self, legs):
#         self.legs = legs
# class Cat(Animal):
#     def __init__(self, fur):
#         super().__init__()
#         self.fur = fur
# Meow = Cat("brown")
# print(Meow.fur) #prints "brown"



# food1 = food("pasta", "hot", 20, 5, 6)
# food2 = food("crab", "colf", 60, 4, 2)
# food3 = food("sandwich", "cold", 5, 5, 7)
# # print(food1.rate)
# # print(food2.dish_name)
# #
# # print(food.count)
# print(food.rate)
# print(food.count)
# print(f"All of the food has a rating of {food.rate} points! There are {food.count} dishes")

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, first_name, last_name, credits, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.credits = credits
        self.gpa = gpa
        Student.count = Student.count + 1
        Student.total_gpa = Student.total_gpa + gpa

    @classmethod
    def get_count(cls):
        return print(f"The number of students is {cls.count}")

    @classmethod
    def get_total_gpa(cls):
        return print(f"The total GPA is {cls.total_gpa}")

    @classmethod
    def get_average_gpa(cls):
        return print(f"The avergae GPA is {cls.total_gpa / cls.count}")

    @staticmethod
    def is_valid_last_name(last_name):
        valid_last_name = ["Smith", "Doe", "Apple"]
        return last_name in valid_last_name

student1 = Student("John", "Doe", 15, 4.0)
student2 = Student("Megan", "Fox", 12, 3.5)
print(Student.get_count())
print(Student.get_total_gpa())
print(Student.get_average_gpa())
print(Student.is_valid_last_name("Dan"))
#
# class Classroom:
#     count = 0
#     def __init__ (self, width, length, chair, desk  ):
#         self.width = width
#         self.length = length
#         self.chair = chair
#         self.desk = desk
#         Classroom.count = Classroom.count + 1
#     def get_count(self):
#         return self.count
#
# classroom1 = Classroom(10,15,20,25)
# print(classroom1.width)
# classroom1.get_count()
# print(classroom1.count)

a = [0,1,2,3,4,5]
print(a[1:4])