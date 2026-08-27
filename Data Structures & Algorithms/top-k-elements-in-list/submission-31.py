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