istiklal_mars = """Korkma, sönmez bu şafaklarda yüzen al sancak;
Sönmeden yurdumun üstünde tüten en son ocak.
O benim milletimin yıldızıdır, parlayacak;
O benimdir, o benim milletimindir ancak.
Çatma, kurban olayım, çehreni ey nazlı hilal!
Kahraman ırkıma bir gül! Ne bu şiddet, bu celal?
Sana olmaz dökülen kanlarımız sonra helal...
Hakkıdır, hakk'a tapan, milletimin istiklal!
Ben ezelden beridir hür yaşadım, hür yaşarım.
Hangi çılgın bana zincir vuracakmış? Şaşarım!
Kükremiş sel gibiyim, bendimi çiğner, aşarım.
Yırtarım dağları, enginlere sığmam, taşarım.
Garbın afakını sarmışsa çelik zırhlı duvar,
Benim iman dolu göğsüm gibi serhaddim var.
Ulusun, korkma! Nasıl böyle bir imanı boğar,
'Medeniyet!' dediğin tek dişi kalmış canavar?
Arkadaş! Yurduma alçakları uğratma, sakın.
Siper et gövdeni, dursun bu hayasızca akın.
Doğacaktır sana va'dettigi günler hakk'ın...
Kim bilir, belki yarın, belki yarından da yakın.
Bastığın yerleri 'toprak!' diyerek geçme, tanı:
Düşün altında binlerce kefensiz yatanı.
Sen şehit oğlusun, incitme, yazıktır, atanı:
Verme, dünyaları alsan da, bu cennet vatanı.
Kim bu cennet vatanın uğruna olmaz ki feda?
Şuheda fışkıracak toprağı sıksan, şuheda!
Canı, cananı, bütün varımı alsın da hüda,
Etmesin tek vatanımdan beni dünyada cüda.
Ruhumun senden, ilahi, şudur ancak emeli:
Değmesin mabedimin göğsüne namahrem eli.
Bu ezanlar-ki şahadetleri dinin temeli,
Ebedi yurdumun üstünde benim inlemeli.
O zaman vecd ile bin secde eder -varsa- taşım,
Her cerihamdan, ilahi, boşanıp kanlı yaşım,
Fışkırır ruh-i mücerred gibi yerden na'şım;
O zaman yükselerek arsa değer belki başım.
Dalgalan sen de şafaklar gibi ey şanlı hilal!
Olsun artık dökülen kanlarımın hepsi helal.
Ebediyen sana yok, ırkıma yok izmihlal:
Hakkıdır, hür yaşamış, bayrağımın hürriyet;
Hakkıdır, hakk'a tapan, milletimin istiklal!
"""



kita_numarasi=1 # Kıta numarası Başlattık.

istiklal_marsi_dict = dict() # Sözlüğümüzü başlattık.

for i in range(1,len(istiklal_mars.splitlines())+1):
    if i % 4 == 0:
        son_deger = i-4

        if i == 40:
            kita = istiklal_mars.splitlines()[son_deger:i+1]

        else:
            kita = istiklal_mars.splitlines()[son_deger:i]

        istiklal_marsi_dict[kita_numarasi] = kita
        kita_numarasi+=1




while True:
    kita_numarasi  = input("Çıkış yapmak için (x)\nLütfen okumak istediğiniz kıtayı girin: ")  #Kullanıcıdan bilgi aldık.

    if kita_numarasi == "x":
        print("Çıkış yaplıyor.")
        break

    elif kita_numarasi.isdigit(): # numara olup olmadığına baktık.

        kita_numarasi = int(kita_numarasi)

        if kita_numarasi > 10 or kita_numarasi < 1: # Kıta kontrolünü
            print("\nİstiklal marşımız 10 kıtadan oluşmaktadır.\n")

        else:
            print("\n" + str(kita_numarasi) + ". Kıta:\n")
            for misra in istiklal_marsi_dict[kita_numarasi]:
                print(misra)
            print("\n")
            
    else:
        print("Lütfen bir sayı giriniz.\n")
