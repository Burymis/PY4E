 # Exercises, part 2 Variables: from 2- 5
 # https://www.py4e.com/html3/02-variables
 # Exercis 2:

name = input("What is your name:\n")
print ("Hello "+name)


hours = input("Enter Hours:\n")
rate = input("Enter Rate: \n")

try:
    pay = float(hours) * float(rate)
except:
    print ("Please enter a number")
# add reconies if the user niput was word or coma    

print(pay)
input("Press Enter to terminate")
 
