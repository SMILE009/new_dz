#TASK 3
# написати функцію, яка повертає n-e число фібоначчі. fibo(n):***return f  1->1, 2->1, 3->2, 4->3, 5->5, 6->8
########################################################################################################################
n = 6

def fibo(n):
    fib1 = 1
    fib2 = 1
    i = 2
    if n == 1 or n == 2:
        return 1
    else:
        while i < n:
            fib_sum = fib2 + fib1
            fib1 = fib2
            fib2 = fib_sum
            i += 1
        return fib_sum



def fibo_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

#print(fibo_recursive(n))
print(fibo(n))