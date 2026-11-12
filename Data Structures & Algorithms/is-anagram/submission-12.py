class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram = {}
        for i in s:
            anagram[i] = anagram.get(i, 0) + 1
        for i in t:
            if i not in anagram:
                return False
            anagram[i]-=1
            if anagram[i] < 0:
                return False
        return True