class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if not num in visited:
                visited.add(num)
            else:
                return True
        return False
        