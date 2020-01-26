import random
import sys

def läsainfil():
    with open("statistik.txt", "r", encoding="utf8") as handle:
        infil = []
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

        return statistik


def helper_poäng(summa_spelare1, summa_spelare2, spelare1, spelare2, game_spelare1, game_spelare2, set_spelare1, set_spelare2):
    poäng1 = 0
    poäng2 = 0

    if summa_spelare1 <= 2 and summa_spelare2 <= 2:
        poäng1 = summa_spelare1 * 15
        poäng2 = summa_spelare2 * 15
    if summa_spelare1 == 3 and summa_spelare2 <= 2:
        poäng1 = 40
        poäng2 = summa_spelare2 * 15
    if summa_spelare1 <= 2 and summa_spelare2 == 3:
        poäng1 = summa_spelare1 * 15
        poäng2 = 40
    if summa_spelare1 == 3 and summa_spelare2 == 3 or summa_spelare1 >= 3 and summa_spelare2 >= 3 and summa_spelare1 == summa_spelare2:
        poäng1 = 40
        poäng2 = 40
    if summa_spelare1 >= 4 and summa_spelare1 - summa_spelare2 == 1:
        poäng1 = "AD"
        poäng2 = " "
    if summa_spelare2 >= 4 and summa_spelare2 - summa_spelare1 == 1:
        poäng1 = " "
        poäng2 = "AD"
    if summa_spelare1 >= 4 and summa_spelare1 - summa_spelare2 >= 2:
        game_spelare1 += 1
        poäng1 = 0
        poäng2 = 0
    if summa_spelare2 >= 4 and summa_spelare2 - summa_spelare1 >= 2:
        game_spelare2 += 1
        poäng1 = 0
        poäng2 = 0
    if game_spelare1 == 6 and game_spelare2 <= 4 or game_spelare1 > 6 and game_spelare2 > 4 and game_spelare1 - game_spelare2 >= 2:
        set_spelare1 += 1
        game_spelare1 = 0
        game_spelare2 = 0
    if game_spelare2 == 6 and game_spelare1 <= 4 or game_spelare2 > 6 and game_spelare1 > 4 and game_spelare2 - game_spelare1 >= 2:
        set_spelare2 += 1
        game_spelare1 = 0
        game_spelare2 = 0

    print("Spelare", 6 * " ", "set", "game", "poäng" )
    print(spelare1, (13 - len(spelare1)) * " ", set_spelare1, 1 * " ", game_spelare1, 2 * " ", poäng1)
    print(spelare2, (13 - len(spelare2)) * " ", set_spelare2, 1 * " ", game_spelare2, 2 * " ", poäng2)
    print("")


def helper_game(game_spelare1, game_spelare2, spelare1, spelare2, set_spelare1, set_spelare2):
    if game_spelare1 == 6 and game_spelare2 <= 4 or game_spelare1 > 6 and game_spelare2 > 4 and game_spelare1 - game_spelare2 >= 2:
        set_spelare1 += 1
        game_spelare1 = 0
        game_spelare2 = 0
    if game_spelare2 == 6 and game_spelare1 <= 4 or game_spelare2 > 6 and game_spelare1 > 4 and game_spelare2 - game_spelare1 >= 2:
        set_spelare2 += 1
        game_spelare1 = 0
        game_spelare2 = 0
    print("Spelare", 6 * " ", "set", "game")
    print(spelare1, (13 - len(spelare1)) * " ",  set_spelare1, 1 * " ", game_spelare1)
    print(spelare2, (13 - len(spelare2)) * " ", set_spelare2, 1 * " ", game_spelare2)
    print("")


def serve_spelare1(visa_resultat, spelare1, spelare2, typ_paus, när_paus, poäng_sum, game_spelare1, game_spelare2, set_spelare1, set_spelare2):
    statistik = läsainfil()
    summa_spelare1 = 0
    summa_spelare2 = 0

    for spelare in statistik:
        if spelare1 == spelare[0]:
            serveprocent_1 = spelare[1]

    while abs(summa_spelare1 - summa_spelare2) < 2 or summa_spelare1 < 4 and summa_spelare2 < 4:
        if random.random() < serveprocent_1:
            summa_spelare1 += 1
            poäng_sum += 1
            if visa_resultat == "Efter varje boll":
                helper_poäng(summa_spelare1, summa_spelare2, spelare1, spelare2, game_spelare1, game_spelare2, set_spelare1, set_spelare2)
            if typ_paus == "Ett antal poäng":
                if poäng_sum == när_paus:
                    sys.exit(0)

        else:
            summa_spelare2 += 1
            poäng_sum += 1
            if visa_resultat == "Efter varje boll":
                helper_poäng(summa_spelare1, summa_spelare2, spelare1, spelare2, game_spelare1, game_spelare2, set_spelare1, set_spelare2)
            if typ_paus == "Ett antal poäng":
                if poäng_sum == när_paus:
                    sys.exit(0)

    if summa_spelare1 > summa_spelare2:
        game_spelare1 += 1
    else:
        game_spelare2 += 1

    return game_spelare1, game_spelare2


