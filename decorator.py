from time import time

# In the beginning we need to know the spending time of calling a funcdtion add
# we do this
def version_1():
    def add(x, y=10):
        return x+y
    before = time()
    print(f"add(10): {add(10)}")
    after = time()
    print(f"time taken: {after - before}")

    before = time()
    print(f"add(20,30): {add(20,30)}")
    after = time()
    print(f"spending time: {after - before}")

    before = time()
    print(f"add('a', 'b'): {add('a', 'b')}")
    after = time()
    print(f"spending time: {after - before}")

# Then, we try to simplify it, like the following 
def version_2():
    def add(x, y=10):
        before = time()
        result = x + y
        after = time()
        print(f"spending time: {after - before}")
        return result
    print(f"add(10): {add(10)}")
    print(f"add(20,30): {add(20,30)}")
    print(f"add('a','b'): {add('a', 'b')}")


# Here comes a problem, what if we need another function sub now?
# we have do write before, after, spening time .....
# still complicated
def version_3():
    def sub(x, y=10):
        before = time()
        result = x - y
        after = time()
        print(f"spending time: {after - before}")
        return result

# then we pack it like this
def version_4():
    def timer(func, x, y=10):
        before = time()
        result = func(x,y)
        after = time()
        print(f"spending time: {after - before}")
        return result

    def add(x, y=10):
        return x+y
    
    def sub(x, y=10):
        return x-y
    
    print(f"add(10): {timer(add, 10)}")
    print(f"add(20,30): {timer(add, 20, 30)}")
    print(f"sub(20,10): {timer(sub, 20, 10)}")

# still annoying, 
def version_5():
    def timer(func):
        def wrapper(x, y=10):
            before = time()
            result = func(x, y)
            after = time()
            print(f"spending time: {after - before}")
            return result
        return wrapper

    def add(x, y=10):
        return x+y
    add = timer(add) # like a pointer

    def sub(x, y=10):
        return x-y
    sub = timer(sub)

    print(f"add(10,20): {add(10,20)}")
    print(f"sub(10,20): {sub(10,20)}")

# Looks good, but still have a problem
# what if function in wrapper could have different types of arguments
# so we replace x and y with *args and **kwargs
def version_6():
    def timer(func):
        def wrapper(*args, **kwargs):
            print(f"args: {args}, kwargs: {kwargs}")
            before = time()
            result = func(*args, **kwargs)
            after = time()
            print(f"spending time: {after - before}")
            return result
        return wrapper

    def add(x, y=10):
        return x+y
    add = timer(add) # like a pointer

    def sub(x, y=10):
        return x-y
    sub = timer(sub)

    print(f"add(10,20): {add(10,20)}")
    print(f"sub(10,20): {sub(10,20)}")


# In version_6, timer is actually a decorator, it accepts a function and returns a funcdtion
# inside the decorator, it encapsulates the origin function
# the following example is where we apply decorator
"""
def add(x, y=10):
    return x+y
add = timer(add) # <- notice here
"""
# in the example, if we rename the function, we've got 3 places to modify
# as a lazy software engineer, we use Syntactic sugar @
def version_7():
    def timer(func):
        def wrapper(*args, **kwargs):
            before = time()
            result = func(*args, **kwargs)
            after = time()
            print(f"spending time: {after - before}")
            return result
        return wrapper
    
    @timer
    def add(x, y=10):
        return x+y

    @timer
    def sub(x, y=10):
        return x-y

    print(f"add(10,20): {add(10,20)}")
    print(f"sub(10,20): {sub(10,20)}")

# version_1()
# version_2()
# version_4()
# version_5()
# version_6()
version_7()