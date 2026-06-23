class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = ''
        current_string = ''
        for st in s:
            if st in current_string:
                current_string = current_string.split(st)[1]
                current_string += st
            else:
                current_string += st
            if len(current_string) > len(longest_string):
                longest_string = current_string
            print(current_string)
                
        print(longest_string)
        return len(longest_string)