#kullanacağımız kütüphanelerin yüklenmesi

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# İlgili siteden verileri yüklemek için kodumuzu girelim.
multeci = pd.read_html("https://multeciler.org.tr/turkiyedeki-suriyeli-sayisi/", header=0)

#veriye baktığımda iki tablonun alt alta olduğunu ve indexlerinin farklı olduğu gözükmektedir.
#Bunun için multeci[0] ve multeci[1] için ayrı ayrı işlem yapacağım.
multeci


#multeci[0] daki tabloyu df değişkenine atıyorum.
df=multeci[0]

#df nin ilk 5 satırına bakıyorum
df.head(5)

#veri hakkında bilgi almak için info() komutunu kullanıyorum. 
#Burada erkek,kadın ve toplam serilerinin integer olması gerekiyor fakat object olarak gözükmekte.
#Bu serilerin türünü değiştirmem gerekiyor.

df.info()

#türünü değiştirmeden önce . ları ortadan kaldırmamız gerekiyor. float görmemesi için 
df = df.apply(lambda x: x.str.replace('.',''))

#integer'a dönüştürmek için astype fonsiyonunu kullanıyorum.
df["TOPLAM"]=df['TOPLAM'].astype(int)
df["KADIN"]=df['KADIN'].astype(int)
df["ERKEK"]=df['ERKEK'].astype(int)


#türlerinin değişip değişmediğine bakıyorum.
df.info()

# 0-18 yaş aralığına ulaşmak için toplam serisindeki .loc[1:4] konumunu kullandık.

sifironsekiz = df['TOPLAM'].loc[1:4].sum()

#istediğimiz yazıyı format metodu ile yazdırdık.

print("Tabloya göre 0-18 yaş aralığında {val:,} Suriyeli bulunuyor.".format(val=sifironsekiz))

#0-9 yaş aralığındakilerin toplamı

sifirdokuz = df["TOPLAM"].loc[1:2].sum()
print("10 yaşın altındaki Suriyeli sayısı ise bu ay {val:,} kişi oldu.".format(val=sifirdokuz))

#yüzde olarak hesapladığımızda 

onyasalti = df["TOPLAM"].loc[1:2].sum()
yuzde_10 = onyasalti / (df["TOPLAM"].loc[1:15].sum())
print("Suriyelilerin {:.2%}’ü 10 yaşının altındadır.".format(yuzde_10))

gencnufus =  df['TOPLAM'].loc[4:5].sum()
yuzde_genc = gencnufus / (df["TOPLAM"].loc[1:15].sum())
print("Suriyeli genç nüfusun toplam Suriyeli sayısındaki oranı {:.2%}. Türkiye’nin genç nüfus oranı ise %15,8.".format(yuzde_genc))

erkek_fark_kadin = (df.loc[0]["ERKEK"]) - (df.loc[0]["KADIN"])
print("Suriyeli Erkeklerin Sayısı Suriyeli Kadınların Sayısından {:,} kişi daha fazla.".format(erkek_fark_kadin))


#Görselleştirme

#toplam değeri,diğer değerlere göre çok fazla olduğundan ve grafiğin yapısını bozacağından dolayı onu çıkartıyorum. 
df=df.drop([0])

#grafiğimin boyutunu belirledim
fig = plt.figure(figsize=(16,10))

#Değişkenlere atadım.Alt tarafta karışıklık çıkmaması için
yas=df['YAŞ']
toplam=df['TOPLAM']
erkek=df['ERKEK']
kadın=df['KADIN']

#barh grafik çeşidini kullandım.

xp=np.arange(len(yas))
plt.yticks(xp,yas,size=11)
plt.barh(xp-0.2,toplam,height=0.2,label="Toplam",color='#edf8b1') 
plt.barh(xp+0,erkek,height=0.2,label="Erkek",color='#7fcdbb')
plt.barh(xp+0.2,kadın,height=0.2,label="Kadın",color='#2c7fb8')

plt.xticks(size=14)
plt.legend(fontsize='x-large')
plt.title("Suriyeli Mültecilerin Yaş Grubuna Göre Nüfusu",size=16)

plt.show()
