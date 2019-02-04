"""Problem 3
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın."""

print("Yakıt Hesaplama Programına Hoşgeldiniz!")

tuketim = float(input("Aracınızın km başına yakıt tüketim değerini girin (L):"))
yol = int(input("Seyahat mesafenizi girin (km):"))
yakit = float(6.1)

print("İşlem yapılıyor...")

harcama = tuketim * yol * yakit

print("Ödemeniz Gereken Tutar: {} TL".format(harcama))

print("Programı kullandığınız için teşekkürler...")

print("Beden Kitle Endeksi Programına gözat :))")