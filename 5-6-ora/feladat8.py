jegy = int(input("Kérek eyg jegyet 1-5: "))
if jegy == 5:
    print(f"a jegyed {jegy} jeles")
elif jegy == 4:
    print(f"a jegyed {jegy} jó")
elif jegy == 3:
    print(f"a jegyed {jegy} közepes")
elif jegy == 2:
    print(f"a jegyed {jegy} elégséges")
elif jegy == 1:
    print(f"a jegyed {jegy} elégtelen")
else:
    print(f"a jegyed {jegy} nem megfelelő")