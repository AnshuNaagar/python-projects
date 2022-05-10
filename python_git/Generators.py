def gen(n):
    for i in gen(n):
        yield i

print (gen(10000))


def gen2(n):
    for i in gen(n):
        yield i 
ob1 = gen2(4)
print(next(ob1))
