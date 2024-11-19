'''
""" Practicle based on simple statement using Arithmetic Operation"""

a = 50
b = 60
c = 10
d = 10
print("Sum of a and b is :", a + b)
print("Substraction of a and b is :" , a - b)
print("multiplecation of a and b is : " , a * b)
print('Division of a and b : ', a / b)
print('Greater than a and b :',a<b)
print('Less than a and b :',a>b)
print('Number is equal a and b :',c==d)
print('a Module b :',a%b)


        Class And  Object Program

# define a class
class Bike:
    name = ""
    gear = 0

# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

OUTPUT:-Name: Mountain Bike, Gears: 11


        Program For Filter Function

# Python filter() function example    
def filterdata(x):    
    if x>5:    
        return x    
# Calling function    
result = filter(filterdata,(1,2,6))    
# Displaying result    
print(list(result))    

OutPut:-
[6]
'''
a=5
for i in range(0,a):
    print (i)

cout=0
while(cout<5):
    cout=cout+1
    print("flexible")

