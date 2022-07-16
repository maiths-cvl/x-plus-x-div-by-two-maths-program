run = True

while run :
    mode = input("x + (x/y) = z ,1) calculer x : , 2) calculer y : , 3) calculer z : , e) pour arreter le programme : ")

    if mode == "1":
        y = int(input("Entrez y : "))
        z = int(input("Entrez z : "))
        calc = (z / (y+1)) * y
        print("x est égal à : " + str(calc))
    if mode == "2":
        x = int(input("Entrez x : "))
        z = int(input("Entrez z : "))
        if (z - x) == 0:
            calc = 1
        if (z - x) != 0:
            calc = x / (z - x)
        print("y est égal à : " + str(calc))
    if mode == "3":
        x = int(input("Entrez x : "))
        y = int(input("Entrez y : "))
        calc = x + (x/y)
        print("z est égal à : " + str(calc))
    if mode == "e":
        run = False
        break