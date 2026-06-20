class Solution:
    key="|=|"
    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += string + Solution.key
        return output

    def decode(self, s: str) -> List[str]:
        output = list(s.split(Solution.key))
        return output[0:-1]