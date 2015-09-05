class Solution:
    # @param {integer[]} nums
    # @return {string}
    
    # Error: made a more traditional bit by bit one at first, considered [344, 34], but could not handle [121, 12]
    # Error: did not handle [0, 0], should give "0", instead of "00"
    def compareStrs(self, str1, str2):
        if (str1 + str2 > str2 + str1):
            return -1
        elif (str1 + str2 == str2 + str1):
            return 0
        else:
            return 1
        
    def largestNumber(self, nums):
        strs = map(str, nums)
        strs = sorted(strs, self.compareStrs)
        result = ''
        for i in range(0, len(strs)):
            result = result + strs[i]
        return str(int(result))

sol = Solution()
print(sol.largestNumber([0, 0]))
