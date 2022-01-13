import math

def main():
    return mult(3, 2)

# Binary multiplication using recursion
# Input: Two n-bit integers x and y, where y >= 0
# Output: Their product
def mult(x, y):
    if y == 0: return 0
    z = mult(x, math.floor(y/2))
    if y % 2 == 0: return 2*z
    else: return (x + 2*z)

if __name__ == '__main__':
    print(main())