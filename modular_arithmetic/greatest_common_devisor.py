def gcd(a,b, algorithm="euclid"):
    if algorithm == "euclid":
        a,b = max(a,b), min(a,b)
        if a == 0:
            return b
        if b == 0:
            return a
        return gcd(b, a%b)
    else:
        # no other algorithms
        return
print(gcd(66528,52920))