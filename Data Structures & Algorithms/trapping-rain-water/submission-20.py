class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = []
        leftMaxH = 0
        rightMax = []
        rightMaxH = 0
        for elem in height:
            leftMaxH = max(leftMaxH, elem)
            leftMax.append(leftMaxH)
        for elem in height[::-1]:
            rightMaxH = max(rightMaxH, elem)
            rightMax.append(rightMaxH)
        rightMax = rightMax[::-1]
        # print(leftMax)
        # print(rightMax)
        maxWater = 0
        for i in range(1, len(height)-1):
            # print(f"i: {i}, leftMax: {leftMax[i-1]}, rightMax: {rightMax[i-1]}, water: {max(0, min(leftMax[i-1], rightMax[i + 1]) - height[i])}")
            maxWater += max(0, min(leftMax[i-1], rightMax[i + 1]) - height[i])
        # print(maxWater)
        return maxWater
