import random

# We choose a random item to move to the first index, then we choose a random other item to move to the second index, etc. We "place" an item in an index by swapping it with the item currently at that index.

# O(n) time
# O(1) space


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle_list(input_list):
    if(len(input_list) <= 1):
        return input_list

    for i in range(0, len(input_list) - 1):
        random_choice_index = get_random(i, len(input_list) - 1)

        if(random_choice_index != i):
            input_list[i], input_list[random_choice_index] = input_list[random_choice_index], input_list[i]
    return input_list


print(shuffle_list([1, 2, 3, 6, 5]))
