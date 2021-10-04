def lrgst_factor(m):
    number = m
    factors = []

    for numbers in range(1, number + 1):
        if number % numbers == 0:                      
            factors.append(numbers)

    print(factors[-2])

lrgst_factor(80)