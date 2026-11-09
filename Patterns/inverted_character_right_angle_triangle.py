def print_inverted_character_right_angled_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(ord('A') + j), end=' ')
        print()


n = int(input("Enter the number of rows: "))
print_inverted_character_right_angled_triangle(n)

"""
A B C D E 
A B C D 
A B C 
A B 
A 
"""