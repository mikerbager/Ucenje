# Program vraća rečenicu s riječima u obrnutom redoslijedu
def master_yoda(text):
    wordlist=text.split()
    newlist=[]
    i=(-1)
    while i >= len(wordlist)*(-1):
        newlist.append(wordlist[i])
        i=i-1
    return ' '.join(newlist)