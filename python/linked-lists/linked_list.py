class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = None
        if type(head) == ListNode:
            self.head = head
        elif type(head) == list:
            for item in head:
                self.append(ListNode(item))

    def append(self, node:ListNode):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        else:
            self.head = node

    def pop(self):
        if self.head:
            prev = self.head
            curr = self.head.next
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None

    def insert(self, node:ListNode, pos:int):
        if(pos < 0 or not self.head):
            print("ERROR: INVALID POSITION OR HEAD IS NONE")
        elif pos == 0:
            node.next = self.head
            self.head = node
        else:
            index = 0
            curr = self.head
            while curr.next and index != pos-1:
                curr = curr.next
                index += 1
            node.next = curr.next
            curr.next = node

    def delete(self, pos:int):
        if(pos < 0 or not self.head):
            print("ERROR: INVALID POSITION OR HEAD IS NONE")
        elif pos == 0:
            self.head = self.head.next
        else:
            index = 0
            prev = self.head
            curr = self.head.next
            while curr.next and index != pos-1:
                prev = curr
                curr = curr.next
                index += 1
            prev.next = curr.next

    def printList(self):
        if self.head:
            curr = self.head
            while curr:
                print("{} ".format(curr.val), end="")
                curr = curr.next
            print()