
vok = "aeoiyuåäöAEIYUOÅÄÖ"
kons = "ZXCVBMNSDFGHJKLQWRTPzxcvbnmsdfghjklqwrtp"

def viskspråket(inrad):
    """Tar bort vokalerna i en mening"""
    utrad = ""
    for tkn in inrad:
        if tkn in vok:
            utrad += ""
        else:
            utrad += tkn
    return utrad


print(viskspråket("Får jag viska ditt namn?"))


def rövarspråk(inrad):
    utrad = ""
    for tkn in inrad:
        if tkn in kons:
            utrad += tkn + "o" + tkn
        else:
            utrad += tkn
    return utrad


print(rövarspråk("att vara eller att inte vara"))


def översättfrånrövarspråk(inrad):
    """Gör om en mening på råvarspråk till svenska"""
    utrad = ""
    counter = 0
    for tkn in inrad:
        if tkn in vok and counter == 0:
            utrad += tkn
        if tkn in kons and counter == 0:
            utrad += tkn
            counter += 3
        if tkn == " ":
            utrad += " "
        if counter > 0:
            counter -= 1
    return utrad

print(översättfrånrövarspråk("atottot vovarora elollorera"))


def bebisspråket(inrad):
    """Gör om mening till bebisspråk"""
    utrad_lista = []
    utrad = ''
    lista = inrad.split()
    for i in lista:
        for x in i:
            if x in kons:
                utrad += x
            if x in vok:
                utrad += x
                utrad = utrad * 3
                utrad_lista.append(utrad)
                utrad = ""
                break
    return " ".join(utrad_lista)


print(bebisspråket("strand näringslivets mamma hej bajs"))


def allspråket(inrad):
    output = ""
    lista = inrad.split()
    for i in lista:
        utrad = []
        for x in i:
            if x in kons:
                utrad.append(x)
            if x in vok:
                head, *tail = i[len(utrad)-1], i[len(utrad):]
                tail = "".join(tail)
                utrad.insert(0,tail)
                utrad.append("all")
                output += "".join(utrad) + " "
                break

    return output


print(allspråket("frostig vinter"))


def fikonspråket(inrad):
    output = ""
    lista = inrad.split()
    for i in lista:
        utrad = []
        for x in i:
            if x in kons:
                utrad.append(x)
            if x in vok:
                utrad.append(x)
                head, *tail = i[len(utrad)-1], i[len(utrad):]
                tail = "".join(tail)
                utrad.insert(0,tail)
                utrad.append("kon")
                utrad.insert(0,"fi")
                output += "".join(utrad) + " "
                break

    return output

print(fikonspråket("anna och cissi springer en mil"))



def meny():

    print("Vilket språk önskas?\n1: Viskspråket  2: Rövaspråket  3: Bebisspråket\n4: Allspråket  5: Fikonspråket  6: Avsluta programmet")
    a = int(input("Skriv här:"))
    if a == 6:
        print("Hej då!")
        return
    inrad = input("Skriv din fras du vill översätta:")
    if a == 1:
        print("Viskspråket:",viskspråket(inrad))
    elif a == 2:
        print("Rövarspråket:",rövarspråk(inrad))
    elif a == 3:
        print("Bebisspråket:",bebisspråket(inrad))
    elif a == 4:
        print("Allspråket:",allspråket(inrad))
    elif a == 5:
        print("Fikosspråket",fikonspråket(inrad))

    meny()

meny()





