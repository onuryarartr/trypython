"""Problem 6
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın."""

#Hipotenüs Formülü: a^2 + b^2 = c^2

print("Merhaba, lütfen gerekli olan değerleri girin..")

k = int(input("1. Dik Kenar Uzunluğu (cm):"))
m = int(input("2. Dik Kenar Uzunluğu (cm):"))

print("İşlem yapılıyor...")

h1 = k**2 + m**2
h = h1**0.5

print("Hipotenüs Uzunluğu: {} cm".format(h))

print("Programı kullandığınız için teşekkürler...")