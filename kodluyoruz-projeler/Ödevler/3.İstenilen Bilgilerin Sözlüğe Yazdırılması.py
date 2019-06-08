musterilistesi=[]
while True:
    musteri=[]
    ad= input("Adınız:")
    soyad=input("Soyadınız:")
    dogumyılı=input("Doğum yılınız:")
    if ad == "" or soyad == "" or dogumyılı == "":
        print("Lütfen Ad, Soyad ve Doğum Yılını eksiksiz girin.")
        continue
    
    tckimlik=input("TC kimlik numaranız")
    print(tckimlik)
    if (tckimlik.isdigit() and int(tckimlik) == 11) or tckimlik == "" :
        musteri.append(ad)
        musteri.append(soyad)
        musteri.append(dogumyılı)        
        musteri.append(tckimlik)
        musterilistesi.append(musteri)
        
    else:
        print("TC kimlik numaranız sayısal bir değer olmalı ve 11 haneden oluşmalıdır.")
        

    

    
    for musteri in musterilistesi:
        for i in musteri:
            print(i)
