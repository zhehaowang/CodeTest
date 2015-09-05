# Old solution of O(n^2)
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        i = 0
        j = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i + 1, j + 1]
'''
# New solution of O(n)
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        i = 0
        array = [0] * 65536 * 2
        has = []
        result = [0] * 2
        cnt = 0
        # Error: [0, 4, 3, 0] targets 0
        for i in range(0, len(nums)):
            array[nums[i]] = array[nums[i]] + 1
            has.append(nums[i])
        for i in range(0, len(has)):
            temp = target - has[i]
            # Error: [3, 2, 4] target 6, same thing used twice
            # Error: second index shown as direct number instead: [3, 2, 4] target 6, prev result [2, 4]
            if (array[temp] == 1 and temp != has[i]) or array[temp] == 2:
                result[cnt] = i + 1
                cnt += 1
                if cnt == 2:
                    return result
        return 

sol = Solution()
print(sol.twoSum([3, 2, 4], 6))
