# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val 
# and return the subtree rooted with that node. 
# If such a node does not exist, return null.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    @staticmethod ##means we can call it without creating an object
    def searchBST(root: TreeNode, val: int):
        curr = root
        #value = target
        while curr is not None:
            
            if curr.val==val:
                return curr
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right

        return curr
    

## root = [4,2,7,1,3], val = 2 ###
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7)
val = 2

search = Solution.searchBST(root, 2)

print(search.val if search else "couldn't fin the node")