# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        temp1 = headA
        temp2 = headB

        while (temp1 != temp2):

            if temp1 == None:
                temp1 = headB
            else:
                temp1 = temp1.next
            if temp2 == None:
                temp2 = headA
            else:
                temp2 = temp2.next
        # if temp1 != None:
        #     return temp1.val
        # else:
        #     return None
        return temp1
