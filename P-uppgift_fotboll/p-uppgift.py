from tkinter import *


def läsa_in_fil():
    """Öppnar textfilen med informationen om fotbollslagen och gör en lista utav informationen"""
    with open("Fotbolls_info.txt", "r", encoding="utf8" ) as handle:
        filstr = handle.read()
        ordlista = filstr.split("\n")
        laginfo = []
        for ord in ordlista:
            laginfo.append(ord.split())

        for element in laginfo:
            for x in range(1,8):
                element[x] = int(element[x])
    return laginfo


def se_tabell():
    """Skapar en tabell utifrån senaste uppdateringen av filen"""

    lag_info = läsa_in_fil()

    for lag in lag_info:
        lag.append(lag[5] - lag[6])

    sorterad_tabell = sorted(lag_info, key=lambda x: (x[7], x[8], x[5]), reverse=True)
    fotbollsserie = ""
    fotbollsserie += (" "*4 +"Lag"+" "*24 + "S"+" "*2 + "V"+" "*2 + "O"+" "*2 + "F"+" "*3 + "M"+" "*5 + "Po" + "\n")

    for element in sorterad_tabell:
        for i in range(1, 8):
            element[i] = str(element[i])

    for lag in sorterad_tabell:
        lag[0] += " "* (27-len(lag[0]))
        lag[1] += " "*2
        lag[2] += " "*2
        lag[3] += " "*2
        lag[4] += " "*2
        lag[5] += "-"
        lag[6] += " " *(7 -len(lag[5]) - len(lag[6]))

    placering = 1
    for elem in sorterad_tabell:
        elem.pop()
        if placering < 10:
            fotbollsserie += str(placering) + ".  " + "".join(elem) + "\n"
        else:
            fotbollsserie += str(placering) + ". " + "".join(elem) + "\n"
        placering += 1
    print(fotbollsserie)
    return fotbollsserie


def autofill(inmat):
    """Kollar om det som användaren har skrivit matchar något lag.
    Om det matchar ett lag ger den resten av lagnamnet. Ifall det
    finns flera möjligheter så ger den så mycket av namnet som är
    gemensamt mellan möjligheterna"""

    lag_info = läsa_in_fil()
    utrad = ""

    counter = 0
    möjliga_lag = []
    for lagnamn in lag_info:
        if inmat == lagnamn[0][:len(inmat)]:
            möjliga_lag.append(lagnamn[0])
            counter += 1

    fortsätt = True
    if counter == 1 :
        utrad = list(möjliga_lag[0])
        for _ in range(0, len(inmat)):
            utrad.pop(0)
        fortsätt = False


    if fortsätt and möjliga_lag != []:

        gemensamma_bokstäver = ""
        gemensamma_tecken = 0
        for i in möjliga_lag[0]:
            if str(i) == möjliga_lag[1][gemensamma_tecken]:
                gemensamma_bokstäver += str(i)
                gemensamma_tecken += 1
        utrad = list(gemensamma_bokstäver)
        for _ in range(0, len(inmat)):
            utrad.pop(0)

    elif möjliga_lag == []:
        print("Du har stavat fel")

    return "".join(utrad)


