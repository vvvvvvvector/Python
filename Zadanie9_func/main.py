s = list(range(10))

only_even = list(filter(lambda i: i % 2 == 0, s))

print(only_even)

pow2 = list(map(lambda i: i*i, s))

print(pow2)

only_even_pow2 = list(filter(lambda i: i % 2 == 0, map(lambda x: x * x, s)))

print(only_even_pow2)