def two_5(n):

    number=n
    digts=[]
    count=0
    while number>0:
        numbers=number%10
        
        digts.append(numbers)
        count=count+1
        number=number//10
    digts.reverse()    
    first = digts[0]
    for second in digts[1:]:
        if second == first:
            return True
        else:
            first = second
    return False
two_5(55055)