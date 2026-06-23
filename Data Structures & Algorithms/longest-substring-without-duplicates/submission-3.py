class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = ''
        current_string = ''
        # Iterate through the characters
        for st in s:
            if st in current_string:
                # Check for duplicate and then get the the recent sequence
                current_string = current_string.split(st)[1]
                current_string += st
            else:
                current_string += st
            # Check if the current string is longer
            if len(current_string) > len(longest_string):
                longest_string = current_string
            print(current_string)

        # Return the longest string                
        return len(longest_string)