# Note: the key is in 'which pointer can be moved'

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        result = min(height[right], height[left]) * (right - left)
        while left < right:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            result = max(result, min(height[right], height[left]) * (right - left))
        return result
