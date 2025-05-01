from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_list_head = None

        if not list1:
            new_list_head = list2
        elif not list2:
            new_list_head = list1
        else:
            list1_iter = list1
            list2_iter = list2

            new_list_items = []

            while list1_iter is not None and list2_iter is not None:
                if list1_iter.val < list2_iter.val:
                    while list1_iter is not None and list1_iter.val < list2_iter.val:
                        new_list_items.append(list1_iter.val)
                        list1_iter = list1_iter.next
                elif list2_iter is not None and list1_iter.val > list2_iter.val:
                    new_list_items.append(list2_iter.val)
                    list2_iter = list2_iter.next
                else:
                    new_list_items.append(list1_iter.val)
                    list1_iter = list1_iter.next
                    new_list_items.append(list2_iter.val)
                    list2_iter = list2_iter.next

            if list1_iter:
                while list1_iter:
                    new_list_items.append(list1_iter.val)
                    list1_iter = list1_iter.next
            else:
                while list2_iter:
                    new_list_items.append(list2_iter.val)
                    list2_iter = list2_iter.next

            reversed_list = new_list_items[::-1]
            curr_head = ListNode(reversed_list[0])
            for item in reversed_list[1:]:
                curr_head = ListNode(item, curr_head)

            new_list_head = curr_head

        return new_list_head


solution = Solution()

# tc
tc = [
    (ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))),
    (None, None),
    (None, ListNode()),
    (ListNode(2), ListNode(1)),
    (ListNode(1), ListNode(2)),
]


# tc = [[0, 0, 0]]


def print_llist(head):
    curr = head

    while curr:
        if not curr.next:
            print(curr.val)
        else:
            print(curr.val, end=" --> ")
        curr = curr.next


for list1, list2 in tc:
    print_llist(solution.mergeTwoLists(list1=list1, list2=list2))
