class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        with division is simple just take the product of the entire thing and    
        divide by each element each time
        '''
        zc = nums.count(0)
        prod = 1
        for elem in nums:
            if (zc == 1) and elem == 0:
                continue
            prod *= elem
        result = []
        for elem in nums:
            if zc == 1 and elem != 0:
                result.append(0)
            elif elem == 0:
                result.append(prod)
            else:
                result.append(prod//elem)
        return result


