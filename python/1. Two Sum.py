from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, number1 in enumerate(nums):
            for index2, number2 in enumerate(nums):
                if (index1 == index2):
                    continue
                if number1 + number2 == target:
                    return [index1, index2]


print(Solution().twoSum([2,7,11,15], 9))