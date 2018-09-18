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
        

def main():
    print('This is main')


if __name__ == '__main__':
    main()
