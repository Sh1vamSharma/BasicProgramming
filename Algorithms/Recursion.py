from util import time_it

#@time_it
def find_sum2(number):
    sum = 0
    for i in range(1, number+1):
        sum += i
    return sum
#@time_it
def find_sum(number):
    # base condition for getting out of recursion
    if number == 1:
        return 1
    return number + find_sum(number-1)

def rec_fibo(nterms):
    if nterms <= 1:
        return 1
    return (rec_fibo(nterms-1) + rec_fibo(nterms-2))
    

def fibo(nterms):
    # Program to display the Fibonacci sequence up to n-th term
    # first two terms
    n1, n2 = 0, 1
    count = 0
    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence upto", nterms, ":")
        while count < nterms:
            print(n1,end=', ')
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

if __name__ == "__main__":
    
    print(find_sum(5))
    print(find_sum2(5))

    n = int(input("How many terms? : "))
    fibo(n)
    print()
    for i in range(n):
        print(rec_fibo(i), end=', ')
