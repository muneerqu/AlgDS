# Declaration of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def list_length(self):
        current = self.head
        count = 0
        if self.next != None:
            count = count + 1
            current = self.get_next()
        return count

    def insert_at_begining(self, data):
        new_node = Node()
        new_node = set_data(data)
        if self.length == 0:
            self.head == new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node()
        new_node.set_data(data)
        current = self.head
        while current.get_next() != None:
            current = current.get_next()

        current.set_next(new_node)
        self.length += 1

    def insert_at_middle(self, pos, node):
        count = 0
        current_node = self.head
        previous_node = self.head

        if pos > self.length < pos:
            print("The selected position does't exist")
        else:
            while current_node.next() != None or count < pos:
                count += 1
                if count == pos:
                    previous_node.next = node
                    node.next = current_node
                    self.length += 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next

    def delete_at_beginning(self):
        if self.length == 0:
            print('The list is empty')
        else:
            self.head = self.head.get_next()
            self.length -+ 1

    def delete_at_end(self):
        if self.length == 0:
            print('The list is empty')
        else:
            previous_node = self.head
            current_node = self.head
            while current != None:
                previous_node = current_node()
                current_node = current_node.get_next()
            previous_node.set_next(None)
            self.length -= 1
                

def main():
    print('This is main')


if __name__ == '__main__':
    main()
