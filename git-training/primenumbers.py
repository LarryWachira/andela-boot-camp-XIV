# A function that generates prime numbers from 0 to n

def prime_numbers(n):

    for a in range(2, n):
        prime = True

        for b in range(2, a):
            if a % b == 0:
                prime = False

        if prime:
            print(a)


