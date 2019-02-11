
def tam_bolen(sayı):
    tam_bolenler = []

    for i in range(2,sayı):

        if(sayı % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayı = input("Sayı girin:")
    if (sayı == "q"):
        break
    else:
        sayı = int(sayı)

        print("Tam bölenleri",tam_bolen(sayı))