#C
symbols = 'asfffF'
unique_s = set(symbols)
print(len(unique_s))
#D
Nu = "34"
print(int((Nu*100))**2)
#E
str1 = 'd'
str2 = 'e'
a1 = str1 >= str2
a2 = str1 < str2
print(str1*a1 + str2*a2)
#F
def infinite_sequence():
    num = 2
    while True:
        yield num
        num += 1
def prime(n):
    pdict = dict()
    pdict[1] = 2
    pdict[2] = 3
    for k in range(3,n+1):
        for j in infinite_sequence():
                if all(j % pdict[m] !=0 for m in range(1, len(pdict)+1)):
                    pdict[k] = j
                    break
    return pdict[n]
#B
str1 = input()
str2 = input()
def dict_match(str1, str2):
    dip = dict()
    if len(str1) <= len(str2):
        for i in range(0, len(str1)):
            dip[str1[i]] = str2[i]
    else:
        for j in range(0, len(str2)):
            dip[str1[j]] = str2[j]
        for k in range(len(str2), len(str1)):
            dip[str1[k]] = None
    return dip.items()
#D
def decoration(R):
    def decorator(func):
        s = dict()
        def wrapper(value):
            if value in s.values():
                pass
            elif (value not in s.values()) and (len(s) < R):
                s[len(s)] = value
                func(value)
            elif (value not in s.values()) and  (len(s) == R):
                for j in range(1,len(s)):
                    s[j-1] = s[j]
                    s[R-1] = value
                func(value)
        return wrapper
    return decorator
@decoration(2)
def foo(value):
    print('calculate foo for {}'.format(value))
    return value
#C
def type_checker(func):
    def wrapper(arg1, arg2):
        if not isinstance(arg1, int) or not isinstance(arg2, str):
            raise TypeError
        else: print("OK")
    return wrapper
@type_checker
def foo(a, b):
    return a