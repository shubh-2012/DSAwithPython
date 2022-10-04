# check palindrom number or not

def palindrome(str):
    for i in range(1,len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

print(palindrome("123454321"))