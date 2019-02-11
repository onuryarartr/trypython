"""Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok"""

print("""*************************************
EBOB Bulucu Uygulama
*************************************
""")

def ebob_bul(sayı1,sayı2):

    x = 1
    ebob = 1

    while(x <= sayı1 and x<= sayı2):
        if (not (sayı1 % x) and not (sayı2 % x)):
            ebob = x
        x += 1
    return ebob

sayı1 = int(input("1. Sayıyı girin:"))
sayı2 = int(input("2. Sayıyı girin:"))

print(sayı1,"ve",sayı2,"sayıları için EBOB:",ebob_bul(sayı1,sayı2))
print("\nProgramı kullandığınız için teşekkürler...")