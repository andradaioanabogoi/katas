class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def isBalanced(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if(abs(left_height - right_height) <= 1) and isBalanced(root.left) is True and isBalanced(root.right) is True:
        return True

    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)

print(isBalanced(root))

# Time Complexity: O(n^2) Worst case occurs in case of skewed tree.

# Optimized implementation: Above implementation can be optimized
# by calculating the height in the same recursion rather
# than calling a height() function separately.
# reduces time complexity to O(n).


# utility class to pass height object
class Height:
    def __init__(self):
        self.height = 0

# helper function to check if binary
# tree is height balanced


def betterIsBalanced(root, height):

    # left_height and right_height to store height of
    # left and right subtree
    left_height = Height()
    right_height = Height()

    # Base condition when tree is
    # empty return true
    if root is None:
        return True

    # l and r are used to check if left
    # and right subtree are balanced
    l = betterIsBalanced(root.left, left_height)
    r = betterIsBalanced(root.right, right_height)

    # height of tree is maximum of
    # left subtree height and
    # right subtree height plus 1
    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    # if we reach here then the tree
    # is not balanced
    return False


height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)

if betterIsBalanced(root, height):
    print('Tree is balanced')
else:
    print('Tree is not balanced')
