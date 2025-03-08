def largestp(n):
    while n % 2 == 0:
        n //= 2
    
    factor = 3
    largest = 2
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2
    
    if n > 1:
        largest = n
    
    return largest

number = 600851475143
print(largestp(number))

