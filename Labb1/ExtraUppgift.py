
lista = []


def LösningsFunktion(int):
    lösning1 = 1
    lösning2 = 1
    lösning3 = 1
    lösning4 = 1
    fortsätt = True

    while fortsätt:

            if lösning1**3 + lösning2**3 == summan:

                 a = lösning1
                 b = lösning2
                 # lösning1 = str(lösning1)
                 # lösning2 = str(lösning2)
                 lista.append(lösning1)
                 lista.append(lösning2)
                 break


            elif lösning1**3 + lösning2**3 < summan:
                 lösning1 += 1

            elif lösning2 >= summan:
                 print("Det finns inga lösningar!")
                 fortsätt = False

            elif lösning1**3 + lösning2**3 > summan:
                 lösning2 += 1
                 lösning1 = 1

    while fortsätt:

            if (lösning3**3 + lösning4**3) == summan and a != lösning3 and b != lösning4 and a != lösning4 and b != lösning3:

                # lösning3 = str(lösning3)
                # lösning4 = str(lösning4)
                lista.append(lösning3)
                lista.append(lösning4)
                fortsätt = False

            elif (lösning3**3+lösning4**3) < summan:
                lösning3 += 1

            elif lösning4 >= summan:
                fortsätt = False

            elif lösning3**3 + lösning4**3 >= summan:
                lösning4 += 1
                lösning3 = 1
    return lista;


summan = int(input("Write a number:"))

LösningsFunktion(summan)

print(lista)