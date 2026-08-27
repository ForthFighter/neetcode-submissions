# Neetcode solution with bucket sort 

# Really it's not the full bucket sort algorithm, which is a true sorting algorithm. We avoid having to sort fully here, and that is where we get a speed up from. We are bucketing the numbers by how many times they show up, hence the 'bucket'.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num,0) 
            # Basically count[num] += 1, or 1 if not already a key
        for num, cnt in count.items():
            freq[cnt].append(num) # Clever, here duplicate instances
            # are fine, in fact they help

        res = []
        for i in range(len(freq) - 1, 0 ,-1): # Front to back
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


        