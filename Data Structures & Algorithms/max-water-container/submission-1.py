class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights)-1
        maxWater = 0
        while p2 > p1:
            # print(f"p1: {heights[p1]} p2: {heights[p2]} area = {min(heights[p1  ], heights[p2]) * (p2-p1)}")
            if heights[p2] > heights[p1]:
                maxWater = max(maxWater, heights[p1] * (p2 - p1))
                p1+=1
            elif heights[p1] >= heights[p2]:
                maxWater = max(maxWater, heights[p2] * (p2 - p1))
                p2-=1
            
        return maxWater


