class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import deque

        num_set = set(nums)
        longest_chain = 0

        while(len(num_set) > 0):
            chain = []
            queue = deque()
            queue.append(next(iter(num_set)))
            
            while(queue):
                a = queue.popleft()
                # print(a)
                chain.append(a)
                num_set.discard(a)
                if((a-1) in num_set):
                    queue.append(a-1)
                if((a+1) in num_set):
                    queue.append(a+1)
            
            
            longest_chain = max(len(chain), longest_chain)
        return longest_chain
