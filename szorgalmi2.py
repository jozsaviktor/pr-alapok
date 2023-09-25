#Kérje be a program az órát és köszönjön napszaknak megfelelően! pl.: ha 21 óra vagy nagyobb akkor jó éjszakat, 16 vagy nagyobb jó estét, 12 vagy nagyobb szép délutánt, 7 vagy nagyobb akkor jóreggelt, és ha kissebb vagy nagyobb mint hat óra akkor alvás van.

ora = int(input("Hány óra van?"))
if ora >= 21:
    print(f"{ora} van jó éjszakát!")
elif ora >= 16:
    print(f"{ora} van jó estét")
elif ora >= 12 :
    print(f"{ora} van szép délutánt!")
elif ora >= 7 :
    print(f"{ora} van jó reggelt!")
elif ora <= 6 :
    print(f"Ilyenkor aludni szokás")
