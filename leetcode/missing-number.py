class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        length = len(nums)
        for i in range(0, length):
            total += nums[i]
        return (length + 1) * length / 2 - total


if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([1, 2]))