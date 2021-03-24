import os
print(os.getcwd());
print("Learning Python");

# Flow control
# IF - THEN - ELSE #
a = 25
b = 17
c = -4

if a > b or b > c:
    print("1 - A is smaller than B or B is greater than C")

if a < b or b < c:
    print("2 - A is smaller than B or B is greater than C")
else:
    print("3 - No condition is executed")

if a < b:
    print("4 - A is smaller than B")
elif b < c:
    print("5 - B is smaller than C")
elif c < a:
    print("6 - C is smaller than A")
else:
    print("7 - No condition is executed")


# ClASSES #
class BasicMath:
    def summing(self, a, b):
        return a+b
    def multiply(self, a, b):
        return a*b
    def raiseit(self, a, b):
        return a**b 
    
first_calc = BasicMath()
first_calc.summing(1,2)

second_calc = BasicMath()
second_calc.raiseit(4,5)

third_calc = BasicMath()
third_calc.multiply(2,3)

#Graph plotting
import  matplotlib.pyplot as plt
x = [5,8,10]
y = [12,16,6]
plt.title('line graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y)
plt.show()

# Loop - While
# Break - Terminates the loop by breaking the control.
# Continue - Continues by passing the control to start of the loop.
while True:
    print("what is your name")
    myname = input()
    print(myname)
    if myname == "Bye":
        break
    print("Thank You")

# Loop - FOR
for i in range(5):
    print(i)

for i in range(10,-1,-2):
    print(i)

# Modules
import random
for i in range(10):
    print(random.randint(i,10))

# Alternative way to import modules but not advisable way #
from random import.*
for i in range(10):
    print(random.randint(1,10))

# Importing sys module = sys.exit() is used to exit the code
import sys
while True:
    print("Type Exit to Exit")
    response = input()

    if response == "Exit":
        sys.exit()

    print('you typed ' + response + '.')

# positional parameter for print() function
print('Hello', end='')
print('World')
print('cat','dog','rat')
print('cat','dog','Mice',sep=',')