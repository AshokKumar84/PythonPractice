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
#from random import.*
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

# Local Variables Cannot Be Used in the Global Scope
def spam():
    eggs = 100
    print("Local - " + str(eggs))

spam()
print("Global - " + str(eggs)) #Fails as it is under Global Variable scope

# Local Scopes Cannot Use Variables in Other Local Scopes
def spam():
    eggs = 100
    bacon()
    print("Spam Local - " + str(eggs))

def bacon():
    hamm = 20
    eggs = 0    # eggs = 0 is not printed as it is local to bacon() function

spam()

# Global Variables Can Be Read from a Local Scope
def spam_1():
    print("Spam Local - " + str(eggs))
eggs = 50   #Global variable declared - Can be used in local and global scope

spam_1()
print("Global - " + str(eggs))

# Local and Global Variables with the Same Name
def spam():
    eggs = "Spam Local"
    print(eggs)

def bacon():
    eggs = "Bacon Local"
    print(eggs)     # prints bacon local
    spam()          # prints spam local
    print(eggs)     # prints bacon local

eggs = "Global"
bacon()
print(eggs)         # prints global

# The global Statement
def spam():
    global eggs     # Global variable declared
    eggs = "spam"

eggs = "Global"
spam()
print(eggs)

# To explain Local and Global scope in more detail
def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)


def spam():
    print(eggs) # ERROR! - This is a local variable referenced before assignment
    eggs = 'spam local'

eggs = 'global'
spam()

# Exception Handling
def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(10))
print(spam(0))
print(spam(50))


# Exception Handling - Stops running the code at the error point because once the execution jumps to except block it never return back
def spam(divideBy):
    return 42/divideBy

try:
    print(spam(2))
    print(spam(10))
    print(spam(0))
    print(spam(50))
except ZeroDivisionError:
    print('Error: Invalid argument.')


# List Data Types
spam = ['cat','rat','dog','elephant']
print(spam)

# Cascading Lists
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0]
spam[1]
spam[0][1]
spam[1][4]

# Index using Negative Integers (-1 as last, -2 as second last, etc)
spam = ['cat', 'bat', 'rat', 'elephant','Tiger']
spam[-1]
spam[-3]
spam[-5]

# Index - Single value from the list
# Slice - Several value from the list
spam[1:4]
spam[0:-1]
spam[1:-2]
spam[:2]
spam[1:]
spam[:]
len(spam)

# chaning values in list using index
spam[1] = "dog"
spam
spam[-1] = "Whale"
spam
spam[2] = spam[1]
spam

# List concatenation and Replication
[1,2,3] * 3
[1,2,3] + ['A','B','C']

# Removing values from the list using del statements
spam = ['cat', 'bat', 'rat', 'elephant','Tiger']
del spam[3]     # Delete the element from the list
spam

# FOR loop in list
for i in range(4):
    print(i)

# Technically - For loop does
for i in [0,1,2,3]:
    print(i)

# Excercise
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for index in range(len(supplies)):
    print('Index ' + str(index) + ' Supplies ' + supplies[index])


# IN and NOT-IN operator
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
'cat' in ['hello', 'hi', 'howdy', 'heyas']

'howdy' not in ['hello', 'hi', 'howdy', 'heyas']
'cat' not in ['hello', 'hi', 'howdy', 'heyas']

# The Multiple Assignment Trick
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size)

cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(color)

# Methods - Same as function except it is called on by Values
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')     # 'Hello' - is a value
spam.index('howdy')

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.index('Pooka')     # Retunrs the index of first value

# Adding values to list
spam.append('mouse')
spam

# deleting  values from list based on index
del spam[1]
spam

# removing values from the list
spam.remove('mouse')
spam

# insert method can insert at any position in the list
spam.insert(1,'chicken')
spam

# Sort the values in the list
spam.sort()
spam

spam.sort(reverse=True)
spam

# Sort the value in regular alphabetical order
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam    

# Strings
name = 'Zophie'
name[0]     # To display string values
name[-2]
name[0:4]
for i in name:
    print ('***' +i+ '***')

# List is mutable whereas Strings are Immutable
name = 'Zophie a cat'
name[7] = 'the'     # This is Immutable
name

name = 'Zophie a cat'
newName = name[0:7] + 'the ' + name[9:12]
newName

# Tuple data type
# Tuple is almost identical to list data type except tuples are typed with in parentheses instead of square brackets.
eggs = ('hello',4,0.2)
eggs[0]
eggs[1:3]
len(eggs)

# Tuples are like Strings. They are Immutable.
eggs[1] = 10    # Throws an error as they are immutable

# Tuple is faster than list
type(('hello',))       # Tuple
type(('hello'))        # Str

# Converting data types - List to Tuple and Tuple to List
tuple(['hello', 10, 0.5 ])      # Converts List to Tuple  
list(('hello',10,0.5))          # Converts Tuple to List
list('hello')                   # Converting Tuple to list to make it Mutable


# Chaning the List reference value will also change the value of List
spam = [1,2,3,4,5]
spam
cheese = spam
cheese
cheese[1] = 'hello'     # Changing the value of list reference 
spam
spam[0] = 'world'       # Changing the list also change the reference value
spam
cheese

# Passing references
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3,4,5]
eggs(spam)
print(spam)

# copy() and deepcopy() function
import copy
spam = [1,2,3,4,5]
cheese = copy.copy(spam)    # Creates a seperate copy not the reference
cheese[1] = 'Hello'
spam
cheese

# Excercise
spam = ['a','b','c','d']
spam[-1]
spam[:2]
spam[int(int('3' * 2) / 11)]

bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat')
bacon.append(99)
bacon.remove('cat')
bacon

# Dictonaries

