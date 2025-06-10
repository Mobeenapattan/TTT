# a = 5
# b=8
# if(a > b):
#     print("a is greater")

# else:
#     print("b is greater")    



# a=int(input("enter a element:"))
# b=int(input("enter b element:"))
# c=int(input("enter c element:"))
# if(a > b and a>c):
#     print("a is greater")
# elif(b>c):
#     print("b is greater")
# else:
#     print("c is greater")



#mark1=int(input("enter mark1 element:"))
# if(mark1>=90):
#     print("grade A+")
# elif(mark1>=80 and mark1<90):
#     print("grade B")
# elif(mark1>=70 and mark1<60):
#     print("grade c")
# else:
#     print("grade d")



# marks = int(input("Enter marks : "))

# if (marks >= 0 and marks <= 100):
#     if (marks >= 90):
#         print("Grade: A")
#     elif (marks >= 75):
#         print("Grade: B")
#     elif (marks >= 60):
#         print("Grade: C")
#     else:
#         print("Grade: D or Fail")
# else:
#     print("Invalid marks entered.")


# for i in range(5):
#     print(i)


# count = 1
# while count <= 5:
#     print("Count is:", count)
#     count += 1


# right angled triangle
# rows = 5
# for i in range(1, rows + 1):
#     print('*' * i)

# print("-------------")


# # inverted triangle
# rows = 5
# for i in range(rows, 0, -1):
#     print('*' * i)


# print("------------------")

# name="mobeena"
# for i in range(1,len(name)+1):
#     print(name[ :i])


from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # No implementation here

# Child class must implement the abstract method
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Cannot create object of abstract class
# shape = Shape()  ❌ Error

circle = Circle(5)
print("Area of circle:", circle.area())

