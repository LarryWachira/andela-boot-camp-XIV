# A function that generates prime numbers from 0 to n

import big_o

def prime_numbers(n):

    for a in range(2, n):
        prime = True

        for b in range(2, a):
            if a % b == 0:
                prime = False

        if prime:
            print(a)

# Asymptotic analysis

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(prime_numbers, positive_int_generator, n_repeats=100)

print(best)


