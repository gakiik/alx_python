for i in range(10):
    for j in range(i):
        print("{:02d}, ".format(j * 10 + i), end="")
print()
