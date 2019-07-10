 # Exercises, part 3 Conditional execution
 # https://www.py4e.com/html3/03-conditional
 # Exercis 3:

imp = input("Write Your score:\n")
try:
    score=float(imp)

    if score > 1:
        print("Bad score!")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except:
    print("Error, please enter numeric input")

input("Press Enter to terminate")

    

