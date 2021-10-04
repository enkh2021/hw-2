def same_ord(a, b):
    while (a > 0 and b > 0):
        a = a // 10;
        b = b // 10;
 
    
    if (a == 0 and b == 0):
        print(True);
    else:
        print(False);
same_ord(50, 100)




