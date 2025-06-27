print("Hello World!")   
name = "Mahek"
age = 22
price = 25.99

#assigning age to another variable
age2 = age 

#printing variables
print("My name is : ",name)
print("My age is: ", age)
print(age2)
print(price)

#datatypes
print(type(name))
print(type(age))
print(type(price))

#example of datatype boolean and none
age = 23
old = True
a = None
print(type(old))
print(type(a))

#example of sum
a = 1000
b = 200
sum = a + b
print("The sum of a and b is: ", sum)

#arithmetic operators
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder
print(a**b) #A^B
print(a//b)


#relational operators
a= 50
b = 20
print(a==b) #equal to
print(a!=b) #not equal to
print(a>b) #greater than
print(a<b) #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to


#assignment operators
num = 10
num += 10 #same as above
num -= 5 #num = num - 5
num *= 2 #num = num * 2
num /= 2 #num = num / 2
num %= 3 #num = num % 3
num **= 2 #num = num ** 2
num //= 2 #num = num // 2
print("num : ",num)


#logical operators
a = 60
b = 40
print(not False)
print(not True)
print(not(a < b))

val1 = True
val2 = False
print("and operatoe: ", val1 and val2)
print("or operator: ", val1 or val2)

print("OR operator :", (a==b) or (a>b))
print("AND operator :", (a==b) and (a>b))


#type conversion
a = 2
b = 4.25

print(type(a))
sum = a + b
print(sum)

#type casting
a = float("2")
b = 4.25

print(type(a))
print(a + b)


# Example of input function

name = input("Enter your name: ")
print("Welcome", name)
age = input("Enter your age: ")
print(age)

val = int(input("Enter some value: "))
print(type(val), val)  
val = float(input("enter some value:"))
print(type(val), val)