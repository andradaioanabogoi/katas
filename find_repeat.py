# INTEGER OVERFLOW
# in case of an integer overflow: Python will automatically allocate space for a larger numbers
# in Java/C the processor would take the real result and truncate it to fit 64bits/32bits etc
# We can reduce likelihood (in Java/C) by using larger integer types: long long
# OR use libraries desgned for this

# O(n) running time and O(1) additional space


def find_repeat(list_numbers):
    if(len(list_numbers) < 2):
        raise ValueError("Finding duplicate requires at least 2 numbers")

    sum_all = sum(list_numbers)
    sum_1_to_n = len(list_numbers) * (len(list_numbers) - 1) / 2

    return sum_all - sum_1_to_n


print(find_repeat(
    [10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1, 2, 3, 4, 5,  6, 7]))
