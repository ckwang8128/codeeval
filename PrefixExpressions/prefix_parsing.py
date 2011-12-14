import sys

"""
Classes and methods to parse and evaluate prefix mathematical expressions

Ex: * + 2 3 4 = 4 * (2 + 3) = 20

Method:
1. Turn expression into an expression tree
2. Perform a DFS tree traversal to eval expressions
"""


op_dict = {'+':lambda a, b: a + b,
            '*':lambda a, b: a * b,
            '/':lambda a, b: a / b}
def parse_expr(expr):
    """
    expr is a list of the terms in a prefix-order arithmetic expression
    """
    if not expr:
        return None, None
    first_term = expr[0]
    if is_operator(first_term):
        new_node = BinaryNode(first_term)
        left_tree, rest_of_expr = parse_expr(expr[1:])
        new_node.leftChild = left_tree
        new_node.rightChild, rest_of_expr = parse_expr(rest_of_expr)
        return new_node, rest_of_expr
    else:
        if len(expr) == 1:
            return BinaryNode(first_term), None
        else:
            return BinaryNode(first_term), expr[1:]

def is_operator(key):
        return key in ['+', '*', '/']


class BinaryNode:
    def __init__(self, item, rightChild=None, leftChild=None):
        self.rightChild = rightChild
        self.leftChild = leftChild
        self.item = item
    
    def __str__(self):
        if not is_operator(self.item):
            return str(self.item)
        else:
            return str(self.leftChild) + str(self.item) + str(self.rightChild)

def eval_node(start_node):
    """
    Does a DFS traversal to evaluate the tree. 
    
    """
    if start_node:
        if not is_operator(start_node.item):
            return int(start_node.item)
        else:
            return op_dict[start_node.item](eval_node(start_node.leftChild),
                                            eval_node(start_node.rightChild))
    else:
        return 0

class ExpressionTree:

    def __init__(self, expr):
        self.root, remaining_expr  = parse_expr(expr)
        if remaining_expr:
            print "FAIL: " + remaining_expr + " is not a valid expression"
            return
        

    def eval_tree(self):
        return eval_node(self.root)


    def __str__(self):
        return str(self.root)

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as tests:
        for line in tests:
            expr = line.strip().split(' ')
            expr_tree = ExpressionTree(expr)
            print expr_tree.eval_tree()
