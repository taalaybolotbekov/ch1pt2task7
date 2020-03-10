def number(): 
    n = int(input('vvedite chislo: '))
    if n>1: 
        return ("1")
    elif n<1:
        return("-1")
    elif n == 0 :
        return("0")
    else:
        return("error")
print(number())
