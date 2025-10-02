# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

##########################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Addition starts from right to left, but in a linked list goes left to right. 
        #We need to reverse the lists to align it with how addition is performed
        # def reverse(head):
        #     prev = None
        #     curr = head

        #     while curr is not None:
        #         next_node = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = next_node
        #     return prev
        
        

        carry = 0
        sum_value = 0
        # Iterate till either num1 is not empty or num2 is
        # not empty or carry is greater than 0
        res = None
        while l1 is not None or l2 is not None or carry != 0:
            sum_value = carry

            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next

            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next
                
            new_node = ListNode(sum_value % 10)

            carry = sum_value // 10

            if res is None:
                res = new_node
                curr = new_node
            else: ##append the created node to the current
                curr.next = new_node
                curr = curr.next

        return res



