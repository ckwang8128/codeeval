import sys


class BinaryNode:
    def __init__(self, item, rightChild=None, leftChild=None):
        self.rightChild = rightChild
        self.leftChild = leftChild
        self.item = item
    
class BinaryTree:

    
    def __init__(self, b_node = None):
        self.root = b_node

    def insert(self, key):
        node = BinaryNode(key)
        if not self.root:

            self.root = node
        else:
            cur_node = self.root
            while (node.item > cur_node.item 
                   and cur_node.rightChild) or (node.item <= cur_node.item  
                                                and cur_node.leftChild):
                  if node.item > cur_node.item:

                      cur_node = cur_node.rightChild
                  else:

                      cur_node = cur_node.leftChild
            if node.item > cur_node.item:
                cur_node.rightChild = node
            else:

                cur_node.leftChild = node

    def find(self, key):
        cur_node = self.root
        while cur_node:
            if key > cur_node.item:
                cur_node = cur_node.rightChild
            elif key < cur_node.item:
                cur_node = cur_node.leftChild
            else:
                return True
        return False

    
def find_lowest_ancestor(bin_tree, key1, key2):
    if ((BinaryTree(bin_tree.root.leftChild).find(key1)
        and BinaryTree(bin_tree.root.rightChild).find(key2)) or
        (BinaryTree(bin_tree.root.leftChild).find(key2)
        and BinaryTree(bin_tree.root.rightChild).find(key1))):
        return bin_tree.root.item
    else:
        if BinaryTree(bin_tree.root.leftChild).find(key1):

            return find_lowest_ancestor(BinaryTree(bin_tree.root.leftChild), key1, key2)
        elif BinaryTree(bin_tree.root.rightChild).find(key1):

            return find_lowest_ancestor(BinaryTree(bin_tree.root.rightChild), key1, key2)
        else:
            return None

if __name__ == '__main__':
    bin_tree = BinaryTree()
    for key in [30,8,52,3,20,10,29]:
        bin_tree.insert(key)
    with open(sys.argv[1], 'r') as tests:
        for line in tests:
            keys = map(int, line.strip().split(' '))
            print find_lowest_ancestor(bin_tree, keys[0], keys[1])
