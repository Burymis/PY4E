 # Exercises, part 2 Variables: from 2- 5
 # https://www.py4e.com/html3/02-variables
 # Exercis 2->Exrcies 6: from part 4.


def pay_rate(hours,rate):
    pay = hours * rate
    return pay
    
name = input("What is your name:\n")
print ("Hello "+name)

try:
    priv_hours = float(input("Enter Hours:\n"))
    priv_rate = float(input("Enter Rate: \n"))  
    priv_pay = pay_rate(priv_hours,priv_rate)
    print(priv_pay)
except:
    print ("Please enter a number")
# add reconies if the user niput was word or coma    

input("Press Enter to terminate")
 
