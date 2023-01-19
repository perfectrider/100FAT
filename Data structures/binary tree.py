
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    '''Binary Tree'''

    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        '''Print method LNR. For switch to RNL, call recursion with node.right firstly'''
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)


a = [10, 5, 7, 16, 13, 2, 20]

t1 = Tree()
for x in a:
    t1.append(Node(x))

t1.show_tree(t1.root)




