class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if (numRows == 1):
            return s
        strs = ['' for i in range(0, numRows)]
        j = 0
        inc = 1
        for i in range(0, len(s)):
            strs[j] = strs[j] + s[i]
            j = j + inc
            if j == numRows:
                j = j - 2
                inc = -1
            if j == -1:
                j = j + 2
                inc = 1
        result = ''
        for i in range(0, numRows):
            result = result + strs[i]
        return result
        
sol = Solution()
print(sol.convert('CRAPISGOOD', 2))
