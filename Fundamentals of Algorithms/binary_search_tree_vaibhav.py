class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()

    def find(self, value):
        if self.value > value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif self.value < value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True
        

b = TreeNode(5)
b.insert(4)
b.insert(3)
b.insert(2)
b.inorder()
print(b.find(7))


