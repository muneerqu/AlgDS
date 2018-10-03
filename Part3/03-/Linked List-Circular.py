#
#
#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.counter = 0
        self.head = None

    def add_node(self, node):
        if self.counter == 0:
            self.add_at_begining(node)
        else:
            self.add_at_end(node)

    def add_at_begining(self, node):
        self.head = node
        node.next = self.head
        self.counter += 1

    def add_at_end(self, node):
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = node
        node.next = self.head
        self.counter += 1

    def print_list(self):
        node = self.head
        if self.counter == 1:
            print(node.data)
        else:
            print(node.data)
            node = node.next
            while node != self.head:
                print(node.data)
                node = node.next


def main():
    print('This is main function')
    mylist = LinkedList()
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)
    mylist.add_node(n1)
    mylist.add_node(n2)
    mylist.add_node(n3)
    mylist.add_node(n4)
    mylist.add_node(n5)
    mylist.print_list()


if __name__ == '__main__':
    main()
