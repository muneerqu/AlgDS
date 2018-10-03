#
#
# Doubly Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def add_node(self, node):
        if self.counter == 0:
            self.add_at_begining(node)
        else:
            self.add_at_end(node)

    def add_at_begining(self, node):
        self.head = node
        node.previous = self.head
        self.counter += 1

    def add_at_end(self, node):
        last = self.head
        while last.next != None:
            last = last.next
        last.next = node
        node.previous = last
        self.counter += 1

    def print_list(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

    def add_at_middle(self, node, position):
        if position > self.counter or position < 0:
            print('Position is out of rainge')
        elif position == self.counter:
            print('You are adding the the end of the list, no position needed')
            self.add_at_end(node)
        else:
            self.counter += 1
            pnode = self.head
            for _ in range(position-1): # -1 to stop before the position
                pnode = pnode.next
            node.next = pnode.next
            node.previous = pnode
            pnode.next = node
            pnode = node.next
            pnode.previous = node


def main():
    print('This is main function')
    mylist = LinkedList()
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(99)
    n5 = Node(60)
    # n1 = Node(10)
    # n1 = Node(10)
    mylist.add_node(n1)
    mylist.add_node(n2)
    mylist.add_node(n3)
    mylist.add_node(n5)
    mylist.add_at_middle(n4, 4)
    mylist.print_list()


if __name__ == '__main__':
    main()
