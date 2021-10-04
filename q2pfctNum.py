def pfct_num(m):
    sum = 0
    for x in range(1, m):
        if m % x == 0:
            sum += x
    return sum == m
print(pfct_num(28))

