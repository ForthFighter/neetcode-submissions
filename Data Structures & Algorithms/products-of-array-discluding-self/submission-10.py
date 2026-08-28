class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            if nums.count(0) > 1:
                return [0]*len(nums)
            product_without_zero = 1
            for num in nums:
                if num != 0:
                    product_without_zero *= num
            
            result = nums
            for i in range(len(result)):
                if result[i] == 0:
                    result[i] = product_without_zero
                else: result[i] = 0
            return result

        product_all = 1
        for num in nums:
            product_all *= num
        
        result = [int(product_all / num) for num in nums]

        return result

        # Problem for 0s

        # Also, multiple zeroes

        # if num = 0

        
             
        