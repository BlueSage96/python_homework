import traceback
import csv
#Task 1
def diary():
    with open("diary.txt", "a") as file:
      try:
        prompt1 = input("What happened today? \n")
        file.write(prompt1 + "\n")  
        prompt2 = ""
        
        while prompt1 != "done for now" and prompt2 != "done for now":
            prompt2 = input("What else? \n") 
            file.write(prompt2 + "\n") 
            
        else:
            file.close()
            
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
    employeeDict = {}
    employeeList = []
    
    with open("../csv/employees.csv", "r") as file:
        try:
            reader = csv.reader(file)
            #first line goes to "fields"
            for i, row in enumerate(reader):
                if i == 0:
                    employeeDict["fields"] = row
                else:
                    employeeList.append(row)
                    employeeDict["rows"] = employeeList

            return employeeDict
        except Exception as e:
            print(f"An exception has occurred: {e}")
    
#calls function and stores the returned value
employees = read_employees()