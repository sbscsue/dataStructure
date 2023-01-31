def pibo(value):
    if(value == 1):
        return 1 
    elif (value == 0):
        return 0
    else:
        return pibo(value-1) + pibo(value-2)


print(pibo(15))