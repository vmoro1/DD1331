import sys

def läsainfil():
    """Läser in textfilen med statistik och omvandlar den till en lista. Listan kommer innehålla listor med varje spelare och tillhörande statistik."""
    with open("statistik.txt", "r", encoding="utf8") as handle:
        infil= []
        statistik = []

        for line in handle:
            if line.strip() != "":
                infil.append(line.strip())
            else:
                statistik.append(infil)
                infil = []

        for element in statistik:
            vinsprocent = int(element[2]) / int(element[3])
            element.append(vinsprocent)

        for i in statistik:
            i[1] = float(i[1])
            i[2] = int(i[2])
            i[3] = int(i[3])
            i[4] = float(i[4])
        if statistik == []:
            print("Infilen existerar inte. Åtgärda detta och kör programmet igen.")
            sys.exit(0)

        return statistik


#print(läsainfil())


def läsainfil_kontroll():
    """Funktionen kontrolerar att filen som läses in innehåller rimlig data. Om den inte gör det kommer programmet att avslutas."""
    statistik = läsainfil()
    for spelare in statistik:
        if len(spelare) != 5:
            print("Du har angivit ett felaktigt antal statistiska paramentrar i filen. Korrigera infilen och kör programmet igen.")
            sys.exit(0)
        if spelare[1] > 1 and spelare[1] < 0:
            print("Du har angivit en felaktig serveprocent. Korrigera infilen och kör programmet igen.")
            sys.exit(0)
        if spelare[2] < 0:
            print("Antalet vinster kan inte vara negativt. Korrigera infilen och kör programmet igen.")
            sys.exit(0)
        if spelare[3] < 0:
            print("Antalet spelade matcher kan inte vara mindre än noll. Korrigera infilen och kör programmet igen.")
            sys.exit(0)
        if spelare[4] < 1 and spelare[4] > 1:
            print("Vinstprocenten måste ligga mellan noll och ett. Korrigera infilen och kör programmet igen.")
            sys.exit(0)


#läsainfil_kontroll()


def tabell():
    """Skapar en tabell över spelarna och deras statistik. Tabellen sorteras efter spelarnas vinsprocent från högst till lägst."""
    statistik_sorterad = sorted(läsainfil(), key=lambda x: x[4], reverse=True)
    for i in statistik_sorterad:
        i[1] = str(i[1])
        i[2] = str(i[2])
        i[3] = str(i[3])
        i[4] = str(i[4])

    for spelare in statistik_sorterad:
        spelare[0] += (25-len(spelare[0])) * " "
        spelare[1] += (16-len(spelare[1])) * " "
        spelare[2] += (11-len(spelare[2])) * " "
        spelare[3] += (11-len(spelare[3])) * " "

    print("Plac", 1 * " ", "Namn", 20 * " ", "serveprocent", 3 * " ", "vinster", 3 * " ", "spelade", 3 * " ", "vinstprocent")
    utrad = ""
    counter = 1
    for element in statistik_sorterad:
        utrad +=  str(counter) + "." + 5 * " " + " ".join(element) + "\n"
        counter += 1
    print(utrad)


#tabell()


def matainresultat():
    """Låter användaren välja ut två spelare och mata in vem av dem som vann för att sedan skriva ut en uppdaterad tabell."""
    statistik = läsainfil()
    läsainfil_kontroll()
    tabell()
    spelare1 = input("Välj en spelare")
    spelare2 = input("Välj en annnan spelare")
    resultat = input("Vem vann matchen, spelare1 eller spelare2?")

    with open("statistik.txt", "w", encoding="utf8") as fil:

        if resultat == "spelare1":
            for spelare in statistik:
                if spelare1 == spelare[0]:
                    spelare[2] += 1
                    spelare[3] += 1
                if spelare2 == spelare[0]:
                    spelare[3] += 1
        elif resultat == "spelare2":
            for spelare in statistik:
                if spelare2 == spelare[0]:
                    spelare[2] += 1
                    spelare[3] += 1
                if spelare1 == spelare[0]:
                    spelare[3] += 1

        output = ""
        counter = 1
        for spelare in statistik:
            for i in spelare:
                if counter % 5 == 0:
                    output += "" + "\n"
                    counter += 1
                else:
                    output += str(i) + "\n"
                    counter += 1
        output += "aa"
        fil.write(output)
    fil.close()
    matainresultat()


#matainresultat()