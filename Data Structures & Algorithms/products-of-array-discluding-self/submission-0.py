import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        for i in range(len(nums)):
            num = nums[i]
            new_nums = nums.copy()
            new_nums.pop(i)
            prods.append(math.prod(new_nums))
        return prods