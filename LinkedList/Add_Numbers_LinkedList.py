# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        sumLL = ListNode()
        cur = sumLL
        cur1 = l1
        cur2 = l2
        carry = 0
        while cur1 != None and cur2 != None:
            sum_val = cur1.val + cur2.val + carry
            sum_digit = sum_val%10
            carry = sum_val//10
            cur.next = ListNode(sum_digit)
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next
        
        while cur1 != None:
            sum_val = cur1.val + carry
            sum_digit = sum_val%10
            carry = sum_val//10
            cur.next = ListNode(sum_digit)
            cur = cur.next
            cur1 = cur1.next

        while cur2 != None:
            sum_val = cur2.val + carry
            sum_digit = sum_val%10
            carry = sum_val//10
            cur.next = ListNode(sum_digit)
            cur = cur.next
            cur2 = cur2.next
        
        if carry > 0:
            cur.next = ListNode(carry)
            cur = cur.next
        
        return sumLL.next 
        