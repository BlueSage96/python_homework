
import pandas as pd
#Task 1

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
     'Age': [25,30,35],
     'City': ['New York', 'Los Angeles', 'Chicago']
}

#Convert to dataframe
task1_data_frame = pd.DataFrame(data)
# print(task1_data_frame)

#save to file
task1_data_frame.to_csv("task1.csv")

#copy and add salary
task1_with_salary = task1_data_frame.copy()
data = {
     'Name': ['Alice', 'Bob', 'Charlie'],
     'Age': [25,30,35],
     'City': ['New York', 'Los Angeles', 'Chicago'],
     'Salary': [70000,80000,90000]
}

task1_with_salary = pd.DataFrame(data)
# print(task1_with_salary)
task1_older = task1_with_salary.copy()

#Increment age by 1
updated_task1_older = [26,31,36]
task1_older["Age"] = pd.Series(updated_task1_older)
# print(task1_older)
task1_older.to_csv("employees.csv", index=False)

#Task 2
task2_employees = pd.read_csv("employees.csv")
# print(task2_employees)
json_employees = pd.read_json("additional_employees.json")
# print(json_employees)

more_employees = pd.concat([task2_employees, json_employees],ignore_index=True)
# print(more_employees)

#Task 3

#Task 4
#Uncomment print statements after all tests pass!