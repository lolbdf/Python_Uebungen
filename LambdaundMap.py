# lambda und map

f = lambda x : x * 2

# ist das lebe wie :
def f2(x, y):
    return x * y


liste = [4, 2, 5, 6, 3]
list2 = list(map(f, liste))

print(list2[4])
