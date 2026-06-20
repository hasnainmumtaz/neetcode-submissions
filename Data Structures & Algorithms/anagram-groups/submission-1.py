from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for string in strs:
            check = str(dict(sorted((Counter(string).items()))))
            print(check)
            if check in my_dict:
                my_dict[check].append(string)
            else:
                my_dict[check] = []
                my_dict[check].append(string)

        output = list(my_dict.values())
        return sorted(output)

