class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        step = k % len(nums)
        first = nums[len(nums) - step:len(nums)]
        last = nums[0:len(nums) - step]
        nums[:] = (first + last)[:]

if __name__ == '__main__':
	sol = Solution()
	nums = [1, 2]
	sol.rotate(nums, 1)
	print(nums)