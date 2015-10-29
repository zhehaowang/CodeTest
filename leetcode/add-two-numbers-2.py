# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        temp1 = l1
        temp2 = l2
        carry = 0
        head = ListNode(0)
        prev = head

        while (temp1 != None or temp2 != None):
            temp = ListNode(0)

            val1 = 0
            if (temp1 != None):
                val1 = temp1.val
                temp1 = temp1.next
            val2 = 0
            if (temp2 != None):
                val2 = temp2.val
                temp2 = temp2.next
            val = val1 + val2 + carry
            carry = 0
            if val > 9:
                val = val - 10
                carry = 1
            temp.val = val
            prev.next = temp
            prev = temp
        if (carry != 0):
            temp = ListNode(1)
            prev.next = temp
        
        return head.next

dig11 = ListNode(0)
# dig12 = ListNode(0)
# dig13 = ListNode(0)
# dig11.next = dig12
# dig12.next = dig13

dig21 = ListNode(0)
# dig22 = ListNode(0)
# dig21.next = dig22

sol = Solution()
temp = sol.addTwoNumbers(dig11, dig21)

while (temp != None):
    print(temp.val)
    temp = temp.next
