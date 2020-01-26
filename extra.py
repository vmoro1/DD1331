def triangel_bas_upp(bas, sida):
    """Skapar en triangel med basen upp"""
    counter = 0
    triangel = ""
    for i in range(bas):
        triangel += sida * " " + counter * " " + bas * "*" + "\n"
        bas -= 2
        counter += 1
    return triangel


print(triangel_bas_upp(10, 5))