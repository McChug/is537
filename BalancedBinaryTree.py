from helpers.BuildTreeFromList import build_tree


def isBalanced(root) -> bool:
    def getBalancedHeight(node):
        if node == None:
            return 0

        left_height = getBalancedHeight(node.left)
        right_height = getBalancedHeight(node.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return getBalancedHeight(root) != -1

# ------------- Tests --------------

vals = [3,9,20,None,None,15,7]
root = build_tree(vals)
print(f"{vals} is {isBalanced(root)}")

vals = [1,2,2,3,3,None,None,4,4]
root = build_tree(vals)
print(f"{vals} is {isBalanced(root)}")

vals = []
root = build_tree(vals)
print(f"{vals} is {isBalanced(root)}")

vals = [1,2,2,3,None,None,3,4,None,None,4]
root = build_tree(vals)
print(f"{vals} is {isBalanced(root)}")