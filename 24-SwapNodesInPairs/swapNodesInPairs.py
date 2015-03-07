# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        start = head
        
        try:
            while True:
                head.val, (head.next).val = (head.next).val, head.val
                if (head.next).next:
                    head = (head.next).next
                else:
                    break
            return start
        except:
            return start
            
        