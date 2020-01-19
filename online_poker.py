# What happens if we run out of space? It's a stack overflow!
# In Python 3.6, you'll get a RecursionError.
# Careful with recursion
# The call stack is what a program uses to keep track of function calls.
# The call stack is made up of stack frames
# TCO: function could free up its stack frame before doing its final call, saving space.
# If a recursive function is optimized with TCO, then it may not end up with a big call stack.
# In general, most languages don't provide TCO.
# Scheme is one of the few languages that guarantee tail call optimization.
# Some Ruby, C, and Javascipt implementations may do it.
# Python and Java decidedly don't.


def single_shuffle(shuffle_deck, half_1, half_2):
    half_1_index = 0
    half_2_index = 0
    half1_max_index = len(half_1) - 1
    half2_max_index = len(half_2) - 1

    for card in shuffle_deck:
        if(half_1_index <= half1_max_index and card == half_1[half_1_index]):
            half_1_index += 1
        elif(half_2_index <= half2_max_index and card == half_2[half_2_index]):
            half_2_index += 1
        else:
            return False
    return True


print(single_shuffle([1, 2, 88, 7, 8, 9, 4, 5, 6],
                     [8, 9, 4, 5, 6], [1, 2, 7, 0]))
