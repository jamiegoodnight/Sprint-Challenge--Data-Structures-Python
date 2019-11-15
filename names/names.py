import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # def insert(self, value):
    #     # < go left
    #     if self.value > value:

    #     # >= go right
    def insert(self, value):
        if self.value > value:
            """LEFT"""
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            """RIGHT"""
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # To search a given key in Binary Search Tree, we first compare it with root,
        # if the key is present at root, we return root. If key is greater than root's key,
        # we recur for right subtree of root node. Otherwise we recur for left subtree.
        if self.value == target:
            return True

        if self.value > target:
            """LEFT"""
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            """RIGHT"""
            if not self.right:
                return False
            else:
                return self.right.contains(target)
    # Return the maximum value found in the tree

    def get_max(self):
        # Go right until you can go right no further
        # if not self.right:
        #     return self.value <----- VALUE
        # else:
        #     self.right.get_max()

        current = self
        max_value = self.value

        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value

        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach

    def for_each(self, cb):
        # visit every node exactly one time
        # go left until you can't anymore, then
        # go back and go right
        # in here somewhere, you want to call cb(node)
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# b=BinarySearchTree(names_1[0])
# for n1 in names_1:
#     b.insert(n1)
#     b.for_each(sdfsdfsdfs)

b = BinarySearchTree(names_1[0])
duplicates = []
for n1 in names_1:
    b.insert(n1)
for n2 in names_2:
    if b.contains(n2):
        duplicates.append(n2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
