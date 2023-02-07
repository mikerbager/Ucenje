# Program ponavlja svako slovo u stringu triput
def paper_doll(text):
    newlist=[]
    i=0
    while i<len(text):
        newlist.append(text[i])
        newlist.append(text[i])
        newlist.append(text[i])
        i=i+1
    return ''.join(newlist)
        