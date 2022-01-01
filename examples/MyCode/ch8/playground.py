if __name__ == '__main__':
    x = int(input()) + 1
    y = int(input()) + 1
    z = int(input()) + 1
    n = int(input())

print([[i, j, k] for i in list(range(x)) for j in list(range(y)) for k in list(range(z))])