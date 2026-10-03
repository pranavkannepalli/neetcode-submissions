# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        sen = ListNode()
        end = sen

        while c1 != None and c2 != None:
            if c1.val < c2.val:
                end.next = c1
                c1 = c1.next
                end = end.next
            else:
                end.next = c2
                c2 = c2.next
                end = end.next
        
        if c1 != None:
            end.next = c1
        elif c2 != None:
            end.next = c2
        
        return sen.next