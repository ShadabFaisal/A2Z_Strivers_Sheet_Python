def print_number_square_pattern(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top=i
            left=j
            right=2*n-2-j
            bottom=2*n-2-i
            print(n-min(top, left, right, bottom), end=" ")
        print()

n = int(input("Enter the size of the number pattern: "))
print_number_square_pattern(n)