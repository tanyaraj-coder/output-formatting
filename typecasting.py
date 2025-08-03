'''
TYPECASTING IN PYTHON
Typecasting is the process of converting a variable from one type to another.
In Python, this can be done using built-in functions like int(), float(), str(), etc

THERE ARE FOUR MAIN TYPES OF TYPECASTING:
1. Implicit Typecasting: Automatically done by Python when converting a smaller data type to a larger data type.

2. Explicit Typecasting: Manually converting a data type using built-in functions.

3. User-defined Typecasting: Creating custom functions to convert data types.

4. Typecasting with Collections: Converting between different collection types like lists, tuples, sets, etc.
'''



#implicit type conversion : converts the datatype into another datatype automatically.
#users dont have to involve in this process
a=5
print(type(a))

b=23.0
print(type(b))

c=a+b
print(c)
print(type(c))

'''#Explici type conversion:it needs user involvement to convert the variables data type 
#into the required data type.

#example of type casting in python

int() : convert it to integer .
float():convert it to float.
str():convert it to string .'''

#python convert int to float 
a=3
n=float(a) #int to float
print(n)
print(type(n))

b=int(n)  #float to int
print(b)
print(type(b))

c=str(b)  #int to str
print(c)
print(type(c))

#find datatype of input in python
a="hello world"
b=10
c=11.22
d=("geeks","for","geeks")  #tuple
e=["geeks","for","geeks"]  #list
f={"geeks":1,"for":2,"geeks":3}   #dictionary

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))