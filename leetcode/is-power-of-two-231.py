class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = n
        if temp <= 0:
            return False
        while temp > 1:
            if temp % 2 != 0:
                return False
            temp = temp / 2
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(-1))