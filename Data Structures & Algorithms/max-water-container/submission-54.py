class Solution:


    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        def Area(i,j):
            return (j-i) * min(heights[i], heights[j])

        left = 0 
        right = len(heights) - 1

        current_max_Area = Area(left,right)

        # Find the next candidate to try - need heights bigger at least

        # Right idea, but no, not bigger at least, as still need to shift. Just shift the minimum one

        while left < right:
            if min(heights[left],heights[right]) == heights[left]:
                left += 1
            else:
                right -= 1
            current_max_Area = max(Area(left,right),current_max_Area)

        return current_max_Area

        



# Start with two biggest... move outward?
# Yea as I don't think the moving in method works
# Can definitely prune to ignore candidate bars where there is a bigger one to the outside?




        '''for i in range(len(heights)):
            for j in range(len(heights)):
                max_area = max(Area(i,j),max_area)

        return max_area'''

        