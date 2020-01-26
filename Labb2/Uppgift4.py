def triangel(b,s):
    counter = 0
    for i in range(b):
        print(s*" " + counter * " " + b * "*")
        b -= 2
        counter += 1
triangel(10,5)