import math

def main():
    # should return 12
    # return euclid(60, 24)

    return extended_euclid(25, 11)

# Modular exponentiation
# Input: Two integeres where a > b > 0
# Output: greatest common divisor
# Time Complexity: O(n^3)
def euclid(a, b):
    if b == 0: return a
    return euclid(b, a % b)

# Input: Two positive integers a and b with a >= b >= 0
# Output: Integers x, y, d such that d = gcd(a, b) and ax + by = d
def extended_euclid(a, b):
    if b ==0: return (1, 0, a)
    x, y, d = extended_euclid(b, a % b)
    return (y, x - math.floor(a/b)*y, d)

if __name__ == '__main__':
    print(main())