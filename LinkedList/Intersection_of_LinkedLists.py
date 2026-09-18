# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        lenA = 1
        lenB = 1
        while curA!=None:
            curA = curA.next
            lenA += 1
        
        while curB!=None:
            curB = curB.next
            lenB += 1
        
        curA = headA
        curB = headB

        while lenA>lenB:
            curA = curA.next
            lenA -= 1

        while lenB>lenA:
            curB = curB.next
            lenB -= 1
        
        while curA != curB and curA != None and curB != None:
            curA = curA.next
            curB = curB.next
        
        if curA == None or curB == None:
            return None
        return curA
        