# You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
# Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, 
# as long as the tree remains a BST after insertion. You can return any of them.

# Example 2:
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]

# Example 3:
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
####################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
        def insert(root, key):
            if root is None:
                return TreeNode(val)
            temporary_node = TreeNode(key) 
            
            #Finding the parent node who is going to have child as temp_node
            parent = None
            curr = root
            while curr is not None:
                parent = curr
                if curr.val > key:
                    curr = curr.left
                else:
                    curr = curr.right

            # if the key is smaller than value
            # this will make value in the left node else right node
            if parent.val > key:
                parent.left = temporary_node
            else:
                parent.right = temporary_node
            
            return root
        
        return insert(root, val)