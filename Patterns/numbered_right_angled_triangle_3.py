def print_numbered_right_angled_triangle_3(n):
    num=1
    for i in range(n):
        for j in range(i+1):
            print(num, end=' ')
            num += 1
        print()

n = int(input("Enter the number of rows: "))
print_numbered_right_angled_triangle_3(n)
"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""