from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)
        mid = (len(res) - 1) // 2
        print(res[mid])

        return res[mid] if len(res) % 2 != 0 else (res[mid] + res[mid + 1])/2



print(Solution().findMedianSortedArrays([1, 2], [3, 4]))