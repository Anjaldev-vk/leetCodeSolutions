class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = nums.count(0)
        numbers = [x for x in nums if x != 0]

        for _ in range(zero):
            numbers.append(0)

        nums[:] = numbers