# Program provjerava počinju li riječi u stringu istim slovima 
def animal_crackers(text):
    wordlist = text.lower().split()
    
    return wordlist[0][0] == wordlist[1][0]