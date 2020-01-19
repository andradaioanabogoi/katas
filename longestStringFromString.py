class LongestString():
    def __init__(self):
        # instance variables (best declares in the init function)
        self.memo = {}
    CACA = "MACA"

    def longestSubstring(self, string_input):
        for char in string_input:
            if char not in self.memo:
                self.memo[char] = 1
            else:
                self.memo[char] += 1
        # return self.memo
        return len(self.memo.keys())

    #INTERESTING
    def lengthOfLongestSubstring(self, s):
        dct = {}
        max_so_far = curr_max = start = 0
        for index, i in enumerate(s):
            print(index, i)
            if i in dct and dct[i] >= start:
                max_so_far = max(max_so_far, curr_max)
                print(max_so_far)
                curr_max = index - dct[i]
                print(curr_max)
                start = dct[i] + 1
            else:
                curr_max += 1
            dct[i] = index
            print(dct)
        return max(max_so_far, curr_max)


print(LongestString().lengthOfLongestSubstring("pwwkew"))
