# Multiple players can have the same score!
# Efficient way to sort array,  at the expense of adding O(n) space.


def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    # score_counts = []
    score_counts = [0] * (HIGHEST_POSSIBLE_SCORE+1)

    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []
    for score in range(len(score_counts)-1, -1, -1):
        count = score_counts[score]

        for i in range(count):
            sorted_scores.append(score)
    return sorted_scores


print(sort_scores([91, 34, 34, 34, 34, 76, 89, 21, 13], 100))
