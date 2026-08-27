class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = list(set(nums))
        for i in range(len(nums)):
            nums[i] = str(nums[i]) 
        for el in lst:
                nums.remove(str(el))
        return nums != []
        