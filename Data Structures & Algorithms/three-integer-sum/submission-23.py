# Finally, a brute force solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Can I reduce this to two sets of twosum?

        n = len(nums)

        hashmap = { nums[i]:i for i in range(n)}

        triplets = []

        for i in range(n):
            for j in range(n):
                if -(nums[i] + nums[j]) in hashmap and i != j and i != hashmap[-nums[i]-nums[j]] and j != hashmap[-nums[i]-nums[j]]:
                    triplets.append(sorted([nums[i],nums[j],-(nums[i]+nums[j])]))

        unique_triplets = []

        # Search for triples.

        cnt = Counter(nums)

        if 0 in cnt and cnt[0] >= 3:
                unique_triplets.append([0,0,0])

        for num in cnt:
            if cnt[num] >= 2 and -2*num in hashmap and num != 0:
                unique_triplets.append(sorted([num,num,-2*num]))


        for t in triplets:
            if t not in unique_triplets and not (t[0] == t[1] or t[0] == t[2] or t[0] == t[1]) :
                unique_triplets.append(t)
        return unique_triplets
        


        

        
        