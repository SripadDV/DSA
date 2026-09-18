# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head == None:
            return head
        if head.next == None:
            return head
        
        headNode = head
        cur = head.next
        prev = head
        head.next = None
        while cur != None:
            print(cur.val)
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        head = prev
        return head

