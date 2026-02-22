def modular_sqrt_tonelli_shanks(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.

        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.

        0 is returned is no square root exists for
        these a and p.

        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

def legendre_symbol(a, p):
    
    """ Compute the Legendre symbol a|p using
        Euler's criterion. p is a prime, a is
        relatively prime to p (if p divides
        a, then a|p = 0)

        Returns 1 if a has a square root modulo
        p, -1 otherwise.
    """
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def extended_gcd(a, b):
    """
    The Extended Euclidean Algorithm.
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a,m):
    """
    Returns the modular inverse of a modulo m.
    """
    gcd, x, y = extended_gcd(a,m)
    if gcd != 1:
        raise Exception("Modular inverse does not exist (moduli are not coprime).")
    else:
        return x%m

def chinese_remainders(remainders, moduli):
    """
    Algorithm: Constructive Chinese Remainder Theorem (CRT)
    @input: remainders=list(int) size n, moduli=list(int) size n
    @output: a, st x = a mod N
    Purpose:
    Solves a system of k congruences of the form:
    x ≡ a_i (mod m_i) for i = 1 to k.

    Preconditions:
    - You have a list of remainders [a_1, a_2, ..., a_k].
    - You have a list of moduli [m_1, m_2, ..., m_k].
    - All moduli must be pairwise coprime (gcd(m_i, m_j) = 1 for all i != j).

    Steps:
    1. Calculate the Global Modulus (M):
    - Multiply all the individual moduli together.
    - M = m_1 * m_2 * ... * m_k
    
    2. Initialize a running total for the solution:
    - x_total = 0
    
    3. Iterate through each congruence equation (for each index i):
    a. Extract the current remainder (a_i) and modulus (m_i).
    
    b. Calculate the Partial Product (M_i):
        - M_i is the global modulus M divided by the current modulus m_i.
        - M_i = M // m_i 
        - (Essentially, M_i is the product of all *other* moduli).
        
    c. Compute the Modular Inverse (y_i):
        - Find the modular inverse of M_i modulo m_i.
        - Solve for y_i such that: (M_i * y_i) ≡ 1 (mod m_i).
        - (This step requires a separate function, typically the Extended 
            Euclidean Algorithm).
        
    d. Calculate the Term for this Congruence:
        - Multiply the remainder, the partial product, and the inverse.
        - term_i = a_i * M_i * y_i
        
    e. Add the term to the running total:
        - x_total += term_i
        
    4. Compute the Final Solution (x):
    - The unique solution modulo M is the running total modulo M.
    - x = x_total % M
    - Return x.
    """
    # Step 1: Calculate the global modulo M.
    # M is the product of all the individual moduli (m_1 * m_2 * ... * m_k).
    total_M = 1
    for m in moduli:
        total_M *= m
        
    x = 0
    
    # Iterate through each congruence equation
    for i in range(len(remainders)):
        a_i = remainders[i]
        m_i = moduli[i]
        
        # Step 2: Calculate the partial products M_i.
        # M_i is the global M divided by the specific modulo m_i for this row.
        M_i = total_M // m_i
        
        # Step 3: Find the modular inverses y_i.
        # y_i is the modular inverse of M_i modulo m_i.
        # We use the Extended Euclidean Algorithm helper function here.
        y_i = mod_inverse(M_i, m_i)
        
        # Step 4: Construct the final solution x.
        # Multiply the target remainder (a_i), the partial product (M_i), 
        # and the inverse (y_i), then add it to our running total.
        x += (a_i * M_i * y_i)
        
    # Finally, take the combined result modulo the global M 
    # to return the smallest positive integer solution.
    return x % total_M

