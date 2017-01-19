# A function that generates prime numbers from 0 to n

#import big_o


def is_prime(n):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        return True

def prime_numbers(n):
    if n > 0:
        if n == 1: return 'one is special'
        elif n == 2: print("2")
        elif n == 3: print('2\n3')
        elif n == 5: print("2\n3\n5")
        else:
            print('2\n3\n5')
            for i in range(7, n+1, 2):
                if is_prime(i):
                    print(i)

print(prime_numbers(100))

# Asymptotic analysis

'''positive_int_generator = lambda n: big_o.datagen.n_(10000)
best, others = big_o.big_o(prime_numbers, positive_int_generator, n_repeats=100)

print(best)'''


