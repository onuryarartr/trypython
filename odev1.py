"""Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın."""

print("Merhaba, lütfen istenen değerleri girin..")

s1 = int(input("Sayı 1:"))
s2 = int(input("Sayı 2:"))
s3 = int(input("Sayı 3:"))

print("İşlem yapılıyor...")

sonuc = s1 * s2 * s3

print("İşlem Sonucu: {}".format(sonuc))

print("Programı kullandığınız için teşekkürler...")
