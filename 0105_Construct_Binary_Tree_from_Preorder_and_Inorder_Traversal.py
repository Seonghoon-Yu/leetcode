class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            
            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[0:idx])
            node.right = self.buildTree(preorder, inorder[idx+1:])
            
            return node
