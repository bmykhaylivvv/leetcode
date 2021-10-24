from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)

        for_prefix = strs[0]

        prefixes = []

        for cut in range(1, len(for_prefix) + 1):
            prefixes.append(for_prefix[:cut])

        suitable_prefixes = []



        for prefix in prefixes:
            matches = 0
            for word in strs:
                if word.startswith(prefix):
                    matches += 1

            if matches == len(strs):
                suitable_prefixes.append(prefix)

        if len(suitable_prefixes) >= 1:
            return suitable_prefixes[-1]

        return ''



# strs = ["dog","racecar","car"]
# strs = sorted(strs, key=len)

# for_prefix = strs[0]

# prefixes = []

# for cut in range(1, len(for_prefix) + 1):
#     prefixes.append(for_prefix[:cut])

# suitable_prefixes = []



# for prefix in prefixes:
#     matches = 0
#     for word in strs:
#         if word.startswith(prefix):
#             matches += 1

#     if matches == len(strs):
#         suitable_prefixes.append(prefix)

# print(suitable_prefixes[-1])