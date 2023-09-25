#Kérjen a program a felhasználótól egy számot és írja ki hogy az adott szám nagyobb, kissebb, vagy egyenlő, mint 10

szam = int(input('Adj meg egy számot!'))
if szam < 10 :
    print(f"Ez a szám kissebb mint 10")
elif szam > 10 :
    print(f"Ez a szám nagyobb mint 10")
elif szam == 10 :
    print(f"Ez a szám 10")