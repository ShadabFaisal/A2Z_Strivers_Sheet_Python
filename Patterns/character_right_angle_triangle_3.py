def print_character_right_angled_triangle_3(n):
    for i in range(n):
        c=chr(ord('E') - i)
        for j in range(i + 1):
            print(chr(ord(c) +j), end=' ')
        print()


n = int(input("Enter the number of rows: "))
print_character_right_angled_triangle_3(n)

"""
E 
D E 
C D E 
B C D E 
A B C D E 
"""