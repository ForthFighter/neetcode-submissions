# Well, I have done this before

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = { nums[i] : i  for i in range(len((nums)))}

        for num in hashmap: 
            if target - num in hashmap and num != target - num:
                return sorted([hashmap[num], hashmap[target - num]])

        # If still not returned, it is a double
        val = target / 2
        indices = []

        for i in range(len((nums))):
            if nums[i] == val:
                indices.append(i)
        
        return indices


        

    # Edge case problem as can have doubles
    # How to get key in dat case?


        