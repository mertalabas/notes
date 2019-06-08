liste = list()

ad, soyad, dogumtarihi = input("Adınız: "), input("Soyadınız: "), int(input("Doğum Yılınız: "))

liste.append([ad,soyad,dogumtarihi])

print("##########")

for i in liste[0]:
    print(i)
