# Program gleda ima li u listi skriven broj 7 nakon što se pojave dvije nule
def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   
       
    return len(code) == 1