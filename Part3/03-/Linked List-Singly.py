#
#


class Node:
    """Class Node to create the linked list node objects"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked list class to perform the linked list operations"""

    def __init__(self):
        self.counter = 0
        self.head = None

    def newNode(self, node):
        if self.counter == 0:
            self.add_at_begining(node)
        else:
            self.add_at_end(node)

    def add_at_begining(self, node):
        self.head = node
        self.counter += 1

    def add_at_end(self, node):
        head = self.head
        while head.next != None:
            head = head.next
        head.next = node
        self.counter += 1

    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, " ")
            node = node.next


def main():
    print('This is main function')
    mylist = LinkedList()
    myNode1 = Node(12)
    mylist.newNode(myNode1)
    myNode2 = Node(15)
    mylist.newNode(myNode2)
    myNode3 = Node(45)
    mylist.newNode(myNode3)
    myNode4 = Node(545)
    mylist.newNode(myNode4)
    myNode5 = Node(458)
    mylist.newNode(myNode5)
    myNode6 = Node(554)
    mylist.newNode(myNode6)
    myNode7 = Node(877)
    mylist.newNode(myNode7)
    mylist.print_list()


if __name__ == '__main__':
    main()
