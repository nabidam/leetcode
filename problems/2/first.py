# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self, l1, l2
    ):
        num1 = self.reverse_array_to_number(l1)
        num2 = self.reverse_array_to_number(l2)

        output_num = num1 + num2

        return self.number_to_reverse_array(output_num)

    def reverse_array_to_number(self, array):
        final_number = 0

        idx = 0
        current_node = array
        while current_node is not None:
            this_num = current_node.val
            final_number += this_num * (10**idx)
            idx += 1

            current_node = current_node.next

        return final_number

    def number_to_reverse_array(self, number):
        array = []

        num = number
        while num >= 10:
            array.append(num % 10)

            num //= 10
        array.append(num)

        n = len(array)
        last_node = None
        for i in range(len(array)):
            last_node = ListNode(val=array[n - i - 1], next=last_node)

        return last_node

l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))


l1 = ListNode(val=0)
l2 = ListNode(val=0)
solution = Solution()

print(solution.addTwoNumbers(l1, l2))