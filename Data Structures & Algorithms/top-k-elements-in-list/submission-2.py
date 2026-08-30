class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fc = dict(zip(set(nums), len(set(nums)) * [0]))
        for num in nums:
            fc[num]+=1
        # print(f"Frequency Counts: \n{fc}")
        result = []
        k_count = 0
        rfc = [[] for _ in range(max(fc.values())+1)]
        # print(rfc)
        for elem in fc.keys():
            # print(f"elem: {elem} \n fc[elem]: {fc[elem]} \n rfc[fc[elem]]:{rfc[fc[elem]]}")
            rfc[fc[elem]].append(elem)
        # print(rfc)
        for elem in rfc[::-1]:
            for val in elem:
                result.append(val)
                k_count += 1
            if(k_count == k):
                return result