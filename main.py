import numpy as np
from simpson import solve

def getf(msg):
    return eval("lambda x : " + input(msg))

def main():
    f = getf('Enter f(x) = ')
    a, b, e = tuple(map(float, input('Enter a, b, eps: ').split()))
    n = int(input("Enter n: "))
    ans, n = solve(f, a, b, e, n)
    for i, a in enumerate(ans):
        print(i + 1, ')', a)
    print("N = ", n)

if __name__ == "__main__":
    main()