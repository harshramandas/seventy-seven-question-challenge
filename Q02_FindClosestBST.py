class AVLTree:

    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.height = 1
            self.left = None
            self.right = None
        def __str__(self):
            return str(self.data)

    def height(self, current):
        if current == None:
            return 0
        else:
            return current.height

    def balance(self, current):
        if current == None:
            return 0
        else:
            return self.height(current.left) - self.height(current.right)

    def llrotation(self, current):
        temp = current
        current = current.left
        temp.left = current.right
        current.right = temp
        current.height += 1
        current.right.height -= 1
        return current

    def lrrotation(self, current):
        current.left = self.rrrotation(current.left)
        current = self.llrotation(current)
        return current

    def rrrotation(self, current):
        temp = current
        current = current.right
        temp.right = current.left
        current.left = temp
        current.height += 1
        current.left.height -= 1
        return current

    def rlrotation(self, current):
        current.right = self.llrotation(current.right)
        current = self.rrrotation(current)
        return current

    def insert(self, data):
        if self.root == None:
            self.root = self.Node(data)
        else:
            self.root = self._insert(data, self.root)

    def _insert(self, data, current):
        if current == None:
            return self.Node(data)
        if data < current.data:
            current.left = self._insert(data, current.left)
        else:
            current.right = self._insert(data, current.right)
        current.height = max(self.height(current.left), self.height(current.right)) + 1
        balance = self.balance(current)
        if balance > 1:
            if data < current.left.data:
                current = self.llrotation(current)
            else:
                current = self.lrrotation(current)
        elif balance < -1:
            if data > current.right.data:
                current = self.rrrotation(current)
            else:
                current = self.rlrotation(current)
        current.height = max(self.height(current.left), self.height(current.right)) + 1
        return current
    
    def delete(self, data):
        if not self.root:
            return
        else:
            self.root = self._delete(self.root, data)
    
    def _delete(self, current, data):
        if current == None:
            return None
        else:
            if data < current.data:
                current.left = self._delete(current.left, data)
            elif data > current.data:
                current.right = self._delete(current.right, data)
            else:
                if current.left == None and current.right == None:
                    return None
                elif current.right == None:
                    current = current.left
                elif current.left == None:
                    current = current.right
                else:
                    if current.left.right == None:
                        current.left.right = current.right
                        current = current.left
                    else:
                        temp = current
                        current = current.left.right
                        temp.left.right = current.right
                        current.right = temp.right
                        current.left = temp.left
                        current.left.height = max(self.height(current.left.left),self.height(current.left.right)) + 1
                        
            current.height = max(self.height(current.left),self.height(current.right)) + 1
            return current

L = AVLTree()

n = int(input("No. of elements: "))
for i in range(n):
    L.insert(int(input("Element: ")))

target = int(input("Target: "))
min_diff = 999999999999
min_diff_key = -1
K = L.root
while K != None:
    if K.data == target:
        min_diff = 0
        min_diff_key = K.data
        break
    elif K.data < target:
        if abs(K.data - target) < min_diff:
            min_diff = abs(K.data - target)
            min_diff_key = K.data
        K = K.right
    else:
        if abs(K.data - target) < min_diff:
            min_diff = abs(K.data - target)
            min_diff_key = K.data
        K = K.left
print("Closest element to target: ",min_diff_key) 