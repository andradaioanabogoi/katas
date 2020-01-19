# Our answer was a modified binary search.
# We got there by reasoning about the expected runtime:
# We started with an O(n^2) "brute force" solution and wondered if we could do better.
# We knew to beat O(n^2) we'd probably do O(n) or
# O(nlgn), so we started thinking of ways we might get an O(nlgn) runtime.
# lg(n) usually comes from iteratively cutting stuff in half, so we arrived at the final algorithm by exploring that idea.


def find_repeat(the_list):
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + int(((ceiling - floor) / 2))

        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor


print(find_repeat([1, 2, 2, 2, 4, 4, 6]))
