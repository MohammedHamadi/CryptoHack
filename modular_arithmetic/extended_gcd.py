def extended_gcd(a,b):
    a,b=max(a,b),min(a,b)
    if b%(a%b) == 0:
        return [1, -(int(a/b))]
    u,v = extended_gcd(b, a%b)
    c = int(a/b)
    return [v,u-c*v]
p=26513
q=32321
print(extended_gcd(p,q))
