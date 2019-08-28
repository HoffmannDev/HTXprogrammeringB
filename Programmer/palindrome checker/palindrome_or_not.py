def reverse(z):
    y =''
    for i in range(len(z)-1, -1, -1):
        y = y + z[i]

    return y


s = input("Enter word: ")
if s == reverse(s):
    print("This is a palindrome")
else: print("This is not a palindrome")
