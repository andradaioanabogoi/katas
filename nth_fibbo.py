# Memoization ensures that a function doesn't run for the same inputs more than once by
#  keeping a record of the results for the given inputs (usually in a dictionary).

# Example of bottom up (going from base case to end, instead of recursion)

# def product_1_to_n(n):
#     # We assume n >= 1
#     result = 1
#     for num in range(1, n + 1):
#         result *= num

#     return result


class Fibo(object):
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise IndexError("Index was negative")
        if n in [0, 1]:
            return n
        if n in self.memo:
            return self.memo[n]

        result = self.fib(n-1) + self.fib(n-2)

        self.memo[n] = result
        return result


def bottom_up_fibo(n):
    if n < 0:
        raise IndexError("Index cannot be negative")
    if n in [0, 1]:
        return n

    a = 0
    b = 1

    for _ in range(n-1):
        current = a + b
        a = b
        b = current
    return current


print(Fibo().fib(5))
print(Fibo().fib(9))

print(bottom_up_fibo(5))
print(bottom_up_fibo(9))
