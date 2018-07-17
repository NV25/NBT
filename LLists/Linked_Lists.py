class LinkedListNode:
    def __init__(self, key=None, value):
        self.value = value
        self.next = None
        if key:
            self.key = key


class LinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None


    def _get_head(self):
        return self.head

    def _get_tail(self):
        return self.tail

    def _add_node_head(self, key, value):
        new_node = LinkedListNode(key, value)

        if self.head:
            new_node.next = self.head
        else:
            self.tail = new_node

        self.head = new_node
        return self.head

    def _add_node_tail(self, key, value):
        new_node = LinkedListNode(key, value)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        return self.head

    def _add_node_index(self, r, key, value):
        new_node = LinkedListNode(key, value)

        cur = self.head
        prev = None
        len = 0

        while cur != None:
            if len == r:
                if prev:
                    prev.next = new_node

                new_node.next = cur
                return self.head

            prev = cur
            cur = cur.next

        # If node to be added at the end
        if cur == None:
            self.head = self._add_node_tail(key, value)

        return self.head

    def _delete_node_head(self):
        return

    def _delete_node_tail(self):
        return

    def _delete_node(self, node):
        return

    def _delete_node_value(self, value):
        return

    def _delete_node_index(self):
        return

    def _reverse_linked_list(self):
        return


    """
    Cycle Detection
    """

    def _find_mid(self):
        slow = self.head
        fast = self.head

        while fast != None or fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _is_loop_present(self):
        slow = self.head
        fast = self.head.next

        while fast != None or fast.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False

    def _find_loop_len(self):
        return

    def _find_loop_start(self):
        return

    """
    Zip problems
    1. Given an integer singly linked list, zip it from its two ends
    2. Zip two separate lists and unzip them back into original lists
    """



    """
    Sort problems
    1. Dutch Flag sort
    2. Merge Sort
    3. Insertion Sort
    4. Bubble sort
    """


    """
    Flatten list
    """

    """
    Arithmetic Operations on lists
    1. Add 2 numbers
    2. Subtract 2 numbers
    """






