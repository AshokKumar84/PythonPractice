#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, World!")


# In[20]:


def hello():
    print("Hello, World!")


# In[28]:


import time

def measure_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution Time: {end - start} seconds")
    return wrapper


# In[12]:


Hola = measure_time(hello)
Hola()


# In[30]:


#Decorators - The above code can be replaced with Decorators using @ operator.
# @measure_time code is equivalent to saying hello = measure_time(hello)
@measure_time
def hello():
    print("Hello, World!")
hello()


# In[31]:


from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


# In[32]:


@debug
def add(x, y):
    """Returns the sum of x and y"""
    return x + y

@debug
def greet(name, message="Hello"):
    """Returns a greeting message with the name"""
    return f"{message}, {name}!"

print(add(2, 3))
print(greet("Alice"))
print(greet("Bob", message="Hi"))

