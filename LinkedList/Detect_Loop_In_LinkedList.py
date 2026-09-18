# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        fast = head
        slow = head
        while fast.next != None:
            fast = fast.next
            slow = slow.next
            if fast.next == None:
                return False
            fast = fast.next
            if fast == slow:
                return True
        return False