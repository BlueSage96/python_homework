# Write your code here.
#Task 1
def hello():
    helloStr = "Hello!"
    return helloStr

print(hello)

#Task 2
def greet(name):
    return(f"Hello, {name}!")

print(greet)

#Task 3
def calc(first, second, calculate = "multiply"):
    try:
        match calculate:
           case "add":
            return first + second 
           case "divide":
            return first / second
           case "subtract":
            return first - second
           case "modulo":
            return first % second 
           case "int_divide":
            return int(first/second)
           case "power":
            return first ^ second
           case _:
            return first * second
        
    except ZeroDivisionError:
        return("You can't divide by 0!")
    
    except TypeError:
        return("You can't multiply those values!")
    
print(calc)

#Task 4
def data_type_conversion(value, name):
    try:
        match name:
            case "int":
                return (int(value))
        
            case "float":
                return (float(value))

            case "str":
                return (str(value))
        
    except ValueError:
        return (f"You can't convert {value} into a {name}.")
    
print(data_type_conversion)