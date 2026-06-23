class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Define Base Cases
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        # Remove the duplicates 
        nums = list(set(nums))
        # Sort the numbers
        nums.sort()
        # Take in account the longest sequence (l_seq) seen and
        # the current sequence (c_seq) that our algorithm is looking at
        l_seq = []
        c_seq = []
        # Iterate through the nums
        for n in nums:
            # Check is the list is empty
            if len(c_seq) == 0:
                c_seq.append(n)
            else:
            # If not empty, compare and then append the number
                if n-c_seq[-1] == 1:
                    c_seq.append(n)
                else:
                    # Compare the sequences and update
                    # Do it here as well because the current sequence 
                    # is going to get updated
                    if len(c_seq) > len(l_seq):
                        l_seq = c_seq
                    c_seq = [n]
        # Compare the sequences and update
        if len(c_seq) > len(l_seq):
            l_seq = c_seq

        return len(l_seq)
            
        
        