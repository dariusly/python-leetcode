class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        result = []
        nums.sort()
        backtrack(0, [])
        return result


solution_instance = Solution()
nums = [1, 2, 2]
print(solution_instance.subsetsWithDup(nums))
