"""Ar tiktok"""
p = input().split(" ")
R = int(p[0])
R = R**2
X = int(p[1])
Y = int(p[2])
CIR = X**2 + Y**2
def cal (r = R,cir=CIR):
    """Cir"""
    if cir < r :
        print("IN")
    elif cir == r :
        print("ON")
    elif cir > r:
        print("OUT")
cal()
