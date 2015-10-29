class Solution(object):
    def canWinNim(self, n):
        r = n % 4
        if (r == 0):
            return False
        return True
        """
        :type n: int
        :rtype: bool
        """
        