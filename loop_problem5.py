"""1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın."""

print("*****************")
print ("1. Yöntem\n")

liste = []

for i in range(1,101):
    if(i % 3 == 0):
        liste.append(i)
print(liste)
print("*****************")


print("\n*****************")
print ("2. Yöntem\n")

for i in range(1, 101):
    if (i % 3 != 0):
        continue
    print(i)

print("*****************")
print("\nProgramı kullandığınız için teşekkürler...")