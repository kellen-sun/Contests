import sys

n = int(input())
arr = list(map(int, input().split()))

class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    # Function to insert a node
    def insert_node(self, root, key):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        if y != None:
            T2 = y.left
            y.left = z
            z.right = T2
            z.height = 1 + max(self.getHeight(z.left),
                            self.getHeight(z.right))
            y.height = 1 + max(self.getHeight(y.left),
                            self.getHeight(y.right))
            return y
        return z

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        if y != None:
            T3 = y.right
            y.right = z
            z.left = T3
            z.height = 1 + max(self.getHeight(z.left),
                            self.getHeight(z.right))
            y.height = 1 + max(self.getHeight(y.left),
                            self.getHeight(y.right))
            return y
        return z

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    def getClosest(self, root, val, mindifsofar, valsofar):
        # init call with minsofar = float('inf) and valsofar = root.key
        #if root.key == val:
         #   return root.key
        
        if abs(root.key - val) < mindifsofar:
            mindifsofar = abs(root.key- val)
            valsofar = root.key

        if root.key>val:
            if root.left == None:
                return valsofar
            else:
                return self.getClosest(root.left, val, mindifsofar, valsofar)
        else:
            if root.right == None:
                return valsofar
            else:
                return self.getClosest(root.right, val, mindifsofar, valsofar)


rightTree = AVLTree()
rightroot = None
for i in range(len(arr[1:])):
    rightroot = rightTree.insert_node(rightroot, arr[i+1])
rightroot = rightTree.insert_node(rightroot, 0)
leftTree = AVLTree()
leftroot = None
leftroot = leftTree.insert_node(leftroot, 0)

sumleft = 0
sumright = sum(arr[1:])

indexLookup = [0 for i in range(int(1e6+5))]
for i in range(len(arr)):
    if indexLookup[arr[i]] == 0:
        indexLookup[arr[i]] = [i]
    else:
        indexLookup[arr[i]].append(i)

# at each possible lookup value we have a sorted array of possible indices leading there

mins = float('inf')
curIndex = -1
trueFound = -1

for i in range(n):
    if sumright == sumleft:
        mins = 0
        curIndex = -2
        trueFound = i+1
        break
    toFind = (sumright - sumleft)/2.0
    leftright = -1 # 0 for search in right, 1 for search in left
    f2 = False
    if toFind > 0: 
        found1 = rightTree.getClosest(rightroot, toFind, float('inf'), rightroot.key)
        leftright = 0
        dif = 2*(toFind - found1)# round to make int?
        if found1 != toFind:
            found2 = rightTree.getClosest(rightroot, 2*toFind-found1, float('inf'), rightroot.key)
            if found2 == 2*toFind - found1:
                f2 = True
    else:
        found1 = leftTree.getClosest(leftroot, -toFind, float('inf'), leftroot.key)
        leftright = 1
        dif = 2*(-toFind - found1) # round to make int?
        if found1 != -toFind:
            found2 = leftTree.getClosest(leftroot, 2*-toFind - found1, float('inf'), leftroot.key)
            if found2 + found1 + 2*toFind == 0:
                f2 = True

    #print(i+1, dif, found1, toFind)


    if abs(dif)<mins:
        #print(abs(dif), i+1)
        if found1 == 0:
            mins = abs(dif)
            trueFound = i+1
            curIndex = -2
            continue
        mins = abs(dif)
        trueFound = i+1
        toConsider = indexLookup[found1]
        #from toConsider find smallest index greater than i (if leftright == 0)
        # otherwise we want smallest index
        # logn time by binary search
        if leftright == 0:
            a,b = 0, len(toConsider)-1
            if toConsider[a]>i:
                curIndex = toConsider[a]
            else:
                while a<=b:
                    c = (a+b)//2
                    #print(a,b)
                    if (toConsider[c+1]>i and toConsider[c]<=i):
                        break
                    elif a+1 == c:
                        if (toConsider[a+1]>i and toConsider[a]<=i):
                            c = a
                            break
                    elif toConsider[c] > i:
                        b = c+1
                    else:
                        a = c
                curIndex = toConsider[c+1]
        else:
            curIndex = toConsider[0]
        
        if f2:
            toConsider = indexLookup[found2]
            if leftright == 0:
                a,b = 0, len(toConsider)-1
                if toConsider[a]>i:
                    curIndex = min(curIndex, toConsider[a])
                else:
                    while a<=b:
                        c = (a+b)//2
                        #print(a,b)
                        if (toConsider[c+1]>i and toConsider[c]<=i):
                            break
                        elif a+1 == c:
                            if (toConsider[a+1]>i and toConsider[a]<=i):
                                c = a
                                break
                        elif toConsider[c] > i:
                            b = c+1
                        else:
                            a = c
                    curIndex = min(curIndex, toConsider[c+1])
            else:
                curIndex = min(curIndex, toConsider[0])
        if dif == 0:
            break
    
    
    if i==n-1:
        break
    sumleft += arr[i]
    sumright -= arr[i+1]
    rightroot = rightTree.delete_node(rightroot, arr[i+1])
    leftroot = leftTree.insert_node(leftroot, arr[i])
print(trueFound, curIndex+1)