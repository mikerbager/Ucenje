# Program gleda da li u listi imaju dva broja 3 za redom
def has_33(nums):
    
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    
    return False