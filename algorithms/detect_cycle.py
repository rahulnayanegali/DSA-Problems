# detect cycle

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


# Individual nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Construction of linkedlist cycle
# [1,2,3,4]
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2


def detect_cycle(head):
    if not head or not head.next:
        return False
    slow = head
    fast = head.next

    while slow != fast:
        if not slow or not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


print(detect_cycle(node1))


