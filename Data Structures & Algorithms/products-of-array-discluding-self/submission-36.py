class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sequence = [1] * (len(nums))
        for i in range(len(nums) - 1):
            prefix_sequence[i + 1] = prefix_sequence[i] * nums[i]

        postfix_sequence = [1] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            postfix_sequence[i - 1] = postfix_sequence[i] * nums[i]

        result = [prefix_sequence[i] * postfix_sequence[i] for i in range(len(nums))]
        return result

        
        