"""wtf"""
N,K,T=map(int,input().split())
p,c=1,1
while p!=T:
    p=(p-1+K)%N+1
    if p==1:break
    c+=1
print(c)
