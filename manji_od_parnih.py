# Program vraća manji broj od dva parna, a ako je jedan ili oba neparan vraća veći
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)