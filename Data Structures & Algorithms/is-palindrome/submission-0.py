class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(filter(str.isalnum,s))
        if filtered.lower() == filtered[::-1].lower():
            return True
        else:
            return False