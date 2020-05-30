#ASSIGNMENT NO 5 ON EXCEPTIONS

print("--------------FILE HANDLING EXCEPTION--------------")
try:
    fh = open("testfile", "r")
    fh.write("This is my testfile!")
except IOError:
    print("Not able to write data in the file!")
else:
    print("Content written")
finally:
    print("File closed!")
    fh.close()
print("--------------ARITHMETIC EXCEPTION--------------")
i = input("Enter 1st number : ")
j = input("Enter 2nd number : ")
try:
    k = int(i) / int(j)
    print(k)
    print("inside try block before m")
    m = int(i) / int(j)
    print("Division : ")
    print(m)
    print("inside try block after m")
except(ZeroDivisionError):
    print("2nd number i.e. divisor is zero Hence no division possible")
except(TypeError):
    print("ip check")
except:
    print("except")
finally:
    m = int(i) * int(j)
    print("Multiplication : ")
    print(m)
print("outside try except finally block")
print("--------------ARGUMENT EXCEPTION--------------")


def convert1(var):
    try:
        print( int(var))
    except ValueError as Argument:
        print("Argument does not contain numbers.")

num=input("Enter a value : ")
convert1(num)

print("--------------USER DEFINED EXCEPTION----------------------------")
print("-------GUESS THE VALUE GAME-------")
class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is large"""
   pass


number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is small, Guess again!")
       print()
   except ValueTooLargeError:
       print("This value is large, Guess again!")
       print()

print("Congratulations! You guessed the number correctly.")
