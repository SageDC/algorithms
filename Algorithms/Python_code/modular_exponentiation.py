import math

def main():
    # should return 30
    return modexp(2, 10, 497)

# Modular exponentiation
# Input: Two n-bit integers x and N, integer exponent y
# Output: x^y mod N
# Time Complexity: O(n^3)
def modexp(x, y, N):
    if y == 0: return 1
    z = modexp(x, math.floor(y/2), N)
    if y % 2 == 0:
        return math.pow(z, 2) % N
    else:
        return x*math.pow(z, 2) % N

if __name__ == '__main__':
    print(main())