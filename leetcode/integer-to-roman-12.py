class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        i = num / 1000
        str = 'M' * i
        
        num = num % 1000
        
        i = num / 100
        if (i == 9):
            str = str + 'CM'
        elif (i > 4 and i < 9):
            str = str + 'D' + 'C' * (i - 5)
        elif (i == 4):
            str = str + 'CD'
        else:
            str = str + 'C' * i
        
        num = num % 100
        
        i = num / 10
        if (i == 9):
            str = str + 'XC'
        elif (i > 4 and i < 9):
            str = str + 'L' + 'X' * (i - 5)
        elif (i == 4):
            str = str + 'XL'
        else:
            str = str + 'X' * i
            
        num = num % 10
        i = num
        if (i == 9):
            str = str + 'IX'
        elif (i > 4 and i < 9):
            str = str + 'V' + 'I' * (i - 5)
        elif (i == 4):
            str = str + 'IV'
        else:
            str = str + 'I' * i
        
        return str

sol = Solution()
print(sol.intToRoman(1994))
