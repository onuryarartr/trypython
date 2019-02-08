print("""*************************************
ATM Makinesi

İŞlemler;

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için "q" harfine basın.
*************************************
""")

bakiye = 1000

while True:
    islem = input("\nİşlemi seçiniz:")

    if(islem == "q"):
        print("\nKullandığınız için teşekkürler...\nYine bekleriz...")
        break
    elif(islem == "1"):
        print("\nBakiyeniz {} TL".format(bakiye))
    elif(islem == "2"):
        miktar = int(input("Miktarı giriniz:"))
        bakiye += miktar
    elif(islem == "3"):
        miktar = int(input("Miktarı giriniz:"))
        if(bakiye - miktar < 0):
            print("\nBakiyeniz bu miktarı çekmek için yeterli değil!")
            continue
        bakiye -= miktar
    else:
        print("\nGeçersiz İşlem...")