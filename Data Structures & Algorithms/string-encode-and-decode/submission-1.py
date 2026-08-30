class Solution:

    def encode(self, strs: List[str]) -> str:
        result = "".join([word[::-1] + "|-|-|" for word in strs])
        print(result)
        return result
    def decode(self, s: str) -> List[str]:
        
        return [word[::-1] for word in s.split('|-|-|')][:-1]