# Program briše članove liste koji se ponavljaju
def unique_list(lst):
    seen_numbers=[]
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
        else:
            pass
    return seen_numbers