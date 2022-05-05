class Solution:

    def recurse(self, current_index, original_list, list, target):
        if len(list) <= 0:
            return Solution().recurse(current_index + 1, original_list[1:len(original_list)], original_list[1:len(original_list)], target)
        num_1 = original_list[0]
        index_to_check = len(list) // 2
        num_2 = list[index_to_check]

        if num_1 + num_2 == target:
            return [num_1, num_2]
        if num_1 + num_2 > target:
            return Solution().recurse(current_index, original_list, list[0:index_to_check], target)
        if num_1 + num_2 < target:
            return Solution().recurse(current_index, original_list, list[index_to_check + 1: len(list)], target)

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(nums)
        answer_nums = Solution().recurse(0, sorted_nums, sorted_nums, target)
        num_1 = answer_nums[0]
        num_2 = answer_nums[1]

        if num_1 == num_2:
            answer_1 = nums.index(num_1)
            temp_nums = list(nums)
            del(temp_nums[answer_1])
            answer_2 = temp_nums.index(num_2) + 1
        else:
            answer_1 = nums.index(num_1)
            answer_2 = nums.index(num_2)
        return [answer_1, answer_2]


nums_list = [1,6142,8192,10239]
target = 18431

print(Solution().twoSum(nums_list, target))