def add(*arg):
    if(len(arg)>15):
       print("this is another easter")
       return "Error: > 15 values"
    
    if(len(arg) > 10):
        print("Error >10 values given!")
        return "Error: >10 Values"
    
    print("Adding",len(arg),"numbers")
    result = 0
    for n in arg:
        result = result + n

    print("Add result is", result)
    return result

def subtract(*arg):
    if(len(arg) > 10):
        print("Error >10 values given!")
        return "Error: >10 Values"
    print("Subtracting",len(arg),"numbers")
    result = arg[0]
    for n in range(1, len(arg)):
        result = result - arg[n]

    print("Subtract result is", result)
    return result

def multiply(*arg):
    if(len(arg) > 10):
        print("Error >10 values given!")
        return "Error: >10 Values"
    print("Multipling",len(arg),"numbers")
    result = arg[0]
    for n in range(1, len(arg)):
        result = result * arg[n]

    print("Multiply result is", result)
    return result

def divide(*arg):
    if(len(arg) > 10):
        print("Error >10 values given!")
        return "Error: >10 Values"
    print("Dividing", len(arg),"numbers")
    
    result = arg[0]
    try:
        for n in range(1, len(arg)):
            result = result / arg[n]

        print("Divide result is", result)
        return result
    except ZeroDivisionError:
        print("Division by Zero Error at number", n+1)
        return ZeroDivisionError

    


  
