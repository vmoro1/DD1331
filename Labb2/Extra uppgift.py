def triangel_bas_upp(bas,sida):
    """Skapar en triangel med basen upp"""
    counter = 0
    triangel1 = ""
    for i in range(bas):
        triangel1 += sida * " " + counter * " " + bas * "*" + "\n"
        bas -= 2
        counter += 1
    return triangel1
print(triangel_bas_upp(9,2))


def triangel_bas_ned(bas,sida):
    """Skapar en triangel med basen ned"""
    antal_stjärnor = 1
    counter = bas//2
    triangel2 = ""
    for i in range(bas):
        triangel2 += sida * " " + counter * " " + antal_stjärnor * "*" + "\n"
        counter -= 1
        antal_stjärnor += 2
        if counter < 0:
            return triangel2

print(triangel_bas_ned(7,5))


def romb(avstånd,bredd):
    def triangel_bas_upp(bas,sida):
        """Skapar en triangel med basen upp"""
        counter = 0
        triangel = ""
        for i in range(bas):
            triangel += sida * " " + counter * " " + bas * "*" + "\n"
            bas -= 2
            counter += 1
        return triangel
    def triangel_bas_ned(bas,sida):
        """Skapar en triangel med basen ned"""
        antal_stjärnor = 1
        counter = bas//2
        triangel = ""
        for i in range(bas):
            triangel += sida * " " + counter * " " + antal_stjärnor * "*" + "\n"
            counter -= 1
            antal_stjärnor += 2
            if counter < 0:
                return triangel

    return triangel_bas_ned(bredd, avstånd - 1) + triangel_bas_upp(bredd - 2, avstånd)


print(romb(4,7))