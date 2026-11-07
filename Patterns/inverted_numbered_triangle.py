def print_inverted_numbered_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end=" ")
        print()


n=int(input("Enter the number of rows: "))
print_inverted_numbered_triangle(n)