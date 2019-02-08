"""Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)"""

print("""*************************************
Mükemmel Sayı Bulucu
*************************************
""")

sayı = int(input("Lütfen bir sayı girin:"))

x = 1
toplam = 0

while (x < sayı):
    if(sayı % x == 0):
        toplam += x
    x += 1

if(toplam == sayı):
    print("\n{} bir mükemmel sayıdır.".format(sayı))
    print("\nProgramı kullandığınız için teşekkürler...")

else:
    print("\n{} bir mükemmel sayı değildir.".format(sayı))
    print("\nProgramı kullandığınız için teşekkürler...")



