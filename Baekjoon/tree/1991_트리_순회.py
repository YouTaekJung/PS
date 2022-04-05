class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


n = int(input())
d = {}
li = []
root = None
for i in range(n):
    data, left, right = input().split()
    d[data] = Node(data)
    if i == 0:
        root = d[data]
    li.append([data, left, right])

for l in li:
    if l[1] != '.':
        d[l[0]].left = d[l[1]]
    if l[2] != '.':
        d[l[0]].right = d[l[2]]

def preorder(node):
    print(node.data, end='')
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)
preorder(root)
print()

def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.data, end='')
    if node.right:
        inorder(node.right)
inorder(root)
print()

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.data, end='')
postorder(root)