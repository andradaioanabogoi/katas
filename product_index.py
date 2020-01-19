
# GREEDY approach in two passes!
# careful at division by 0. If we have one 0, then the product is 0 but for that position. What if we have 2 zeroes.


def get_products_of_all_ints_except_at_index(input):
    # Alernative: output = [None]*len(input)
    output = []
    product_so_far = 1

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time

    # Careful at insert vs append!!
    for i in range(len(input)):
        output.insert(i, product_so_far)
        product_so_far *= input[i]

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers

    product_so_far = 1
    for i in range(len(input) - 1, -1, -1):
        output[i] *= product_so_far
        product_so_far *= input[i]

    return output


print(get_products_of_all_ints_except_at_index([1, 3, 7, 8]))
