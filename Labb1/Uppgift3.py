print("1729 är det minsta (positiva) tal som kan skrivas som summan av två kuber på två olika sätt")
print("Du ska säga två tal så räknar jag ut summan av deras kuber, när du hittat de rätta talen vinner så du")
fortsätt1 = True

while fortsätt1:
   a = int(input("A:"))
   b = int(input("B:"))

   if a**3 + b**3 != 1729:
       print("A^3 + B^3 = ",a**3 + b**3,", försök igen...")
   else:
       print("A^3 + B^3 = 1729. Du vann!")
       fortsätt1 = False
