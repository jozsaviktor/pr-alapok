#feladat_001
"""
Kérjük e a billentyűzetről a nevünket, és
irassuk ki a képernyőre!
"""
szam_1 = input("Kérek egy számot!: ")
szam_1 = int(szam_1)
szam_3 = float(szam_1)

szam_2 = int(input("Kérek egy másik számot!: "))
osszeg = szam_1 + szam_2
print(f"A megadott két szám összege: {szam_1 + szam_2}")
print(f"A megadott két szám összege: {osszeg}")
print(f"Szam_1 változó típusa: {type(szam_1)}")
print(f"Szam_2 változó típusa: {type(szam_2)}")
print(f"Az összeg változó típusa: {type(osszeg)}")
print(f"A megadott két szám összege: {osszeg}")
print(f"Szam_3 változó értéke: {szam_3}")


