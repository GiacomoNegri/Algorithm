class Tree:
    def __init__(self, arr:list, length:int):
        self.n=length
        self.tree=[(float('inf'), -1)]*(2*self.n)

        for i in range(self.n):
            self.tree[i+self.n]=(arr[i],i)
        
        for i in range(self.n-1, 0,-1):
            self.tree[i]=min(self.tree[i*2], self.tree[i*2+1])
        # print(self.tree)

    def find_min(self, left, right):
        start=left+self.n
        end=right+self.n
        min_value=(float('inf'),-1)

        while start<=end:
            if start%2==1:
                min_value=min(min_value, self.tree[start])
                start+=1
            if end%2==0:
                min_value=min(min_value, self.tree[end])
                end-=1
            start//=2
            end//=2
        return min_value[0], min_value[1]

def score(start, end):
    if start>end:
        return None
        
    val, ind=tree.find_min(start, end)
    
    curr_sum=cumulative[end+1]-cumulative[start]
    candidates.append(curr_sum*val)
    
    score(start, ind-1)
    score(ind+1, end)

def score(arr,length):
    cumulative=[0]*(length+1)
    for i in range(length):
        cumulative[i+1]=cumulative[i]+arr[i]
    
    tree=Tree(arr,length)
    stack=[(0,length-1)]
    max_score= -float('inf')

    while stack:
        start, end=stack.pop()
        if start>end:
            continue

        val, ind=tree.find_min(start,end)
        curr_sum=cumulative[end+1]-cumulative[start]
        max_score=max(max_score,curr_sum*val)

        stack.append((start,ind-1))
        stack.append((ind+1,end))
    return max_score
    
z=int(input())
for _ in range(z):
    n=int(input())
    l=[int(x) for x in input().split()]

    print(score(l,n))