def inmata_resultat(inmatningHemmalag, inmatningBortalag, inmatningResultat):
    """Användaren matar in ett resultat som uppdaterar filen"""
    lag_info = läsa_in_fil()

    hemmalag = inmatningHemmalag
    bortalag = inmatningBortalag
    resultat = str(inmatningResultat).split("-")

    with open("Fotbolls_info.txt", "w", encoding="utf8") as fil:

        fortsätt = True

        if int(resultat[0]) < 0 or 20 < int(resultat[0]) or int(resultat[1]) < 0 or 20 < int(resultat[1]):
            print("Skriv in ett rimligt resultat!")
            fortsätt = False
        elif resultat[0] > resultat[1]:
            for lag in lag_info:
                if hemmalag == lag[0]:
                    lag[7] += 3
                    lag[2] += 1
                elif bortalag == lag[0]:
                    lag[4] += 1
        elif resultat[0] == resultat[1]:
            for lag in lag_info:
                if hemmalag == lag[0]:
                    lag[7] += 1
                    lag[3] += 1
                elif bortalag == lag[0]:
                    lag[7] += 1
                    lag[3] += 1
        elif resultat[1] > resultat[0]:
            for lag in lag_info:
                if bortalag == lag[0]:
                    lag[7] += 3
                    lag[2] += 1
                elif hemmalag == lag[0]:
                    lag[4] += 1

        if fortsätt:
            for element in lag_info:
                if hemmalag in element:
                    element[5] += int(resultat[0])
                    element[6] += int(resultat[1])
                    element[1] += 1
                if bortalag in element:
                    element[5] += int(resultat[1])
                    element[6] += int(resultat[0])
                    element[1] += 1

        for i in lag_info:
            for x in range(1, 8):
                i[x] = str(i[x])

        output = ""
        for info in lag_info:
            if info[0] == lag_info[19][0]:
                output += " ".join(info)
            else:
                output += " ".join(info) + "\n"

        print(output)
        fil.write(output)


def raise_frame(frame):
    """Tar fram den Frame som önskas"""
    frame.tkraise()

def GUI():
    """Gör ett grafisk användargränssnitt med de olika möjligheterna att "Se tabell", "Inmata resultat", "Avsluta",
    samt "Spara på fil". "Se tabell" och "Inmata resultat" tar användaren till en ny Frame med möjligheterna att
    inmata ett resultat eller se tabellen över Premier League"""

    root = Tk()
    meny = Frame(root)
    inmata = Frame(root)
    tabell = Frame(root)

    for frame in (meny, inmata, tabell):
        frame.grid(row=0, column=0, sticky='news')

    root.title("Premier League")

    Button(meny, text='Se tabell', command=lambda: raise_frame(tabell)).grid(row=0, column=0)
    Button(meny, text="Inmata resultat", command=lambda: raise_frame(inmata)).grid(row=1,column=0)
    Button(meny, text="Avsluta", command=lambda: quit()).grid(row=2, column=0)
    Button(meny, text="Spara på fil").grid(row=3, column=0)

    Label(inmata, text="Hemmalag:").grid(row=0, column=0)
    Label(inmata, text="Bortalag:").grid(row=1, column=0)
    Label(inmata, text="Resultat:").grid(row=2, column=0)

    inmat_hemmalag = Entry(inmata)
    inmat_hemmalag.bind("<Return>", (lambda event: inmat_hemmalag.insert(END, autofill(inmat_hemmalag.get()))))
    inmat_bortalag = Entry(inmata)
    inmat_bortalag.bind("<Return>", (lambda event: inmat_bortalag.insert(END, autofill(inmat_bortalag.get()))))
    inmat_resultat = Entry(inmata)
    inmat_resultat.bind("<Return>", (lambda event: inmata_resultat(inmat_hemmalag.get(), inmat_bortalag.get(), inmat_resultat.get())))

    inmat_hemmalag.grid(row=0, column=1)
    inmat_bortalag.grid(row=1, column=1)
    inmat_resultat.grid(row=2, column=1)
    Button(inmata, text='Tillbaka', command=lambda: raise_frame(meny)).grid(row=5, column=1)

    Button(tabell, text='Tabell', command=lambda: textruta.insert(END, se_tabell())).grid(row=0, column=0)
    Button(tabell, text="Rensa", command=lambda: textruta.delete(1.0,END)).grid(row=0, column=1)
    Button(tabell, text='Tillbaka', command=lambda: raise_frame(meny)).grid(row=0, column=2)
    textruta = Text(tabell, width=60, height=10)
    textruta.grid(row=1)

    raise_frame(meny)
    root.mainloop()


GUI()
