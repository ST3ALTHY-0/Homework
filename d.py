
def print_half_star_tree():
    for i in range(1, 6, 1):
        print("*" * i)


def print_full_star_tree():
    p=4
    for i in range(1, 11, 2):
        print(" " * p, end="")
        print("*" * i)
        p = p - 1


print_half_star_tree()
print_full_star_tree()