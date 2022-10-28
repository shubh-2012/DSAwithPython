# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()

        temp = head
        carry = 0

        while (l1 and l2):
            add = l1.val + l2.val + carry

            if add < 9:

                temp.val = add
                carry = 0
            else:

                temp.val = add % 10
                carry = add // 10

            l1 = l1.next
            l2 = l2.next

            if ((l1 != None) or (l2 != None)) or carry != 0:
                temp.next = ListNode()
                temp = temp.next

        while (l1):
            add = l1.val + carry

            if add < 9:

                temp.val = add
                carry = 0
            else:

                temp.val = add % 10
                carry = add // 10

            l1 = l1.next

            if l1 != None or carry != 0:
                temp.next = ListNode()
                temp = temp.next

        while (l2):
            add = l2.val + carry

            if add < 9:

                temp.val = add
                carry = 0
            else:

                temp.val = add % 10
                carry = add // 10

            l2 = l2.next

            if l2 != None or carry != 0:
                temp.next = ListNode()
                temp = temp.next

        if carry != 0:
            temp.val = carry

        return head
