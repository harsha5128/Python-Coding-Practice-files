def reverse_integer(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if x < 0:
        sign = -1
        x = abs(x)
    else:
        sign = 1
    
    reversed_num = 0
    while x != 0:
        pop = x % 10
        x //= 10
        if reversed_num > (INT_MAX - pop) // 10:
            return 0
        reversed_num = reversed_num * 10 + pop
    
    return sign * reversed_num


x=487
result = reverse_integer(x)

print(result)