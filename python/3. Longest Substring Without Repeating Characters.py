class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        substrings = []
        for cut_pos in range(len(s)):
            substrings.append(s[cut_pos:])

        lengths = list(map(self.longestSubstring, substrings))           
        return max(lengths)
        



    def longestSubstring(self, substring):
        buffer = ''
        for char in substring:
            if char in buffer:
                return len(buffer)
            buffer += char
        return len(buffer)


print(Solution().lengthOfLongestSubstring("au"))


