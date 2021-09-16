no = int(input("Enter a number: "))
num = no
rev = 0
while num > 0:
    digit = num % 10
    rev = (rev * 10) + digit
    num //= 10


if rev == no:
    print(str(no) + " is a palindrome number")
else:
    print(str(no) + " is not a palindrome number")