"""Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi"""

print("""*************************************
Sayı Okuma Uygulaması
*************************************
""")

birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]


while True:
    sayı = int(input("Lütfen 2 basamaklı bir sayı girin:"))

    if (sayı >= 100):
        print("\nGirdiğiniz sayı 2 basamaklı değil !")
        continue
    else:
        def sayı_oku(sayı):
            basamak1 = sayı % 10
            basamak2 = sayı // 10

            return onlar[basamak2] + " " + birler[basamak1]

        print(sayı_oku(sayı))
        print("\nProgramı kullandığınız için teşekkürler...")
        break
