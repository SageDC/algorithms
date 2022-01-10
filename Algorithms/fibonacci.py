def main():
    return fib2(15)

# recursive definition
# Time Complexity: O((1.6)^n)
def fib1(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib1(n - 1) + fib1(n - 2)

# polynomial definition
def fib2(n):
    if n == 0: return 0
    fList = [None]*(n+1)
    fList[0] = 0
    fList[1] = 1
    for i in range(2, n+1):
        fList[i] = fList[i - 1] + fList[i - 2]
    return fList[n]

if __name__ == '__main__':
    print(main())