def print_matrix_integer(matrix=[[]]):
    if not matrix or not any(matrix):
        print()
        return

    for row in matrix:
        for i, num in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))
        print()
