
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        temp = ListNode()

        head = temp

        temp1 = list1
        temp2 = list2
        if temp1== None and temp2 == None:
            return None

        while(temp1 and temp2):

            if temp1.val <= temp2.val:
                temp.val = temp1.val
                temp1 = temp1.next

            else:
                temp.val = temp2.val
                temp2 = temp2.next

            temp.next = ListNode()
            temp = temp.next

        while(temp1):
            temp.val = temp1.val
            temp1 = temp1.next

            if temp1 != None:
                temp.next = ListNode()
                temp = temp.next

        while(temp2):
            temp.val = temp2.val
            temp2 = temp2.next
            if temp2 != None :
                temp.next = ListNode()
                temp = temp.next


        return head