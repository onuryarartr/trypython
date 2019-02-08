"""Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4"""

print("""*************************************
Armstrong Sayısı Bulucu
*************************************
""")

sayı = (input("Lütfen bir sayı girin:"))
üs = len(sayı)
sayı = int(sayı)

x = sayı
basamak = 0
toplam = 0

while (x > 0):
    basamak = x % 10
    toplam += basamak ** üs
    x //= 10

if (toplam == sayı):
    print(sayı, "bir Armstrong sayısıdır.")
    print("\nProgramı kullandığınız için teşekkürler...")
else:
    print(sayı, "bir Armstrong sayısı değildir!")
    print("\nProgramı kullandığınız için teşekkürler...")

