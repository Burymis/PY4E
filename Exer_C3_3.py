 # Exercises, part 3 Conditional execution
 # https://www.py4e.com/html3/03-conditional
 # Exercis 3:

def grade(score):
    try:
        score = float(score)

        if score > 1:
            user_grade = "Bad score!"
        elif score >= 0.9:
            user_grade = "A"
        elif score >= 0.8:
            user_grade = "B"
        elif score >= 0.7:
            user_grade = "C"
        elif score >= 0.6:
            user_grade = "D"
        else:
            user_grade = "F"
    except:
        user_grade = "Bad score!"
    return user_grade

inp = input("Write Your score:\n")
print(grade(inp))

input("Press Enter to terminate")

    

