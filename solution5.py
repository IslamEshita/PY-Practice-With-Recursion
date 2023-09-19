
# Write a function that checks whether a string is a palindrome or not. 
# The program should take in a string and return True if the string is a palindrome and False if not.

def is_palindrome(s):
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        first_char = s[0]
        index2 = len(s) - 1
        last_char = s[index2]

        return first_char == last_char and is_palindrome(s[1:index2])

print(is_palindrome('abc'))
print(is_palindrome('abcba'))    
print(is_palindrome('racecar'))