class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict(zip(set(nums), [0]*len(set(nums))))
        for num in nums:
            num_dict[num]+=1
        for num in num_dict.keys():
            if (target-num in num_dict and (target != num or num_dict[num]>1)):
                i = nums.index(num)
                j = len(nums) - 1 - nums[::-1].index(target-num)
                return [min(i, j), max(i, j)]
