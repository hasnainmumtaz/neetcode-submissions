class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            complement = target - i
            print(complement)
            if complement in numbers and complement != i:
                return [numbers.index(i)+1, numbers.index(complement)+1]
