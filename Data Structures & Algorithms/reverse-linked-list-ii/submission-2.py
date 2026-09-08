# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        left_prev , curr = dummy , head

        # put left pointer in left spot
        for _ in range(left - 1):
            left_prev = curr
            curr = curr.next

        # reverse the space between left and right
        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # stitching together lists
        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next




