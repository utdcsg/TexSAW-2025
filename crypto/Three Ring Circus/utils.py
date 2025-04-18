#!/usr/bin/env python3
"""
Three Ring Circus - Utility Functions
------------------------------------

This file contains utility functions for elliptic curve operations.
You'll need to implement some of these functions to solve the challenge.
"""

import math
from collections import defaultdict

# Basic elliptic curve operations
def point_add(P, Q, a, p):
    """
    Add two points on an elliptic curve y^2 = x^3 + ax + b mod p.
    
    Args:
        P, Q: Points on the curve as tuples (x, y) or None for the point at infinity
        a: Coefficient a in the curve equation
        p: Prime modulus
        
    Returns:
        Resulting point as a tuple (x, y) or None for the point at infinity
    """
    # Handle point at infinity cases
    if P is None:
        return Q
    if Q is None:
        return P
    
    x1, y1 = P
    x2, y2 = Q
    
    # Check if points are inverses of each other
    if x1 == x2 and (y1 + y2) % p == 0:
        return None  # Result is the point at infinity
    
    # Calculate lambda (the slope)
    if x1 == x2 and y1 == y2:
        # Point doubling formula
        lam = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        # Point addition formula
        lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
    
    # Calculate the new point
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    
    return (x3, y3)

def point_multiply(P, k, a, p):
    """
    Multiply a point P by scalar k on an elliptic curve y^2 = x^3 + ax + b mod p.
    Uses the double-and-add algorithm.
    
    Args:
        P: Point on the curve as a tuple (x, y) or None for the point at infinity
        k: Scalar to multiply by (integer)
        a: Coefficient a in the curve equation
        p: Prime modulus
        
    Returns:
        Resulting point as a tuple (x, y) or None for the point at infinity
    """
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
    """
    Find the order of a point P on an elliptic curve y^2 = x^3 + ax + b mod p.
    The order is the smallest positive integer n such that nP = O (point at infinity).
    
    Args:
        P: Point on the curve as a tuple (x, y)
        a: Coefficient a in the curve equation
        p: Prime modulus
        
    Returns:
        Order of the point (integer)
    """
    # TODO: Implement this function to find the order of the point
    # Hint: You can use the point_multiply function and iterate until you reach the point at infinity
    
    pass

def baby_step_giant_step(P, Q, a, p, n=None):
    """
    Solve the discrete logarithm problem using Baby-step Giant-step algorithm.
    Find k such that Q = kP on an elliptic curve y^2 = x^3 + ax + b mod p.
    
    Args:
        P: Base point on the curve as a tuple (x, y)
        Q: Target point on the curve as a tuple (x, y)
        a: Coefficient a in the curve equation
        p: Prime modulus
        n: Optional order of the point P (if known)
        
    Returns:
        Integer k such that Q = kP, or None if no solution is found
    """
    # TODO: Implement the Baby-step Giant-step algorithm
    # This is more efficient than brute force for large discrete logarithm problems
    
    pass

def chinese_remainder_theorem(remainders, moduli):
    """
    Solve a system of congruences using the Chinese Remainder Theorem.
    Find x such that x ≡ remainders[i] (mod moduli[i]) for all i.
    
    Args:
        remainders: List of remainders [r1, r2, ...]
        moduli: List of moduli [m1, m2, ...]
        
    Returns:
        Integer x that satisfies all congruences, unique modulo the product of all moduli
    """
    # TODO: Implement the Chinese Remainder Theorem to reconstruct the full key
    # from partial solutions across different curves
    
    pass

def verify_point_on_curve(P, a, b, p):
    """
    Verify that a point P lies on the elliptic curve y^2 = x^3 + ax + b mod p.
    
    Args:
        P: Point to check as a tuple (x, y)
        a, b: Coefficients in the curve equation
        p: Prime modulus
        
    Returns:
        True if the point lies on the curve, False otherwise
    """
    if P is None:
        return True  # Point at infinity is always on the curve
    
    x, y = P
    left = (y * y) % p
    right = (x * x * x + a * x + b) % p
    
    return left == right
