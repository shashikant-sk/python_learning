# WAP to find out the prime factors of a number entered through keyboard (distinct). /*Hints: A prime number is any number with no divisors other than itself and 1, such as 2 and 5. Any number can be written as a product of prime numbers in a unique way (except for the order). These are called prime factors of a number. In other words, In number theory, the prime factors of a positive integer are the prime numbers that divide that integer exactly, without leaving a remainder. The process of finding these numbers is called integer factorization, or prime factorization. • Enter a number : 100  • The prime factors of 100 are 2(2) and 5(2) • That is, 100 = 2 x 2 x 5 x 5, and those numbers are primes.

def primeFactors(n):
    num = 2
    while num <= n:
        if n % num == 0:
            print(num)
            n = n / num
        else:
            num = num + 1

n = int(input("Enter number to find prime factors: "))
primeFactors(n) 

