class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums) # so have a dict with keys as nums, values 
        # as instances
        result = []
        entries_filled = 0

        top_k_sorted_amounts = sorted(list(count.values()))[-k :]

        for num in count.keys():
            if count[num] in top_k_sorted_amounts:
                result.append(num)

        return result

    # Is using sorted and Counter cheating? Let us see.














        # Keep order but not duplicates, and only the k maxima
        # Problem as can have a duplicate amount not for duplicate entry

        sorted_amounts = list(dict.fromkeys(sorted_amounts))

        result = []
        entries_filled = 0

        
        for amount in sorted_amounts[:: -1]:
            if hashmap[amount] not in result:
                result.append(hashmap[amount])
                entries_filled += 1
            if entries_filled == k: return result
        return result

    



        