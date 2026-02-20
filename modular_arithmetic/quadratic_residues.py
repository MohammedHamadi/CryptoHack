# Quadratic Residues and Non-Residues
#
# An integer x is a Quadratic Residue if there exists an a such that a^2 ≡ x mod p.
# If there is no such solution, then the integer is a Quadratic Non-Residue.
# If a^2 = x then (-a)^2 = x. So if x is a quadratic residue in some finite field,
# then there are always two solutions for a.

p = 29
ints = [14,6,11]

for i in range(29):
    if i*i % p in ints:
        print(min(i%p, -i%p))
        break