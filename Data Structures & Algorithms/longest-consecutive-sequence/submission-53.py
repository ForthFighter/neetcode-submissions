class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        numset = set(nums)

        index = 0
        best_run_length = 1

        for num in nums: # find minimum for that run:
            if num not in numset:
                True
            else:
                current_run_length = 1
                while num - 1 in numset:
                    num -= 1
                # now find length of run, removing at each stage
                while num + 1 in numset:
                    current_run_length += 1
                    numset.remove(num)
                    num += 1
            
                best_run_length = max(best_run_length, current_run_length)

        return best_run_length
