def hashCreator(anagram):
    from string import ascii_lowercase

    letters = dict(zip(ascii_lowercase, [0] * 26))

    for letter in anagram:
        letters[letter] += 1

    return letters


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for elem in strs:
            key = tuple(hashCreator(elem).items())

            if key not in groups:
                groups[key] = []

            groups[key].append(elem)

        return list(groups.values())