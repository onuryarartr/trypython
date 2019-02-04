"""Problem 3
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın."""

print("Yakıt Hesaplama Programına Hoşgeldiniz!")

tuketim = float(input("Aracınızın 100km başına yakıt tüketim değerini girin (L):"))
yol = int(input("Seyahat mesafenizi girin (km):"))
yakit = float(6.1)
harcanan = (tuketim * yol) / 100

#Aracın 100km'deki yakıt tüketimi alındığı için harcanan değeri hesaplarken 100'e böldüm.

print("İşlem yapılıyor...")

harcama = harcanan * yakit

print("Harcadığınız Yakıt Miktarı: {}L".format(harcanan))

print("Harcadığınız Tutar: {} TL".format(harcama))

print("Programı kullandığınız için teşekkürler...")