from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get_node_values_list(self) -> list:
        values = []
        while self.next:
            values.append(self.val)
            self = self.next
        values.append(self.val)
        return list(reversed(values))

    def get_node_values_as_number(self) -> int:
        l = self.get_node_values_list()
        value = ""
        for v in l:
            value = value + str(v)
        return int(value)

    def __str__(self):
        return self.get_node_values_list()


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        l1_value = l1.get_node_values_as_number() if l1 else 0
        l2_value = l2.get_node_values_as_number() if l2 else 0
        result = l1_value + l2_value
        result_reversed_list = list(reversed([int(value) for value in str(result)]))
        return result_reversed_list


solution = Solution()


l1_n3 = ListNode(3)
l1_n2 = ListNode(4, l1_n3)
l1_n1 = ListNode(2, l1_n2)

l2_n3 = ListNode(4)
l2_n2 = ListNode(6, l2_n3)
l2_n1 = ListNode(5, l2_n2)
print(solution.addTwoNumbers(l1_n1, l2_n1))
