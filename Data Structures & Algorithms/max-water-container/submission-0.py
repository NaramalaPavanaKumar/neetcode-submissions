class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max=0
        while left<right:
            a=min(heights[left],heights[right])*(right-left)
            if a>max:
                max=a
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return max

        