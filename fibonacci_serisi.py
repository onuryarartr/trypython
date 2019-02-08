print("""*************************************
Fibonacci Serisi
*************************************
""")

a = 1
b = 1

fibonacci = [a,b]

while True:
    sayı = int(input("Fibonacci serisi için uzunluk girin:"))
    if(sayı > 20):
        print("\nLütfen 20'den küçük bir değer girin!\n")
        continue
    else:
        for i in range(sayı-2):
            a,b = b,a+b

            fibonacci.append(b)

    print("Fibonacci Serisi:",fibonacci)

    print("\nProgramı kullandığınız için teşekkürler...")
    break