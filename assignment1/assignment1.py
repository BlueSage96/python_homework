# Write your code here.
import string
#Task 1
def hello():
    helloStr = "Hello!"
    return helloStr

print(hello())

#Task 2
def greet(name):
    return(f"Hello, {name}!")

print(greet("Brittany"))

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
            return first ** second
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

#Task 5
def grade(*args):
    try:
        finalGrade = sum(args) / len(args)
        
        if finalGrade >= 90:
            return "A"
        
        if finalGrade >= 80 and finalGrade <= 89:
            return "B"
        
        if finalGrade >= 70 and finalGrade <= 79:
            return "C"
        
        if finalGrade >= 60 and finalGrade <= 69:
            return "D"
        
        if finalGrade < 60:
            return "F"
        
    except TypeError:
        return("Invalid data was provided.")
    
print(grade)

#Task 6
def repeat(string, count):
    newString = ""
    for c in range(count):
        c += 1
        newString = string * c
    return newString

print(repeat)

#Task 7
def student_scores(param, **scores):
    try:
        if param == "mean":
            scoreSum = sum(scores.values()) / len(scores.values())
            return scoreSum
        if param == "best":      
            bestStudent = max(scores, key=scores.get)
            return bestStudent
               
    except TypeError:
        return("Wrong keyword!")
    
print(student_scores)

#Task 8
def titleize(words):
    words = words.lower().split()
    firstWord = words[0].title() #capitalize first word

    #Array for filtering little words
    littleWords = ["a","on","an","the","of","and","is","in"]
    
    #result after splitting and filtering and concatenating
    result = ""
    for i, w in enumerate(words):  
        i += 1
        if i == 1:
            continue
        #Capitalize the last word no matter what
        if words.index(w) == len(words) -1:
            result += " " + w.capitalize()
            
            #filter out little words to keep as lowercase
        elif w in littleWords:
            result += " " + w
        else:
            #after filtering capitalize all other words
            result += " " + w.capitalize()
    return firstWord + result #concatenation

print(titleize)

#Task 9
def hangman(secret, guess):
    finalGuess = ""
    for s in secret:
        if s in guess:
            finalGuess += "" + s
        else:
            finalGuess += "_"
    return finalGuess
print(hangman)

#Task 10
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        # Rule 1: starts with vowel
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            index = 0

            # move through consonants
            while index < len(word):
                # special case: "qu"
                if word[index:index+2] == "qu":
                    index += 2
                elif word[index] not in vowels:
                    index += 1
                else:
                    break

            # split and rebuild
            result.append(word[index:] + word[:index] + "ay")

    return " ".join(result)
print(pig_latin)