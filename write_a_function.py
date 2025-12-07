def is_leap(year):
    leap =False
    if year%400==0:  #if year divisible by 400 then it is a leap year
        return True 
    elif year%100==0:   #if year divisible by 100 then its not leap year
        return False
    elif year%4==0:    #if year divisible by 4 then it also a leap year
        return True
    return leap   
year = int(input())

print(is_leap(year))
