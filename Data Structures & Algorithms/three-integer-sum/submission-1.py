class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            print(f"i: {i}")
            p1 = i + 1
            p2 = len(nums) - 1
            while(p2 > p1):
                threeSum = nums[p1] + nums[p2] + nums[i]
                if (threeSum == 0):    
                    results.append([nums[p1], nums[p2], nums[i]])
                    p1 += 1
                    p2 -= 1
                elif (threeSum > 0):
                    p2 -= 1
                elif (threeSum < 0):
                    p1 += 1
        return list(set([tuple(x) for x in results]))

