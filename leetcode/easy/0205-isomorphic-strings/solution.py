class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        reverse = {}

        for i in range(len(s)):
            if s[i] in mapping and mapping[s[i]] != t[i]:
                return False

            if t[i] in reverse and reverse[t[i]] != s[i]:
                return False

            mapping[s[i]] = t[i]
            reverse[t[i]] = s[i]

        return True