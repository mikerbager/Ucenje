# Program mijenja prvo i četvrto slovo stringa u veliko
def old_macdonald(name):
    first_letter=name[0]
    middle=name[1:3]
    fourth_letter=name[3]
    end=name[4:]
    return first_letter.upper() + middle + fourth_letter.upper() + end