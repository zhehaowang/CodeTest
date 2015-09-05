# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        replace = head
        if (not replace):
            return None
        temp = head.next
        while temp != None:
            if (temp.val == val):
                replace.next = temp.next
            # NOTE: this is the part where I got wrong at first
            else:
                replace = temp
            temp = temp.next
        if (head.val == val):
            return head.next
        return head

node = ListNode(5)
node1 = ListNode(5)
node2 = ListNode(3)
node3 = ListNode(5)

node.next = node1
node1.next = node2
node2.next = node3

sol = Solution()
temp = sol.removeElements(node, 5)

while temp != None:
    print(temp.val)
    temp = temp.next

print('over')
