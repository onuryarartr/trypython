"""1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)"""

print("""*************************************
Pisagor Üçgeni Bulma Uygulaması

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
        def pisagor_bul(sayı1,sayı2):

            pisagor_list = list()

            for i in range(sayı1,sayı2+1):
                for j in range(sayı1,sayı2+1):
                    c = (i ** 2 + j ** 2) ** 0.5

                    if (c == int(c)):
                        pisagor_list.append((i, j, int(c)))

            return pisagor_list

        print(pisagor_bul(sayı1,sayı2))
        print("\nProgramı kullandığınız için teşekkürler...")
        break
