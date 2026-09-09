"""K.U.Y"""
a,b=map(int,input().split())
p=[n for n in range(max(a,2),b+1) if all(n%i for i in range(2,int(n**0.5)+1))]
if len(p) >= 1:
    print(*p)
print(f"Total primes: {len(p)}")
    