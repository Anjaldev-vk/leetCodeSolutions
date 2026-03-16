class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_type = len(set(candyType))
        max_allowed = len(candyType) // 2
        return min(unique_type, max_allowed)
        