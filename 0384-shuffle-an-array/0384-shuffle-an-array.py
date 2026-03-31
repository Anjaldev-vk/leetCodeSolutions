import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.array = nums[:]
        

    def reset(self) -> List[int]:
        self.array = self.original[:]
        return self.array
        

    def shuffle(self) -> List[int]:
        nums = self.array[:]
        for i in range(len(nums)):
            j = random.randint(i, len(nums)-1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()