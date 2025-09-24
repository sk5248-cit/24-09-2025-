def print_range(a_range):
    index = 0
    while index < len(a_range):
        print(a_range[index], end=" ")
        index += 1
        print()

print_range(range(0, 11))
print_range(range(0, 21, 2))
print_range(range(5, 16, 2))
print_range(range(10, -1, -1))