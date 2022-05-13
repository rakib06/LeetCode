# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = None

        def addtoLast(node, value):
            current = node
            if current:
                while current.next != None:
                    current = current.next
                current.next = ListNode(value)
            elif node != None:
                node.val = ListNode(value)
            else:
                node = ListNode(value)
            return node

        L1 = list1
        L2 = list2
        while L1 != None or L2 != None:
            if L1 != None and L2 != None:
                if L1.val <= L2.val:
                    merged_list = addtoLast(merged_list, L1.val)
                    L1 = L1.next
                else:
                    merged_list = addtoLast(merged_list, L2.val)
                    L2 = L2.next
            elif L1 == None and L2 != None:
                merged_list = addtoLast(merged_list, L2.val)
                L2 = L2.next

            elif L1 != None and L2 == None:
                merged_list = addtoLast(merged_list, L1.val)
                L1 = L1.next

        return merged_list
