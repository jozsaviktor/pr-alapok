#Kérje be a program az órát és köszönjön napszaknak megfelelően!

ora = int(input("Hány óra van?"))
if ora > 20:
    print(f"{ora} van jó éjszakát!")
elif ora > 12 :
    print(f"{ora} van szép délutánt!")
elif ora < 12 :
    print(f"{ora} van jó reggelt!")