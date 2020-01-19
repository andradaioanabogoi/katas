class Solution(object):
    def bfs(self, candidates, target, result, valuelist, start):
        if target == 0 and valuelist not in result:
            return result.append(valuelist)
        for index in range(start, len(candidates)):
            print(index)
            if target < candidates[index]:
                return
                print("HERE")
            self.bfs(candidates, target -
                     candidates[index], result, valuelist + [candidates[index]], index + 1)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.bfs(candidates, target, result, [], 0)
        return result


print(Solution().combinationSum2([1, 2, 3, 4, 7, 4, 3], 8))
