def change(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:

        for higher_amount in range(coin, amount + 1):  # de la 1 la 5
            higher_amount_remainder = higher_amount - coin  # 0 1 2 3 4
            ways_of_doing_n_cents[higher_amount] += (
                ways_of_doing_n_cents[higher_amount_remainder]  # 1 1 2 3 4
            )

    return ways_of_doing_n_cents[amount]


print(change(4, [1, 2, 3]))
print(change(5, [1, 3, 5]))


class Change(object):
    def __init__(self):
        self.memo = {}

    def change(self, amount, denominations):


ways_of_doing_n_cents
