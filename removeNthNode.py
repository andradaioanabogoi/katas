class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, "")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node


new_linked_list = LinkedList()

new_linked_list.insert_at_start(Node(3))
new_linked_list.insert_at_start(Node(4))
new_linked_list.insert_at_start(Node(5))
new_linked_list.insert_at_start(Node(6))
new_linked_list.insert_at_start(Node(3))

print(new_linked_list.traverse_list())


# def removeNthFromEnd(head, n) {
#     Node dummy = new Node(0);
#     dummy.next = head;
#     ListNode first = dummy;
#     ListNode second = dummy;
#     // Advances first pointer so that the gap between first and second is n nodes apart
#     for (int i = 1; i <= n + 1; i++) {
#         first = first.next;
#     }
#     // Move first to the end, maintaining the gap
#     while (first != null) {
#         first = first.next;
#         second = second.next;
#     }
#     second.next = second.next.next;
#     return dummy.next;
# }
