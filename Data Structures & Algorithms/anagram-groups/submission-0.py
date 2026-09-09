class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        for s in strs:
            letters = [0] * 26
            for i in s:
                letters[ord(i) - 97] += 1
            tl = tuple(letters)
            if tl not in dicts.keys():
                dicts[tl] = []
            dicts[tl].append(s)
        return list(dicts.values())