print("""*************************************
Faktöriyel Bulma Programı

Programdan çıkmak için "q" harfine basın.
*************************************
""")

while True:
    sayı = input("Sayı:")
    if(sayı == "q"):
        print("\nProgram sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)

        faktoriyel = 1
        for i in range(2, sayı+1):
            faktoriyel *= i
        print("\n{} sayısının faktöriyeli: {}".format(sayı,faktoriyel))
        break
print("\nProgramı kullandığınız için teşekkürler...")
