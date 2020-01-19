import collections
# use Maths properties. If length of array is 2N and N+1 are equal, then
# at least one subarray of 4 has 2 elements that are the same
# leetCode


class Solution:
    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        print(count)
        for k in count:
            if count[k] > 1:
                return k

    def betterRepeatedNTimes(self, A):
        for k in range(1, 4):
            for i in range(len(A) - k):
                if A[i] == A[i+k]:
                    return A[i]


print(Solution().repeatedNTimes([1, 2, 5, 6, 2, 2, 2, 3]))
print(Solution().betterRepeatedNTimes([1, 2, 5, 6, 2, 2, 2, 3]))
