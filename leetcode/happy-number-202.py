class Solution:
    def happyWrapper(self, n, loop):
        print(n)
        if (n in loop):
            return False
        elif n == 1:
            return True
        else:
            loop.append(n)
            num = n
            sqr = 0
            while num != 0:
                sqr = sqr + (num % 10) * (num % 10)
                num = num / 10
            return self.happyWrapper(sqr, loop)
        
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        loop = []
        return self.happyWrapper(n, loop)
        
sol = Solution()
print(sol.isHappy(19))
