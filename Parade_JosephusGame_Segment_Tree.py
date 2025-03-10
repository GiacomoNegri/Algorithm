import math
class Tree:
    def __init__(self, length:int):
        power=(2**(math.ceil(math.log2(length))+1))
        self.n=power//2
        self.tree=[0]*power

        for i in range(length):
            self.tree[i+self.n]=1
        
        for i in range(self.n-1, 0,-1):
            self.tree[i]=self.tree[i*2]+self.tree[i*2+1]
    
    def find_position(self,k):
        i=1
        s=k
        if self.tree[i]<s:
            return None
        
        while i < self.n:
            if self.tree[2*i]>=s:
                i*=2
            else:
                s-=self.tree[2*i]
                i=i*2+1
        return i-self.n

    def update(self,pos):
        j=pos+self.n
        self.tree[j]=0
        while j>=1:
            j//=2
            self.tree[j]=self.tree[2*j]+self.tree[2*j+1]
        

def order(n, steps):
    tree=Tree(n)
    results=[0]*n
    soldiers=[i for i in range(1,n+1)]

    for i in range(n-1, -1, -1):
        
        pos=tree.find_position(i-steps[i]+1)
        results[i]=soldiers[pos]
        tree.update(pos)

    print(" ".join([str(i) for i in results]))


n=int(input())
l=[int(x) for x in input().split()]

order(n,l)