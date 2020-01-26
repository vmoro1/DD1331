fil = open("ordlistau.txt")

filstr = fil.read()

ordlista = filstr.split()

print(ordlista)

def hitta_ord(lista, elem):
    """Uppgift 2"""
    elem = input("Välj ett ord:")
    for i in lista:
        if i == elem:
            print(elem + " finns")
            hitta_ord(ordlista)
    print(elem + " finns inte")

# hitta_ord(ordlista, "övrigt")

def helper_ordpar(lista, elem):
    for i in lista:
        if i == elem:
            return True
    return False


def sök_upp_ordpar(lista):
    """Uppgift 3"""
    utrad = ""
    for ord in lista:
            if helper_ordpar(lista, ord) == helper_ordpar(lista, (ord[2:] + ord[:2])):
                utrad += ord + " " + (ord[2:] + ord[:2]) + "\n"
    print(utrad)

#sök_upp_ordpar(ordlista)


def binsok(li, x):
    """Uppgift 4"""
    lo = 0
    hi = len(li)-1
    while lo <= hi:
        mid = (lo+hi)//2
        # print(li[mid])
        if x < li[mid]:
            hi = mid - 1
        elif x > li[mid]:
            lo = mid + 1
        else:
            return True
    return False

print(binsok(ordlista, "övrigt"))

def binärsökning_ordpar(lista):
    """Uppgift 6"""
    utrad = ""
    for ord in lista:
            if binsok(lista, ord) == binsok(lista, (ord[2:] + ord[:2])):
                utrad += ord + " " + (ord[2:] + ord[:2]) + "\n"
    print(utrad)

#binärsökning_ordpar(ordlista)


def br_search(v, target):
    """Returns True if the sorted list v contains target and False otherwise.
    Undefined behaviour if v is not sorted"""
    return helper(v, 0, len(v), target)

def helper(v, start, end, target):
    if start > end or start >= len(v):     # basfall
        return False
    mid = (start+end) // 2
    if v[mid] == target:                   # basfall
        return True
    if v[mid] < target:
        return helper(v, mid+1, end, target)         # rekursion
    else:
        return helper(v, start, mid-1, target)        # rekursion


def välj_metod(lista, sök_metod):
    return sök_metod(lista)


print(välj_metod(ordlista, binärsökning_ordpar))
