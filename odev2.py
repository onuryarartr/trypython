"""Problem 2
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun."""

#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

print("Beden kitle endeksi hesaplama programına hoşgeldiniz!" )

b = float(input("Boyunuz (m):"))
k = int(input("Kilonuz (kg):"))

bke = k / (b*b)

print("İşlem yapılıyor...")

print("Beden Kitle Endeksiniz: {}".format(bke))

print("Programı kullandığınız için teşekkürler...")