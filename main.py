
#   bekérek két egész számot


elso_szam = int(input("Adj meg egy számot: "))
masodik_szam = int(input("Add meg a masodik számot: "))

#   a feladat :  Ha a két szám szorzata kevesebb mint  1000, írd ki azok szorzatát
#   ha azok szorzata ezer felett van  írd ki szok összegét

#  meghatároztam az összeget
szamok_osszege = elso_szam + masodik_szam

#   meghatározom a két szám szorzatát
szamok_szorzata = elso_szam * masodik_szam


#  meghatározom, hogy a szám kisebb vagy nagyobb mint 1000

if szamok_szorzata >= 1000:
    print("Az eredmény: ", szamok_osszege)
else:
    print("Az eredmény: ", szamok_szorzata)

