class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)

        for x in s:
            hashmap[x] += 1
        for x in t:
            hashmap[x] -= 1

        for val in hashmap.values():
            if val != 0:
                return False
        return True