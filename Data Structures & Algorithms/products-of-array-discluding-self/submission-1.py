import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        raw_nums = [nums.copy() for i in range(length)]
        for i in range(length):
            raw_nums[i].pop(i)

        output = []
        for n in raw_nums:
            output.append(math.prod(n))    
        return output