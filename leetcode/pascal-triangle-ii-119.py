class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if (rowIndex == 0):
            return eval('[1]')
        strfront = '[1'
        strback = '1]'
        num = 1
        
        for i in range(1, (rowIndex + 2) / 2):
            num = num * (rowIndex - i + 1) / i
            strfront = strfront + ',' + str(num)
            if (rowIndex % 2 == 1 or i != rowIndex / 2):
                strback = str(num) + ','  + strback
        
        return eval(strfront + ',' + strback)

sol = Solution()
print(sol.getRow(3))
