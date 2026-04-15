import traceback
import csv
import os
import custom_module
from datetime import datetime

#Task 1
def diary():
    with open("diary.txt", "a") as file:
      try:
        prompt1 = input("What happened today? \n")
        file.write(prompt1 + "\n")  
        prompt2 = ""
        
        while prompt2 != "done for now":
            prompt2 = input("What else? \n")
            if prompt2 != "done for now":
                file.write(prompt2 + "\n")
                    
      except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}")
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
        if message:
            print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
diary()

#Task 2
def read_employees():
    employee_dict = {}
    employee_list = []
    
    with open("../csv/employees.csv", "r") as file:
        try:
            reader = csv.reader(file)
            #first line goes to "fields"
            employee_dict["rows"] = employee_list
            for i, row in enumerate(reader):
                if i == 0:
                    employee_dict["fields"] = row
                else:
                    employee_list.append(row)
                  
            return employee_dict
        except Exception as e:
            print(f"An exception has occurred: {e}")
    
#calls function and stores the returned value
employees = read_employees()

#Task 3
def column_index(index):
    return employees["fields"].index(index)
employee_id_column = column_index("employee_id")

#Task 4
def first_name(rowNum):
    col = column_index("first_name")
    return employees["rows"][rowNum][col]

first_name(1)

#Task 5
def employee_find(employee_id):
    def employee_match(row):
        #returns true if there's a match
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return list(matches)

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"]))
    return matches

#Task 7
def sort_by_last_name():
    #sort rows stored in the dict
    employees["rows"].sort(key = lambda row: row[column_index("last_name")])
    return employees["rows"]

sort_by_last_name()

#Task 8
def employee_dict(row):
    em_dict = {}
    for r in range(1, len(row)):
      #skips index 0
      key = employees["fields"][r]
      value = row[r]
      em_dict[key] = value
    return em_dict

single_employee_dict = employee_dict(employees["rows"][0])

#Task 9
def all_employees_dict():
    em_dict = {}
    row = employees["rows"]
    for r in row:
      key = r[0]
      value = employee_dict(r)
      em_dict[key] = value
    return em_dict

all_employees_dict()

#Task 10
def get_this_value():
     return os.environ.get("THISVALUE")
 
 #Task 11
def set_that_secret(secret):
    custom_module.set_secret(secret)

set_that_secret("secret")
print(custom_module.secret)

#Task 12
def read_dict(file_path):
    minute_dict = {}
    
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        fields = next(reader) #first row
        rows = []
        
        for row in reader:
           rows.append(tuple(row))
        minute_dict["fields"] = fields
        minute_dict["rows"] = rows
    return minute_dict

def read_minutes():
    mins1 = read_dict("../csv/minutes1.csv")
    mins2 = read_dict("../csv/minutes2.csv")
    return mins1, mins2

minutes1, minutes2 = read_minutes()

#Task 13
def create_minutes_set():
    min1, min2 = read_minutes()  
    min1_set = min1["rows"]
    min2_set = min2["rows"]
    minutes_set = {}
    
    minutes_set = set(min1_set + min2_set)
    return minutes_set

minutes_set = create_minutes_set()

#Task 14
def create_minutes_list():
    minutes_list = list(minutes_set)
    new_mins_list = list(
        map(lambda x: (x[0], datetime.strptime(x[1],"%B %d, %Y" )), minutes_list)
    )
    return new_mins_list

minutes_list = create_minutes_list()

#Task 15
def write_sorted_list():
    sorted_minutes_list = sorted(minutes_list, key=lambda x: x[1])

    new_mins_list = list(
        map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_minutes_list)
    )

    mins1, mins2 = read_minutes()  # unpack properly

    with open("minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(mins1["fields"])  # header

        for row in new_mins_list:
            writer.writerow(row)

    return new_mins_list
