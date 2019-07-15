 # Exercises, part 5 Iteration
 # https://www.py4e.com/html3/05-iterations
 # Exercis 1->2:


count = 0
total = 0
min_numb = None
max_numb = None

while True:
    imp=input("Enter a number: ")
    if imp == "done":
        break
    try:
        imp_numb=float(imp)
    except:
        print("Invalid input")
        continue
    if min_numb == None or imp_numb < min_numb: #store the min value
        min_numb = imp_numb
        
    if max_numb == None or imp_numb > max_numb: #store the max value
        max_numb = imp_numb
    
    count = count +1
    total = total + imp_numb
    average  = total/count
    print("trial: ", count," Total: ", total, " average: ", average)
    
print("Final score:")
print("Trials: ", count," Total: ", total, " Average: ", average)
print("Min value: ", min_numb," Max value: ", max_numb)


