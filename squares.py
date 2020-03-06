import math

a = 1000000000
i = 31623

def allDigitsIn(s):
    for i in range(10):
        if str(i) not in s:
            return False
    return True

def rule(s):
    r = s[0] + s[3] + s[4] + s[1]
    return r

def ignoreAll(s):
    r = s[7] + s[2] + s[9] + s[8] + s[0] + s[1] + " " + s[5] + s[4] + s[4]
    return r

def isPerfectSqrt(s):
    i = math.sqrt(int(s))
    return (i).is_integer()


while(a>= 1000000000 and a<=9999999999):
    a = i**2
    
    s = str(a)
    if(allDigitsIn(s)):
        if(isPerfectSqrt(rule(s))):
            print(s)
            print(rule(s))
            print(ignoreAll(s))
    i += 1




"""
s = "REGULATION"

print(rule(s))
print(ignoreAll(s))
"""
