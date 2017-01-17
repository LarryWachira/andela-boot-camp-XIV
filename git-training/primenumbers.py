# A function that generates prime numbers from 0 to n

import big_o


def prime_numbers(n):
    print('2\n3')

    def is_prime(x):
        if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
            return True

    for i in range(5, n, 2):
        if is_prime(n):
            print(i)

print(prime_numbers(n))

# Asymptotic analysis

positive_int_generator = lambda n: big_o.datagen.n_(10000)
best, others = big_o.big_o(prime_numbers, positive_int_generator, n_repeats=100)

print(best)


