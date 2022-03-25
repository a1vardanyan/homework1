import functools

s = 'yfyjf'
print(s)
s += ';ughg'
print(s)

l = list()
l = []

d = set()
d.add(4)
d.add(989)
d.add(4)
d.add(6)
print(d)
y = {5, 8, 989, 4}
print(y.union(d))

f = True

t34 = 3.0

y = 10
print(100000000000000000000000000000000000000000000000000000000000000000000000000000000 % 3)

sdsd = {
    "yyy": "hihi",
    "jhj": "ljl"
}

print(sdsd["yyy"])
i = 0
while i < 100 and sdsd["yyy"] == "hihi":
    i += 1

for i in range(0, 10, 2):
    print(i)

def foo(t1, t2, t3):
    return (t1 + t2 + t3)

print(foo(5, 7, 8))

def u(r):
    r[3] = 9

def yu(r):
    r = 0

h = [1, 3, 5, 6]
u(h)
print(h)

i = 7
yu(i)
print(i)

#int float boolean - копируются



def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)



def mycache(foo):   # декоратор
    a = dict()
    def wrapper(n):
        if n in a:
            return a[n]
        a[n] = foo(n)
        return a[n]
    return wrapper


@mycache
def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)



def r(*args):
    for x in args:
        print(x)


def mymin(*args):
    min = args[0]
    for x in args:
        if x < min:
            min = x
    return min


def squares(n):
    i = 0
    while i < n:
        yield i * i
        i += 1

a = (squares(5))
for x in a:
    print(x)

print([x for x in squares(100)])


def myzip(first, second):
    n = min(len(first), len(second))
    i = 0
    while i < n:
        yield first[i], second[i]
        i += 1


e = [1, 2, 3, 5, 6]
b = ["hjh", "nkl", "ijhi", "khj", "nkjn"]
print([(id, name) for id, name in myzip(e, b)])


# vминимум 3 цифры
# минимум 1 симол не буква и не цифра
# длинна больше равна 8 и меньше 100
# есть и большие и маленькие буквы

def check_pass(password):
    nums = set('1234567890')
    symbols = 'qwertyuiopasdfghjklzxcvbnm'
    symbols += symbols.upper()
    symbols = set(symbols)
    if len(password) < 8 or len(password) > 100:
        return False
    if password.lower() == password or password.upper() == password:
        return False
    if len(nums.intersection(set(password))) < 3:
        return False
    if len(set(password).difference(nums.union(symbols))) == 0:
        return False
    return True


print(check_pass("jjj"))

print(check_pass("1234567890"))

print(check_pass("hhhhhhhhhhhhh888"))


print(check_pass("ghgHH%88780kkk"))

u = {6, 8, 7}
yyy = {
    "hgg": "gugu",
    "hubb": "gugu",
    "ihig": "iuhi"
}

for key, value in yyy.items():
    print(key, value)

y = (7, 9, 9)
ss = 'hiih'

print('gugu' * 10)

def ttttt(a, y):
    print(y)

ttttt(y='hhh', a=6)


def gggg(*args, **kwargs):
    print(args)
    print(kwargs)


gggg(3, 4, a='jbjb')
arddd = [1, 2, 3, 4]

print(mymin(*arddd))
















