# GREEDY again
# Calculate highest/lowest product of 1 and 2 and the highest_product_of_3


def get_highest_product_of_three(input):

    if(len(input) < 3):
        raise ValueError("Less than 3 items")

    highest_product_of_3 = input[0]*input[1]*input[2]
    highest_product_of_2 = input[0]*input[1]
    highest = max(input[0], input[1])

    lowest_product_of_2 = input[0] * input[1]
    lowest = min(input[0], input[1])

    for i in range(2, len(input)):
        current = input[i]

        highest_product_of_3 = max(
            highest_product_of_2*current, highest_product_of_3, current*lowest_product_of_2)
        highest_product_of_2 = max(
            lowest*current, highest_product_of_2, highest*current)
        highest = max(highest, current)

        lowest_product_of_2 = min(
            lowest*current, lowest_product_of_2, highest*current)
        lowest = min(lowest, current)

    return highest_product_of_3


print(get_highest_product_of_three([-2, 3, -9, 5, 6, 1, 2]))
print(get_highest_product_of_three([-2, 3]))
