kortlek = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

counter = 0
def riffel_blandning(lista):
    global counter
    help_list = []
    first_half = 0
    second_half = (len(lista)//2)
    for cards in range(len(lista)//2):
        help_list.append(lista[first_half])
        help_list.append(lista[second_half])
        first_half += 1
        second_half += 1
    output = help_list
    counter += 1
    if output != kortlek:
        return riffel_blandning(output)
    else:
        print(counter)
        return output

print(riffel_blandning(kortlek))













