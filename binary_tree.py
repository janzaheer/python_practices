class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, new_data):
        if self.data:
            if new_data < self.data:
                if self.left is None:
                    self.left = Node(new_data)
                else:
                    self.left.insert(new_data)
            elif new_data > self.data:
                if self.right is None:
                    self.right = Node(new_data)
                else:
                    self.right.insert(new_data)
        else:
            self.data = new_data

    def search(self, search_val):
        if search_val < self.data:
            if self.left is None:
                return "%d Not Found" % search_val
            return self.left.search(search_val)
        elif search_val > self.data:
            if self.right is None:
                return "%d Not Found" % search_val
            return self.right.search(search_val)
        else:
            return '%d is Found !!!' % search_val

    def print_tree(self):
        if self.left:
            self.left.print_tree()

        print(self.data)

        if self.right:
            self.right.print_tree()

    # In Order Traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        result = []
        if root:
            result = self.inorderTraversal(root.left)
            result.append(root.data)
            result = result + self.inorderTraversal(root.right)
        return result

    # Pre Order Traversal
    # Root -> Left -> Right
    def preOrderTraversal(self, root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.preOrderTraversal(root.left)
            result = result + self.preOrderTraversal(root.right)

        return result

    # Post Order Traversal
    # Left -> Right -> Root
    def postOrderTraversal(self, root):
        result = []
        if root:
            result = self.postOrderTraversal(root.left)
            result = result + self.postOrderTraversal(root.right)
            result.append(root.data)

        return result


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print "Print the Tree"
print root.search(2)
print root.print_tree()
print "In Order Traversal"
print root.inorderTraversal(root)
print "Pre Order Traversal"
print root.preOrderTraversal(root)
print "Post Order Traversal"
print root.postOrderTraversal(root)
