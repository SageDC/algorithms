import math

def main():
    return div(4, 3)

# Division using recursion
# Input: Two n-bit integers x and y, where y >= 1
# Output: Their quotient and remainder
# Time complexity: O(n^2)
def div(x, y):
    if x == 0: return (0, 0)
    q, r = div(math.floor(x/2), y)
    q = 2*q
    r = 2*r
    if x % 2 != 0: r = r + 1
    if r >= y:
        r = r - y
        q = q + 1
    return (q, r)

if __name__ == '__main__':
    print(main())