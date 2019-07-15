 # Exercises, part 5 Iteration
 # https://www.py4e.com/html3/05-iterations
 # Exercis 1:


count = 0
total = 0



while True:
    imp=input("Enter a number: ")
    if imp == "done":
        break

    try:
        imp_numb=float(imp)
    except:
        print("Invalid input")
        continue
                             
    count = count +1
    total = total + imp_numb
    average  = total/count
    print("trial: ", count," Total: ", total, " average: ", average)
    
print("End sccor: \n")
print("Trials: ", count," Total: ", total, " Average: ", average)    


