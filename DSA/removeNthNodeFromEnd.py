# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = head
        temp1 = head

        while (n):
            temp = temp.next
            n -= 1

        if temp == None:
            head = head.next

        else:

            while (temp.next != None):
                temp1 = temp1.next
                temp = temp.next

            temp1.next = temp1.next.next

        return head

