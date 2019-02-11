"""1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)."""

print("""*************************************
Bir Sayı Aralığındaki Mükemmel Sayıları Bulma Uygulaması

Çıkmak için "q"ya basın!
*************************************
""")

while True:

    sayı1 = (input("Aralık başlangıç sayısı girin:"))
    if((sayı1 == "q") or (sayı1 == "Q")):
        break
    else:
        sayı1 = int(sayı1)
    sayı2 = int(input("Aralık bitiş sayısı girin:"))

    if(sayı1 > sayı2):
        print("!!! Girdiğiniz sayı başlangıç sayısından daha küçük.\n\nLütfen başlangıç sayısından daha büyük bir sayı girin.\n")
        continue

    else:
        def mukemmel_sayi(sayı):

            toplam = 0

            for i in range(1,sayı):
                if (sayı % i == 0):
                    toplam += i
            return toplam == sayı


        liste = []

        for i in range(sayı1,sayı2):
            if (mukemmel_sayi(i)):
                liste.append(i)

        print("\n{} ile {} aralığındaki mükemmel sayılar: {}".format(sayı1,sayı2,liste))
        print("\nProgramı kullandığınız için teşekkürler...")
        break