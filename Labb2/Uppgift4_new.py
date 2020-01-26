def triangel_bas_upp(bas,sida):
    """Skapar en triangel med basen upp"""
    counter = 0
    for i in range(bas):
        print(sida * " " + counter * " " + bas * "*")
        bas -= 2
        counter += 1

triangel_bas_upp(9,2)


def triangel_bas_ned(bas,sida):
    """Skapar en triangel med basen ned"""
    antal_stjärnor = 1
    counter = bas//2
    for i in range(bas):
        print(sida * " " + counter * " " + antal_stjärnor * "*")
        counter -= 1
        antal_stjärnor += 2
        if counter < 0:
            return

triangel_bas_ned(7,5)


