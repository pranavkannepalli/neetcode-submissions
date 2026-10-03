# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        sen = ListNode()
        end = sen
        carryOver = False
        
        while l1 != None or l2 != None:
            v1 = 0
            v2 = 0
            if l1 != None:
                v1 = l1.val
            if l2 != None:
                v2 = l2.val

            out = ((v1 + v2) + (1 if carryOver else 0))
            end.next = ListNode(out % 10)
            end = end.next
            if out >= 10:
                carryOver = True
            else:
                carryOver = False
            index += 1

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carryOver:
            end.next = ListNode(1)
        return sen.next