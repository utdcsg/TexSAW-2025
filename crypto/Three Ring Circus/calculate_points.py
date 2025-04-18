#!/usr/bin/env python3

# Curve parameters
p1, a1, b1 = 1019, 11, 19
G1 = (712, 495)

p2, a2, b2 = 1031, 7, 13
G2 = (371, 219)

p3, a3, b3 = 1033, 23, 11
G3 = (667, 532)

# The new secret key
SECRET_KEY = 29478365012847596

def point_add(P, Q, a, p):
    """Add two points on an elliptic curve."""
    if P is None: return Q
    if Q is None: return P
    
    x1, y1 = P
    x2, y2 = Q
    
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    
    if x1 == x2 and y1 == y2:
        lam = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
    
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    
    return (x3, y3)

def point_multiply(P, k, a, p):
    """Multiply a point P by scalar k using double-and-add algorithm."""
    if k == 0 or P is None:
        return None  # Return the point at infinity
    
    if k < 0:
        # Negative scalar multiplication: multiply by |k| and negate the result
        x, y = point_multiply(P, -k, a, p)
        return (x, (-y) % p)
    
    # Double-and-add algorithm
    result = None  # Start with the point at infinity
    addend = P
    
    while k:
        if k & 1:  # If the bit is set
            result = point_add(result, addend, a, p)
        addend = point_add(addend, addend, a, p)
        k >>= 1
    
    return result

def find_point_order(P, a, p):
    """Find the order of a point P on an elliptic curve."""
    if P is None:
        return 1  # The point at infinity has order 1
    
    Q = P
    n = 1
    
    while True:
        Q = point_add(Q, P, a, p)
        n += 1
        
        if Q is None:  # We've reached the point at infinity
            return n

# Calculate the orders
order1 = find_point_order(G1, a1, p1)
order2 = find_point_order(G2, a2, p2)
order3 = find_point_order(G3, a3, p3)

# Calculate the public points using the modular reductions of the key
k1 = SECRET_KEY % order1
k2 = SECRET_KEY % order2
k3 = SECRET_KEY % order3

P1 = point_multiply(G1, k1, a1, p1)
P2 = point_multiply(G2, k2, a2, p2)
P3 = point_multiply(G3, k3, a3, p3)

print(f"SECRET_KEY = {SECRET_KEY}")
print(f"Order of G1: {order1}")
print(f"Order of G2: {order2}")
print(f"Order of G3: {order3}")
print(f"k1 = {k1} (mod {order1})")
print(f"k2 = {k2} (mod {order2})")
print(f"k3 = {k3} (mod {order3})")
print(f"P1 = {P1}")
print(f"P2 = {P2}")
print(f"P3 = {P3}")
