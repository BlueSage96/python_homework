import pandas as pd

#Task 1#
# Uncomment print statements after all tests pass!
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
     'Age': [25,30,35],
     'City': ['New York', 'Los Angeles', 'Chicago']
}

#Convert to dataframe
task1_data_frame = pd.DataFrame(data)
print("\nIntial data: \n",task1_data_frame)

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
print("\nData with salaries: \n",task1_with_salary)
task1_older = task1_with_salary.copy()

#Increment age by 1
updated_task1_older = [26,31,36]
task1_older["Age"] = pd.Series(updated_task1_older)
print("\nIncremented ages by 1: \n",task1_older)
task1_older.to_csv("employees.csv", index=False)

#Task 2
task2_employees = pd.read_csv("employees.csv")
print("\nCSV employees: \n",task2_employees)
json_employees = pd.read_json("additional_employees.json")
print("\nJSON employees: \n",json_employees)

more_employees = pd.concat([task2_employees, json_employees],ignore_index=True)
print("\nCombined employees: \n",more_employees)

#Task 3
first_three = more_employees.head(3)
print("\n First three rows: \n",first_three)
last_two = more_employees.tail(2)
print("\nLast two rows: \n",last_two)

employee_shape = more_employees.shape
print("\n Employee shape: \n",employee_shape)
print("\n More employees info: \n")
more_employees.info()

#Task 4
dirty_data = pd.read_csv("dirty_data.csv")
print("\nInitial dirty data: \n",dirty_data)
clean_data = dirty_data.copy()

clean_data.drop_duplicates(inplace=True)
clean_data["Age"] = pd.to_numeric(clean_data["Age"], downcast="integer", errors="coerce")

#Replace unknown values
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"].replace(["unknown", "n/a"], pd.NA), errors="coerce")
median_salary = clean_data["Salary"].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)

fill_age = clean_data["Age"].mean()
clean_data["Age"] = clean_data["Age"].fillna(fill_age)

#convert Hire Date to Datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format="mixed")

#Strip whitespace & upper case
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print("\n Cleaned data: \n",clean_data)