class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = nums1[:m] + nums2
        temp.sort()
        for i in range(m + n):
            nums1[i] = temp[i]

        