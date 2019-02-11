"""Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;"""

print("""*************************************
EKOK Bulucu Uygulama
*************************************
""")


def ekok_bul(sayı1,sayı2):

    x = 2
    ekok = 1

    while True:
        if (sayı1 % x == 0 and sayı2 % x == 0):
            ekok *= x

            sayı1 //= x
            sayı2 //= x


        elif (sayı1 % x ==  0 and sayı2 % x != 0):
            ekok *= x

            sayı1 //= x


        elif (sayı1 % x != 0 and sayı2 % x == 0):
            ekok *= x

            sayı2 //= x
        else:
            x += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok

sayı1 = int(input("1. Sayıyı girin:"))
sayı2 = int(input("2. Sayıyı girin:"))

print(sayı1,"ve",sayı2,"sayıları için EKOK:",ekok_bul(sayı1,sayı2))
print("\nProgramı kullandığınız için teşekkürler...")