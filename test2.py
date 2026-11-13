#Δίνονται χρονικά διαστήματα ή τμήματα που επικαλύπτονται. Συγχώνευσε όσα τέμνονται.
#Π.χ. [[1,3], [2,6], [8,10]] → [[1,6], [8,10]]


def bubble_sort(a):
    for j in range(0, len(a) - 1):
        for k in range(0, len(a) -1 - j):
            if a[k] > a[k+1]:
                temp = a[k+1]
                a[k+1] = a[k]
                a[k] = temp
    return a

def foo(a): # exo to teleytaio stoixeio poy gia arxh einai
    # to proto kai se kathe epanalhpsh eite to allazo to deksi akro
    #  toy teleytaio sdtoixeiou an yparxei sygxoneysh kai to deksi akro 
    # toy epomenoy stoixeiou einai megalytero apo to torino deksi akro eite
    #  krato to deksi akro an ayto einai megalytero. an den yparxei
    #  sygxoneysh prostheto to stoixeio to opoio ginetai ayto
    #  teleytaio kai synexizetai h idia diadikasia
    # an einai kenos o pinakas
    if not a:
        return []
    # proto stoixeio
    overlaps = [a[0]]

    for i in range(0, len(a) - 1):
        current = overlaps[-1]
        next = a[i+1]
        if current[1] >= next[0]: # synthkh sygxoneyshs
            if current[1] < next[1]:
                current[1] = next[1]
        else: # prosthikh epomenou diasthmatos
            overlaps.append(next)

    return overlaps




b = [[1,3], [2,6], [8,10]]
c = bubble_sort(b)
print(c)
d = foo(b)
print(d)
