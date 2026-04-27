class Solution(object):
    def summaryRanges(self, nums):
        res = []
        left = right = 0
        n = len(nums)

        while right < n:

            if right == n - 1 or nums[right] + 1 != nums[right + 1]:
                if right == left:
                    res.append(str(nums[left]))
                else:
                    res.append(f"{nums[left]}->{nums[right]}")
                
                left = right + 1 
            right += 1

        return res