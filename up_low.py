# Program prebraja velika i mala slova
def up_low(s):
    upper=0
    lower=0
    for char in s:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
        else:
            pass
    return upper, lower