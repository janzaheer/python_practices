class Node(object):

    def __init__(self, data=None, next_data=None):
        self.data = data
        self.next_data = next_data


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def listprint(self):
        current = self.head
        # print all the data while head is empty
        # print current data and set next_data to current
        while current:
            print(current.data)
            current = current.next_data

    def begining_insert(self, new_data):
        """
        'Mon', 'Tue', 'Wed' already in LinkedList
        'beginning_insert('Sun')
        => new_node = Node('Sun')
        new_node is 'Sun', and the new_node.next is None
        add new_node.next = head (where now the head is Mon)
        So 'Mon' goes to the next node of 'Sun'
        => new_node.next = 'Mon'
        make the head now 'Sun'
        => head = 'Sun'
        So now the result would be ['Son', 'Mon', 'Tue', 'Wed']
        """
        # move the previous head into new next data
        # and add the new data into head
        new_node = Node(data=new_data)
        new_node.next_data = self.head
        self.head = new_node

    def insert_between(self, middle_node, new_data):
        """
        'Mon', 'Tue', 'Wed', 'Fri' already in LinkedList
        middle_node = Wed
        new_data = Thu
        new_node('Thu')
        new_node next is empty
        middle_node next is 'Fri'
        put 'Fri' into new node next
        => new_node.next_data = middle_node.next
        and make middle.next as 'Thu'
        => middle.next = new_data
        """
        if not middle_node:
            print("Enter the Middle Node")
            return

        new_node = Node(new_data)
        new_node.next_data = middle_node.next_data
        middle_node.next_data = new_node

    def end_insert(self, new_data):
        """
        'Mon', 'Tue', 'Wed' already in LinkedList
        end_insert('Fri')
        => new_node = 'Fri'
        head would be 'Mon', if there is no head then setup head as 'Fri'
        => head = new_node
        head is 'Mon' and next is 'Tue'
        so run a loop until head becomes None
        once it becomes None add the new_data next to last one 'Wed'
        last.next_data = 'Sun'
        """
        new_node = Node(data=new_data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next_data:
            last = last.next_data

        last.next_data = new_node

    def remove_node(self, remove_data):
        head_val = self.head
        if head_val:
            if head_val.data == remove_data:
                self.head = head_val.next_data
                head_val = None
                return

        while head_val:
            if head_val.data == remove_data:
                break

            prev = head_val
            head_val = head_val.next_data

        if not head_val:
            return

        prev.next_data = head_val.next_data
        head_val = None

    def search(self, search_data):
        current = self.head
        found = False
        while current and found is False:
            if current.data == search_data:
                found = True
            else:
                current = current.next_data

        if current is None:
            raise ValueError('Data not in the List')

        print ('Search data is %s' % current.data)

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_data

        print ('Size if LinkedList is %d' % count)


ll = LinkedList()
ll.head = Node(data='Mon')
e2 = Node(data='Tue')
e3 = Node(data='Wed')

ll.head.next_data = e2

e2.next_data = e3

ll.begining_insert(new_data='Sun')
ll.end_insert(new_data='Fri')
ll.insert_between(e2.next_data, new_data='Thu')

# ll.remove_node(remove_data='Thu')

ll.search(search_data='Mon')

ll.size()


ll.listprint()
