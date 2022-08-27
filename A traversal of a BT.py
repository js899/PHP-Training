# OUTPUT A traversal: 8 4 2 1 3 7 12 i.e. inverted left view to root to right view
#          1
#      2          3
#   4    5     6     7
#    9      13 12
from collections import deque
class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def A_traversal(root):
    finalList = []
    # pass left subtree, get the left view
    # pass right subtree, get the right view
    # In a tree like
    #          1
    #      2       3
    #   4     6   8
    #  5     7
    # output desired: 5 4 2 1 3 8 7
    # OR use level order traversal to get the first and last nodes of a level, if the same node
    # makes up for the first and the last node, do not repeat it for the right side. Like:
    #           1
    #       2       3
    #   4
    #5    x
    # output desired: 5 4 2 1 3(if 6 is absent)
    # output desired: 5 4 2 1 3 4 6(if 6 is present)
    return finalList

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
root.left.left.right = node(9)
root.right.left.right = node(12)
root.right.left.left = node(13)
A_traversal(root)

# OUTPUT HEART(looks like something else tho heheh) traversal: 1 2 4 8 9 10 5 6 13 12 7 3 1
#          1
#      2          3
#   4    5     6     7
#      9  10 13 12