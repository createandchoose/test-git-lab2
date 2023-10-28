def power(n, m):
    if m == 0:
        return 1
    elif m > 0:
        result = 1
        for _ in range(m):
            result *= n
        return result
    else:
        return 1 / power(n, -m)

n = 2
m = 3
result = power(n, m)
print(f"{n} в степени {m} равно {result}")
