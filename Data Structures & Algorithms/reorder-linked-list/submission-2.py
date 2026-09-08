# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find mid point first
        slow , fast = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now, slow is the midpoint
        # split the lists
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # 0 -> 1 -> 2 -> 3
        # 6 -> 5 -> 4

        first , second = head , prev
        while second:
            temp1 , temp2 = first.next , second.next
            first.next = second
            second.next = temp1
            first , second = temp1 , temp2



            