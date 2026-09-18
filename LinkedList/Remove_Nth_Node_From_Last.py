# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # if n == 1:
        #     if head.next == None:
        #         return head.next
            
        ll_len = 0
        cur = head
        while cur != None:
            ll_len += 1
            cur = cur.next
        if n == ll_len:
            newHead = head.next
            head.next = None
            return newHead
        
        left = head
        right = head
        for i in range(n-1):
            right = right.next
        
        while right.next != None:
            right = right.next
            left = left.next
        
        cur = head
        while cur.next != left:
            cur = cur.next
        
        cur.next = left.next
        return head


        