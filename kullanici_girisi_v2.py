print("""*************************************
Kullanıcı Girişi v2
*************************************
""")

sys_kullanıcı_adı = "onur"
sys_parola = "12345"
giris_hakki = 3

while True:
    kullanıcı_adı = input("\nKullanıcı Adı:")
    parola = input("Parola:")
    if (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("\nParola hatalı!")
        giris_hakki -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("\nKullanıcı adı hatalı!")
        giris_hakki -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("\nKullanıcı adı ve parola hatalı!")
        giris_hakki -= 1
    else:
        print("\nSisteme başarıyla giriş yapıldı")
        break
    if (giris_hakki == 0):
        print("\nGiriş hakkınız bitti!")
        break
