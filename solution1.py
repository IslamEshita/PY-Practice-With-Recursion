# Write code for algorithm 1 below
def print_positive(n):
    if n == 0:
        print(n)
    else:
        print(n)
        print_positive(n - 1)

print_positive(3)