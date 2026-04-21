import csv
#Task 3
def list_comprehensions(): 
    with open("../csv/employees.csv", "r") as file:
        reader = csv.reader(file)
        employees_list = [x for x in reader]

        employee_names = [
            y[1] + " " + y[2]
            for y in employees_list[1:]
        ]
        print(f"All employees: {employee_names} \n")
       
        employee_names_e = [
            xe for xe in employee_names 
            if "e" in xe]
        print(f"Only employees with e: {employee_names_e} \n")
        
list_comprehensions()     