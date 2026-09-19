# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def findMid2(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast.next != None:
            fast = fast.next

            if fast.next != None:
                fast = fast.next
                slow = slow.next
            else:
                return slow
        return slow

    def reverse(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        if head.next == None:
            return head
        
        prev = head
        cur = head.next
        while cur != None:
            curNext = cur.next
            cur.next = prev
            prev = cur
            cur = curNext
        
        head.next = None
        return prev

    def isPalindrome(self, head: ListNode | None) -> bool:
        if head.next == None:
            return True
        mid = self.findMid2(head)

        mid.next = self.reverse(mid.next)
        
        cur1 = head
        cur2 = mid.next

        while cur2 != None:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next

        return True

