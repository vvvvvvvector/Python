def print_gen(seq):
    for i in seq:
        print(i, end=' ')
    print()

# generator 1
def even(sequence):
    for i in sequence:
        if i % 2 == 0:
            yield i

gen1 = even(range(10))

print_gen(gen1)

# generator 2
def pow2(sequence):
    for i in sequence:
        yield i**2


gen2 = pow2(range(10))

print_gen(gen2)

# generator 3
def pow2_even(sequence):
    for i in sequence:
        if i**2 % 2 == 0:
            yield i**2

gen3 = pow2_even(range(10))

print_gen(gen3)
