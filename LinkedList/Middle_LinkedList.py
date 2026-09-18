# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if head == None:
            return head
        if head.next == None:
            return head
        fast = head
        slow = head
        while fast.next != None:
            fast = fast.next
            slow = slow.next
            if fast.next == None:
                return slow
            fast = fast.next
        return slow