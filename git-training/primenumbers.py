# A function that generates prime numbers from 0 to n

#import big_o


def is_prime(x):
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
        return True

def prime_numbers(n):

    print('2\n3')

    for i in range(5, n, 2):
        if is_prime(i):
            print(i)

print(prime_numbers(100))

# Asymptotic analysis

#positive_int_generator = lambda n: big_o.datagen.n_(10000)
#best, others = big_o.big_o(prime_numbers, positive_int_generator, n_repeats=100)

#print(best)


