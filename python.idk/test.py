# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = 0
        curr = dummy
        carry = 0

        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
        curr.next = listnode(carry % 10)
        carry //= 10
        curr = curr.next
        return dummy.next 
    
l1 = list(map(int, input("Input l1:=").split()))
l2 = list(map(int, input("Input l2:=").split()))

solution = Solution()
result = solution.addTwoNumbers(l1,l2)

print(result)