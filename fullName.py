def fullName(a, b):
    if(isinstance(a, str) and isinstance(b, str)):
        return a + " " + b
    else:
        return "not a string input"
