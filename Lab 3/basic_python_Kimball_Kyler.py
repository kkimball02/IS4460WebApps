#this is a comment
##this is another comment


print("Hello World!")



print("hello class")

5+5

##literals
print("Thing") #this is an object type of string
print(3.14) #this is a number. Technically a float

##variable names
a = 5
b = 6
print(a+b)


#A = 6
#a = 5
#print(a)
#print(A)

##strings and variables +f string
student_gpa = 4.0
user_name = "kkimball20"
print(type(student_gpa))

print(student_gpa)
print(user_name)

print("My name is " + user_name + " not Ingo")
print("My name is {user_name}")

##converting between types and substrings
number = 145 * 17
print(str(number)+ " This is a string")

##add number function
def add_number(a,b):
  output = a + b
  return output
 
print(add_number(10, 10))

##say hello functions
def say_hi(a):
  print(a)

say_hi("hi")


name = "Bob"

def say_hello():
  name = "Matt"
  print(name)

say_hello()
print(name)

