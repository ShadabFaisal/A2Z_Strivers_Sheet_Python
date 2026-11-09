def print_character_right_angled_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(ord('A') + j), end=' ')
        print()


n = int(input("Enter the number of rows: "))
print_character_right_angled_triangle(n)
"""
A 
A B 
A B C 
A B C D 
A B C D E 
"""