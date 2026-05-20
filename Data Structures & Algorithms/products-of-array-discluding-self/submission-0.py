class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = math.prod(nums)
        res = [0] * len(nums)
        for i, n in enumerate(nums) :
            if n :
                res[i] = int(total_product / n)
            else:
                res[i] = math.prod(nums[:i] + nums[i+1:]) 
        return res
        