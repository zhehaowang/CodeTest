class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = dict()
        tDict = dict()
        
        for i in s:
            if i in sDict:
                sDict[i] += 1
            else:
                sDict[i] = 1

        for i in t:
            if i in tDict:
                tDict[i] += 1
            else:
                tDict[i] = 1

        for i in tDict:
            if (not i in sDict) or (sDict[i] != tDict[i]):
                return False

        for i in sDict:
            if (not i in tDict) or (sDict[i] != tDict[i]):
                return False

        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("ab", "a"))