def serve_spelare2(visa_resultat, spelare1, spelare2, typ_paus, när_paus, poäng_sum, game_spelare1, game_spelare2, set_spelare1, set_spelare2):
    statistik = läsainfil()
    summa_spelare1 = 0
    summa_spelare2 = 0

    for spelare in statistik:
        if spelare2 == spelare[0]:
            serveprocent_2 = spelare[1]

    while abs(summa_spelare1 - summa_spelare2) < 2 or summa_spelare1 < 4 and summa_spelare2 < 4:
        if random.random() < serveprocent_2:
            summa_spelare2 += 1
            poäng_sum += 1
            if visa_resultat == "Efter varje boll":
                helper_poäng(summa_spelare1, summa_spelare2, spelare1, spelare2, game_spelare1, game_spelare2, set_spelare1, set_spelare2)
            if typ_paus == "Ett antal poäng":
                if poäng_sum == när_paus:
                    sys.exit(0)
        else:
            summa_spelare1 += 1
            poäng_sum += 1
            if visa_resultat == "Efter varje boll":
                helper_poäng(summa_spelare1, summa_spelare2, spelare1, spelare2, game_spelare1, game_spelare2, set_spelare1, set_spelare2)
            if typ_paus == "Ett antal poäng":
                if poäng_sum == när_paus:
                    sys.exit(0)

    if summa_spelare2 > summa_spelare1:
        game_spelare2 += 1
    else:
        game_spelare1 += 1

    return game_spelare2, game_spelare1

#print(serve_spelare2())

def set(visa_resultat, spelare1, spelare2, typ_paus, när_paus, poäng_sum, game_spelare1, game_spelare2, set_spelare1, set_spelare2):
    while game_spelare1 < 6 and game_spelare2 < 6 or abs(game_spelare1 - game_spelare2) < 2:
        if game_spelare1 + game_spelare2 % 2 == 0:
            if serve_spelare1(visa_resultat, spelare1, spelare2, typ_paus, när_paus, poäng_sum, game_spelare1, game_spelare2, set_spelare1, set_spelare2) == (1, 0):
                game_spelare1 += 1
                if visa_resultat == "Efter varje game":
                    helper_game(game_spelare1, game_spelare2, spelare1, spelare2)

            else:
                game_spelare2 += 1
                if visa_resultat == "Efter varje game":
                    helper_game(game_spelare1, game_spelare2, spelare1, spelare2)
        else:
            if serve_spelare2(visa_resultat, spelare1, spelare2, typ_paus, när_paus, poäng_sum, game_spelare1, game_spelare2, set_spelare1, set_spelare2) == (1, 0):
                game_spelare2 += 1
                if visa_resultat == "Efter varje game":
                    helper_game(game_spelare1, game_spelare2, spelare1, spelare2)
            else:
                game_spelare1 += 1
                if visa_resultat == "Efter varje game":
                    helper_game(game_spelare1, game_spelare2, spelare1, spelare2)

    if game_spelare1 > game_spelare2:
        set_spelare1 += 1
    else:
        set_spelare2 += 1
    return set_spelare1, set_spelare2


def main():
    spelare1 = input("Välj spelare1. Spelare1 kommer börja serva.\n")
    spelare2 = input("Välj spelare2\n")
    set_spelare1 = 0
    set_spelare2 = 0
    game_spelare1 = 0
    game_spelare2 = 0
    game_sum = 0
    poäng_sum = 0
    visa_resultat = input("Hur ofta vill du se resultatet:\nEfter varje boll\nEfter varje game\nEfter matchen\n")
    typ_paus = input("Vill du pausa efter:\nEtt antal poäng\nEtt antal game?\n")
    när_paus = int(input("Efter hur många poäng eller game vill du pausa?\n"))
    while (set_spelare1 + set_spelare2) <= 2:
        while game_spelare1 < 6 and game_spelare2 < 6 or abs(game_spelare1 - game_spelare2) < 2:
            if game_spelare1 + game_spelare2 % 2 == 0:
                if serve_spelare1(visa_resultat, spelare1, spelare2, typ_paus, när_paus, poäng_sum, game_spelare1, game_spelare2, set_spelare1, set_spelare2) == (1, 0):
                    game_spelare1 += 1
                    game_sum += 1
                    if visa_resultat == "Efter varje game":
                        helper_game(game_spelare1, game_spelare2, spelare1, spelare2, set_spelare1, set_spelare2)
                    if typ_paus == "Ett antal game":
                        if game_sum == när_paus:
                            sys.exit(0)
                else:
                    game_spelare2 += 1
                    game_sum += 1
                    if visa_resultat == "Efter varje game":
                        helper_game(game_spelare1, game_spelare2, spelare1, spelare2, set_spelare1, set_spelare2)
                    if typ_paus == "Ett antal game":
                        if game_sum == när_paus:
                            sys.exit(0)
            else:
                if serve_spelare2(visa_resultat, spelare1, spelare2, typ_paus, när_paus, poäng_sum, game_spelare1, game_spelare2, set_spelare1, set_spelare2) == (1, 0):
                    game_spelare2 += 1
                    game_sum += 1
                    if visa_resultat == "Efter varje game":
                        helper_game(game_spelare1, game_spelare2, spelare1, spelare2, set_spelare1, set_spelare2)
                    if typ_paus == "Ett antal game":
                        if game_sum == när_paus:
                            sys.exit(0)
                else:
                    game_spelare1 += 1
                    game_sum += 1
                    if visa_resultat == "Efter varje game":
                        helper_game(game_spelare1, game_spelare2, spelare1, spelare2, set_spelare1, set_spelare2)
                    if typ_paus == "Ett antal game":
                        if game_sum == när_paus:
                            sys.exit(0)
        if set(visa_resultat, spelare1, spelare2, typ_paus, när_paus, poäng_sum, game_spelare1, game_spelare2, set_spelare1, set_spelare2) == (1, 0):
            game_spelare2 = 0
            game_spelare1 = 0
            set_spelare1 += 1

        else:
            game_spelare2 = 0
            game_spelare1 = 0
            set_spelare2 += 1

    if set_spelare1 > set_spelare2:
        print(spelare1, "vann matchen med", set_spelare1, "-", set_spelare2)
    else:
        print(spelare2, "vann matchen med", set_spelare2, "-", set_spelare1)


#main()