class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(0, len(nums)):
            num_1 = nums[i]
            for j in range(0, len(nums)):
                if i == j:
                    continue
                elif num_1 + nums[j] == target:
                    return [i, j]