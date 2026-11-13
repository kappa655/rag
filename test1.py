# Δίνεται ένας πίνακας ακεραίων. Βρες το πρώτο στοιχείο που εμφανίζεται ακριβώς μία φορά.
#Π.χ. [4, 2, 4, 3, 2, 5] → 3

"""
def foo(a):
    index = None
    duplicates = []
    for i in range(0, len(a)-1):
        counter = 1
        counter2 = 0
        for j in range(0+i, len(a)-1):
            if a[i] == a[j+1]:
                duplicates.append(a[i])
                counter = 0
                break
        if counter:
            for num in duplicates:
                if a[i] == num:
                    break
                else:
                    counter2 = counter2 + 1
            if counter2 == len(duplicates):
                index = i
                break
    return index


"""


def foo(a):
    index = None
    for i in range(0, len(a)):
        counter = 0
        for j in range(0, len(a)):
            if a[i] == a[j]:
                counter = counter + 1
        if counter == 1:
            index = i
            break
    return index




ast = [4, 2, 4, 3, 2, 5]
res = foo(ast)
if res is not None:
    print(f"array is {ast} and the element is {ast[res]}")
else :
    print("Not found")


def foo(a):
    key = None
    counts = {}
    for num in a:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1
    for num in a:
        if counts[num] == 1:
            key = num
            break
    
    return key, counts

ast = [4, 2, 4, 3, 2, 5]
res, counters = foo(ast)
if res is not None:
    print(f"array is {ast} and counters is {counters} and the element is {res}")
else :
    print("Not found")