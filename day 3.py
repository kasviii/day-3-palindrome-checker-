def is_palindrome(s):
    s = s.lower()  
    s = ''.join(c for c in s if c.isalnum()) 
    return s == s[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
