
def str_converter(string):
    if string == "Male" or string == "male":
        return float(0)
    elif string == "Female" or string == "female":
        return float(1)
    else:
        return "Enter correct gender"


    
