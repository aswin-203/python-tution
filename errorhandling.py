# Python Exception Handling allows a program to gracefully handle unexpected events (like invalid input or missing files) without crashing. Instead of terminating abruptly


# Difference Between Errors and Exceptions
# Errors and exceptions are both issues in a program, but they differ in severity and handling. Let's see how:

# Error: Serious problems in the program logic that cannot be handled. Examples include syntax errors or memory errors.
# Exception: Less severe problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).

# num =int(input("enter a number: "))

# try: 
#   result = num / 0
#   print(result)
# except ZeroDivisionError:
#   print('can not divide a number by zero')


# try:
#       # Code 
# except SomeException:
#       # Code 
# else:
#      # Code 
# finally:
#     # Code 




# try: Runs the risky code that might cause an error.
# except: Catches and handles the error if one occurs.
# else: Executes only if no exception occurs in try.
# finally: Runs regardless of what happens useful for cleanup tasks like closing files.


# try:
#     # n = int('a')
#     n = 2
#     res = 100 / n
    
# except ZeroDivisionError:
#     print("You can't divide by zero!")
    
# except ValueError:
#     print("Enter a valid number!")
    
# else:
#     print("Result is", res)
    
# finally:
#     print("Execution complete.")



# try:
#   n = int(input('enter an number: '))
#   res = 100/n
# except (ZeroDivisionError , ValueError) as e:
#   print("Error: ",e )

# else:
#   print("Result: " , res)



# try:
#   n = int(input('Enter an number: '))
#   res = 100 / n
# except:
#   print('Something went wrong!')
# else:
#   print('Result: ' , res)



# def set(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     print(f"Age set to {age}")

# try:
#     set(-5)
# except ValueError as e:
#     print(e)


# def set(age):
#   if age < 0:
#     raise ValueError("Age cannot be negative.")
#   print("your age is ",age)

# try:
#   age = int(input('Enter your age'))
#   set(age)
# except ValueError as e:
#   print('you cant enter an minus number')
# else:
#   if age > 21:
#     print('you can enter the club')
#   else:
#     print('you are not old enough')



# Advantages
# Below are some benefits of using exception handling:

# Improved reliability: Programs don’t crash on unexpected input.
# Separation of concerns: Error-handling code stays separate from business logic.
# Cleaner code: Fewer conditional checks scattered in code.
# Helpful debugging: Tracebacks show exactly where the problem occurred.
# Disadvantages
# Exception handling have some cons as well which are listed below:

# Performance overhead: Handling exceptions is slower than simple condition checks.
# Added complexity: Multiple exception types may complicate code.
# Security risks: Poorly handled exceptions might leak sensitive details.


# ArithmeticError	Raised when an error occurs in numeric calculations
# AssertionError	Raised when an assert statement fails
# AttributeError	Raised when attribute reference or assignment fails
# Exception	Base class for all exceptions
# EOFError	Raised when the input() method hits an "end of file" condition (EOF)
# FloatingPointError	Raised when a floating point calculation fails
# GeneratorExit	Raised when a generator is closed (with the close() method)
# ImportError	Raised when an imported module does not exist
# IndentationError	Raised when indentation is not correct
# IndexError	Raised when an index of a sequence does not exist
# KeyError	Raised when a key does not exist in a dictionary
# KeyboardInterrupt	Raised when the user presses Ctrl+c, Ctrl+z or Delete
# LookupError	Raised when errors raised cant be found
# MemoryError	Raised when a program runs out of memory
# NameError	Raised when a variable does not exist
# NotImplementedError	Raised when an abstract method requires an inherited class to override the method
# OSError	Raised when a system related operation causes an error
# OverflowError	Raised when the result of a numeric calculation is too large
# ReferenceError	Raised when a weak reference object does not exist
# RuntimeError	Raised when an error occurs that do not belong to any specific exceptions
# StopIteration	Raised when the next() method of an iterator has no further values
# SyntaxError	Raised when a syntax error occurs
# TabError	Raised when indentation consists of tabs or spaces
# SystemError	Raised when a system error occurs
# SystemExit	Raised when the sys.exit() function is called
# TypeError	Raised when two different types are combined
# UnboundLocalError	Raised when a local variable is referenced before assignment
# UnicodeError	Raised when a unicode problem occurs
# UnicodeEncodeError	Raised when a unicode encoding problem occurs
# UnicodeDecodeError	Raised when a unicode decoding problem occurs
# UnicodeTranslateError	Raised when a unicode translation problem occurs
# ValueError	Raised when there is a wrong value in a specified data type
# ZeroDivisionError	Raised when the second operator in a division is zero



# nameError
# print(a)


# if 10< 20:
#   print('yes')




# indexError
# names = ['aswin', 'sam' , 'gopal']
# print(names[3])