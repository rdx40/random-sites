def sum_multiples(limit):
    return sum(x for x in range(limit) if x%3 == 0 or x%5 == 0)
print(sum_multiples(1000))
