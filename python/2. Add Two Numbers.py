# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)




class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        current_num1 = l1
        while current_num1:
            num1 += str(current_num1.val)
            current_num1 = current_num1.next

        num2 = ''
        current_num2 = l2
        while current_num2:
            num2 += str(current_num2.val)
            current_num2 = current_num2.next

        num1, num2 = int(num1[::-1]), int(num2[::-1])
        
        res = num1 + num2

        res_string = str(res)[::-1]

        linked_res = ListNode(res_string[0])
        curr = linked_res
        for digit in res_string[1:]:
            curr.next = ListNode(digit)
            curr = curr.next

        return linked_res

res = Solution().addTwoNumbers(l1, l2)


current = res
while current:
    print(current.val)
    current = current.next