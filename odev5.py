"""Problem 5
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin."""

print("Merhaba, lütfen değiştirmek istediğiniz değerleri girin..")

a = (input("Birinci Sayı:"))
b = (input("İkinci Sayı:"))

Sayılar = ["a","b"]

a,b = b,a

x = len(Sayılar)

print(x, "adet değer başarıyla değiştirildi!")

print("Birinci Sayı: {}\nİkinci Sayı: {}".format(a,b))

print("Programı kullandığınız için teşekkürler...")