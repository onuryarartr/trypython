print("""*************************************
Kullanıcı Girişi
*************************************
""")

sys_kullanıcı_adı = "onur"
sys_parola = "12345"

kullanıcı_adı = input("\nKullanıcı Adı:")
parola = input("Parola:")
if (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
    print("\nParola hatalı!")

elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print("\nKullanıcı adı hatalı!")

elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("\nKullanıcı adı ve parola hatalı!")

else:
    print("\nSisteme başarıyla giriş yapıldı")
