"""Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın."""

print("""*************************************
Sayı Toplama Uygulaması
*************************************
""")

toplam = 0
liste = []

while True:
    sayı = input("Sayı Girin: ")
    if(sayı == "q") or (sayı == "Q"):
        print("\n{} sayılarının toplamı: {}".format(liste, toplam))
        print("\nProgramı kullandığınız için teşekkürler...")
        break
    else:
        toplam += int(sayı)
        liste.append(int(sayı))



