"""Problem 1
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez"""

print("Sağlıklı yaşam asistanına hoş geldiniz!\n")

boy = float(input("Boyunuzu girin (m):"))
kilo = float(input("Kilonuzu girin (kg):"))

bki = kilo / boy**2

print("\nBeden Kitle Endeksiniz: {}\n".format(bki))

if (bki < 18.5):
    print("Durmunuz: Zayıf")
elif (bki >=18.5 and bki < 25):
    print("Durumunuz: Normal")
elif (bki >=25 and bki < 30):
    print("Durumunuz: Fazla Kilolu")
else:
    print("Durumunuz: Obez")

print("\nProgramı kullandığınız için teşekkürler...")