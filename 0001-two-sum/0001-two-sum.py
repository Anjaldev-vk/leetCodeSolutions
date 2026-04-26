class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in s:
                return [s[value],i]
            s[num] = i
                
        