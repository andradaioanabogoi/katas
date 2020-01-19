class judgeCircle:
    def __init__(self):
        self.memo = {"U": 0, "D": 0, "R": 0, "L": 0}

    def judgeCircle(self, moves):
        for char in moves:
            self.memo[char] += 1
        return (self.memo["L"] == self.memo["R"] and self.memo["U"] == self.memo["D"])


print(judgeCircle().judgeCircle("UUDDLR"))
