"""Problem 2
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın."""

a = int(input("1. Sayı:"))
b = int(input("2. Sayı:"))
c = int(input("3. Sayı:"))

if (a > b and a > c):
    print("\nEn büyük değer: {}".format(a))

elif (b > a and b > c):
    print("\nEn büyük değer: {}".format(b))
else:
    print("\nEn büyük değer: {}".format(c))

print("\nProgramı kullandığınız için teşekkürler...")