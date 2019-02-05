"""Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF"""

print("****** Harf Notu Hesaplama Modülü ******\n")

v1 = int(input("1. Vize Notunuzu Girin:"))
v2 = int(input("\n2. Vize Notunuzu Girin:"))
fn = int(input("\nFinal Notunuzu Girin:"))

genel_not = v1*0.3 + v2*0.3 + fn*0.4

print("\nHarf notunuz hesaplanıyor...")

if (genel_not >= 90):
    print("\nHarf Notunuz: AA")
elif (genel_not >= 85):
    print("\nHarf Notunuz: BA")
elif (genel_not >= 80):
    print("\nHarf Notunuz: BB")
elif (genel_not >= 75):
    print("\nHarf Notunuz: CB")
elif (genel_not >= 70):
    print("\nHarf Notunuz: CC")
elif (genel_not >= 65):
    print("\nHarf Notunuz: DC")
elif (genel_not >= 60):
    print("\nHarf Notunuz: DD")
elif (genel_not >= 55):
    print("\nHarf Notunuz: FD")
else:
    print("\nHarf Notunuz: FF")

print("\nProgramı kullandığınız için teşekkürler...")
