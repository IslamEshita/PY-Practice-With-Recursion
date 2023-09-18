# Write a program that takes a positive number as an argument and prints the numbers from n to zero.
def count_down(n):
    if n == 0:
        print(n)
    else:
        print(n)
        count_down(n - 1)

count_down(7)