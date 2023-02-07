# Program gleda jel broj udaljen za 10 od 100 ili 200
def almost_there(n):
    if (n > 89 and n < 111) or (n > 189 and n < 211):
        return True
    else:
        return False