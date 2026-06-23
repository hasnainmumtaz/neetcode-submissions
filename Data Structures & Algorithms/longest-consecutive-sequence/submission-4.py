class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        nums = list(set(nums))
        nums.sort()
        print(nums)
        l_seq = []
        c_seq = []
        for n in nums:
            if len(c_seq) == 0:
                c_seq.append(n)
            else:
                if n-c_seq[-1] == 1:
                    c_seq.append(n)
                else:
                    if len(c_seq) > len(l_seq):
                        l_seq = c_seq
                    c_seq = [n]
        if len(c_seq) > len(l_seq):
            l_seq = c_seq

        print(l_seq)
        return len(l_seq)
            
        
        