for i in range(10):
    for j in range(i):
        print(", ".join(f"{i:02d}"for i in range(10)for j in range(i+1,10)))

print()
