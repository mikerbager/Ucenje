# Program provjerava palindrom
def palindrome(s):
    s=s.lower().replace(' ','')
    if s[::] == s[::-1]:
        return 'To je palindrom'
    else:
        return 'Nije palindrom'