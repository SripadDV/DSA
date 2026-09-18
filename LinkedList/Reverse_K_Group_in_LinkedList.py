# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def checkKNodes(self, head: ListNode, k: int) -> bool:
        count = 0
        cur = head
        while cur != None:
            cur = cur.next
            count += 1
            if count == k:
                return True
        return False

    def reverseLLKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        if self.checkKNodes(head, k):
        
            count = 1
            prev = head
            cur = head.next
            while count < k:
                curNext = cur.next
                cur.next = prev
                prev = cur
                cur = curNext
                count += 1
            head.next = self.reverseLLKGroup(cur, k)
            return prev
        else:
            return head


    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 1:
            return head
        
        return self.reverseLLKGroup(head, k)