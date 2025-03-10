open_type=['(','[','{']
close_type=[')',']','}']

z=int(input())
for _ in range(z):
    seq=list(input())

    def check_parenthesis(sequence):
        stack=[]
        open_len=0
        close_len=0
        
        for par in sequence:
            
            if par in close_type:
                cur_ind=close_type.index(par)
                
                if (not stack) or stack[-1]!=open_type[cur_ind]:
                    return "NO"
                stack.pop()
            else:
                stack.append(par)
                
        if stack:
            return ''.join([close_type[open_type.index(par)] for par in stack[::-1]])
        else:
            return "YES"
    
    print(check_parenthesis(seq))