import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

idx = [0] * (n + 1)
for i in range(n):
    idx[inorder[i]] = i

def preorder(ins, ine, pos, poe):
    if (ins > ine) or (pos > poe):
        return

    root = postorder[poe]
    left = idx[root] - ins
    right = ine - idx[root]

    print(root, end=" ")
    preorder(ins, ins + left - 1, pos, pos + left - 1)
    preorder(ine - right + 1, ine, poe - right, poe - 1)

preorder(0, n - 1, 0, n - 1)