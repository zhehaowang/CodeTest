class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict1 = dict()
        dict2 = dict()
        
        strs = str.strip().split(" ")
        idx = -1
        
        if (len(strs) != len(pattern)):
            return False
        
        for item in strs:
            idx += 1
            if (item in dict1):
                if (dict1[item] in dict2):
                    if pattern[idx] == dict1[item]:
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                if (pattern[idx] in dict2):
                    return False
                else:
                    dict2[pattern[idx]] = item
                    dict1[item] = pattern[idx]
        return True