def uniq_digits(x):

    number=x
    digts=[]
    count=0
    while number>0:
        numbers=number%10
        
        digts.append(numbers)
        count=count+1
        number=number//10
    digts.reverse()    
 
    a_set = set(digts)
    unique_digit_num = len(a_set)
    print(unique_digit_num)

uniq_digits(8675309)
uniq_digits(1313131)