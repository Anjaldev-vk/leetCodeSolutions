class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        if any(v > 1 for v in freq.values()):
            return True
        else:
            return False