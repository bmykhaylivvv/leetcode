import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.fullmatch(p, s) != None



s = 'aab'
p = 'c*a*b'

print(re.fullmatch(p, s) != None)
