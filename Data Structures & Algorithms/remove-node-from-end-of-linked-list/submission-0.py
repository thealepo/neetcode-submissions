# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)

        ptr = head
        for _ in range(n):
            ptr = ptr.next

        prev , node = dummy , head
        while ptr:
            prev = node
            node = node.next
            ptr = ptr.next

        # now, node is in the removal spot
        # and prev is in node.prev
        prev.next = node.next
        return dummy.next