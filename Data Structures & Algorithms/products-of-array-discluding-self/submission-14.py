class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 0:
            if zero_count > 1:
                return [0]*len(nums)
            product_without_zero = 1
            for num in nums:
                if num != 0:
                    product_without_zero *= num
            
            result = nums[:] # Bad practice to set a = b to get a copy of b, since then b is just a reference to a, and mutating one affects the other. Can also use result = nums.copy()
            
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

        
             
        