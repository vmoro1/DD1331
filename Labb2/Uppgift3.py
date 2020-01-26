def ram(n,m,c):
    for i in range(n):
        if i <= (n/3 - 1):
            print(m * "*")
        elif (n/3 - 1) < i <= (2*n)/3:
            print(c * "*" + (m - 2*c) * " " + c * "*")
        else:
            print(m * "*")





ram(10,30,3)
