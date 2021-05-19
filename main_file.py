import numpy as np
from simpson import solve

def getf(msg):
    return eval("lambda x : " + msg)

def main():
    o = int(input("Enter num of example: "))
    with open("data.txt", 'rt') as f:
        for _ in range(4 * (o - 1)):
            f.readline()
        f.readline()
        a, b, e = tuple(map(float, f.readline().split()))
        n = int(f.readline())
        func = getf(f.readline())
    ans, n = solve(func, a, b, e, n)
    for i, a in enumerate(ans):
        print(i + 1, ')', a)
    print("N = ", n)

if __name__ == "__main__":
    main()