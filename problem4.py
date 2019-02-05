"""Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o
Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
abs(-4)
4
abs(5)
5"""

print("""*************************************
Şekil Hesaplama Uygulaması

Parametreler;

1 - Üçgen

2 - Dörtgen

*************************************\n""")

sekil = input("Tipini bulmak istediğiniz sekil kodunu girin:")

if (sekil == "2"):
    print("Lütfen kenar ölçülerini belirtilen sırayla girin")
    a = int(input("1. Kenar ölçüsünü girin:"))
    b = int(input("2. Kenar ölçüsünü girin:"))
    c = int(input("3. Kenar ölçüsünü girin:"))
    d = int(input("4. Kenar ölçüsünü girin:"))

    if (a == b and b == c and c == d):
        print("\nBu şekil bir 'Kare'dir!")
    elif ((a == b and c == d) or (a == c and b == d) or (a == d and b == c)):
        print("\nBu şekil bir 'Dikdötgen'dir!")
    else:
        print("\nBu şekil bir 'Dörtgen'dir!")

elif (sekil == "1"):
    a = int(input("1. Kenar ölçüsünü girin:"))
    b = int(input("2. Kenar ölçüsünü girin:"))
    c = int(input("3. Kenar ölçüsünü girin:"))

    if ((abs(a - b) < c < abs(a + b)) or (abs(a - c) < b < abs(a + c)) or (abs(b - c) < a < abs(b + c))):

        if (a == b and b == c):
            print( "\nBu bir 'Eşkenar Üçgen'dir!")
        elif (a == b or b == c or a == c):
            print("\nBu bir 'İkizkenar Üçgen'dir!")
        else:
            print("\nBu bir 'Çeşitkenar Üçgen'dir!")

    else:
        print("\nÜçgen Oluşmaz!")

print("\nProgramı kullandığınız için teşekkürler...")

