class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        temp = num

        if temp <= 0:
            return False
        while temp > 1:
            if temp % 2 == 0:
                temp = temp / 2
                continue
            if temp % 3 == 0:
                temp = temp / 3
                continue
            if temp % 5 == 0:
                temp = temp / 5
                continue
            return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isUgly(21))