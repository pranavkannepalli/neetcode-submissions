# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sen = ListNode()
        sen.next = head
        
        slow = sen
        fast = sen
        for i in range(n):
            fast = fast.next
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next

        print(slow.val, fast.val)
        slow.next = slow.next.next

        return sen.next