#!/usr/bin/env python
# coding: utf-8

# # Python İle Türkiye'nin Kalkınma Göstergelerine Erişim
# Merhaba! Bu yazımızda Türkiye'nin iktisadi kalkınma göstergelerine Dünya Bankası'nın sitesinden nasıl erişildiğini öğreneceğiz.Bunun yanında erişilen verileri düzenleyip, bazılarını görselleştireceğiz. Keyifli Okumalar..

# * [1.Verilerin Düzenlenmesi](#1.Verilerin-Düzenlenmesi)
# * [2.Görselleştirme](#2.Görselleştirme)
#     * [2.1.Demografik Göstergeler ](#2.1.Demografik-Göstergeler)
#     * [2.2.Enerji Göstergeleri](#2.2.Enerji-Göstergeleri)
#     * [2.3.Makro Ekonomik Göstergeler](#2.3.Makro-Ekonomik-Göstergeler)
#     * [2.4.Dış Ticaret Göstergeleri](#2.4.Dış-Ticaret-Göstergeleri)

# ## 1.Verilerin Düzenlenmesi
# <a id="optparam"></a>
# İlk olarak kullanacağımız kütüphaneleri yükleyerek işlemlere başlıyoruz.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Dünya Bankası'nın sitesinden **Türkiye'ye ait göstergelerin yer aldığı linki** alıyorum ve df değişkenine atıyorum. Burada başlıkları daha anlamlı görebilmek için `header=2` olarak alınmıştır.İstenilen başlık türüne göre değiştirilebilinir.

# In[2]:


df = pd.read_excel("http://api.worldbank.org/v2/tr/country/TUR?downloadformat=excel",header=2)


# Data setimizin baştan İlk 2 değerini çağırarak,sütunlarına ve satırlarına bakıyoruz.
# 
# Veri analizinde önemli noktalardan bir tanesi, **verilerin satır ve sütunlarının nasıl oluştuğuna bakılması**, istenilen verinin çağrılmasının ve görselleştirilmesinin kolay olmasıdır. Verilere baktığımızda **gösterge isimlerinin ve kodlarının iki ayrı sütunda** oluştuğunu görmekteyiz. Bu görselleştirme ve verilerin çağırılması açısından istediğimiz formata uygundur. **Fakat yılların her biri ayrı sütunlarda yer almaktadır.** Görselleştirmeyi kolaylaştırmak ve göstergeleri  daha kolay anlamak için veri üzerinde bir takım oynamalar yapmamız gerekmektedir.

# In[3]:


df.head(2)


# Bunun için ilk olarak yeni bir boş DataFrame oluşturuyorum. Oluşturduğum for döngüsü ile df data setimdeki satırların hepsini, sütunların ise tüm yılların yer aldığı sütunları seçiyorum. **Daha sonra bu satır ve sütunları yeni oluşturduğum df_baz değişkenine atıyorum.** df_baz içindeki yılların "Year" lardan ve values lerden oluştuğunu belittikten sonra `.concat()` metodu ile birleştiriyorum.
# Bu işlemi daha iyi bir şekilde anlamak için bu linkte yazılan örneği inceleyebilirsiniz.
# 

# In[4]:


df_yeni=pd.DataFrame()
for col in df.iloc[:,4:]:
    df_baz = df.iloc[:,:4]
    df_baz["Year"]=col
    df_baz["Values"] = df[col]
    df_yeni = pd.concat([df_yeni,df_baz],ignore_index=True)


# Elde ettiğim yeni datasetim ise aşağıdaki gibidir. Burada **yılların ve değerlerin tek bir sütun olduğunu** görmekteyiz.Bu verilerin okunaklılığı ve görselleştirilmesi açısından işimizi kolaylaştıracaktır.

# In[5]:


df_yeni.head()


# Yeni oluşan Dataset içerisinde `NaN` değerler mevcuttur.Bu değerlerin temizlenmesi ya da yerine değerler atanması gerekmektedir.**Burada değer atamak doğru olmadığından NaN değerleri silmemiz gerekmektedir.** Tüm nan değerleri silerek turkiye değişkenine atıyoruz.

# In[6]:


turkiye=df_yeni.dropna()


# `NaN` değerleri sildikten sonra data hakkında özet bilgiler elde etmek istiyorum. Bu özet bilgiler veriyle işlem yaparken
# işimizi kolaylaştıracaktır.
# Datasetin özet bilgilerine baktığımızda toplamda **6 sütun ve 2417 satırdan** oluştuğunu görmekteyiz.Bunun yanında Country Name, Country Code, Indicator Name, Indicator Code, Year değişkenlerinin **object yani strig değerler**, Values değişkeninin ise `float64` olduğunu görmekteyiz. **Fakat "Year" değişkeninin de mantıken integer olması gerektiğini biliyoruz.**

# In[7]:


turkiye.info()


# Year değişkenini integere dönüştürmek için **`.astype()`** metodunu kullanıyoruz.

# In[132]:



turkiye["Year"] = turkiye["Year"].astype("int")


# Özet bilgiye tekrar baktığımızda Year değişkeninin **integer** olduğunu görmekteyiz.

# In[133]:


turkiye.info()


# Yapacağımız bir başka veri düzenlemesi ise **göstergelerin kodu ve isimlerinin net bir şekilde gözükmesini** sağlamaya yöneliktir. Datasetimizde hangi göstergenin hangi başlığa ait olduğunu bulabilmek için **ikisini ayrı bir liste yapıp daha sonra `.concat()` metodu ile birleştiriyorum.** 
#  
# ***!!!Eğer gösterge ismi ve kodunu karıştırmıyorsanız bu adımı uygulamayabilirsiniz.***

# In[134]:


liste=[]
for names_item in turkiye["Indicator Name"]:
    liste.append(names_item)
    
liste1=[]
for names_item in turkiye["Indicator Code"]:
    liste1.append(names_item)

newindicator=pd.DataFrame(liste)
newcode=pd.DataFrame(liste1)
birlesik=pd.concat([newindicator,newcode],axis=1)


# Toplamda 22 değişik göstergemin olduğu gözükmekte. O yüzden **ilk 22 gösterge ve koduna** bakmam işimi kolaylaştıracaktır.

# In[135]:


birlesik.head(22)


# ## 2.Görselleştirme 
# <a id="optparam"></a>
# Bu başlık altında grafiklerdeki karmaşıklığı engellemek için bazı filtrelemeler yapacağız, her bir göstergeyi ayrı alanlarına göre ayırıp başlıklandıracağız ve **2000 yılı sonrası kalkınma göstergelerini görselleştireceğiz.**

# ### 2.1.Demografik Göstergeler 
# <a id="optparam"></a>
# 
# Demografi ile ilgili olduğunu düşündüğümüz tüm göstergeleri kısa ve anlaşılır bir başlığa tanımlıyoruz.Bunun yanında 2000 yılı
# sonrası için filtreleme yapıyoruz.

# In[ ]:


nüfus=turkiye[(turkiye["Indicator Code"]=='SP.POP.TOTL') & (turkiye.Year>2000)]

nüfusoran=turkiye[(turkiye["Indicator Code"]=='SP.POP.GROW') & (turkiye.Year>2000)]

doğurganlıkoranı=turkiye[(turkiye["Indicator Code"]=='SP.DYN.TFRT.IN') & (turkiye.Year>2000)]

beklenenyasam=turkiye[(turkiye["Indicator Code"]=='SP.DYN.LE00.IN') & (turkiye.Year>2000)]

ölümoranı=turkiye[(turkiye["Indicator Code"]=='SP.DYN.IMRT.IN') & (turkiye.Year>2000)]


# Tüm demografik göstergeleri bir arada görmek istediğimden **`.subplot()`** metodunu kullanıyoruz.Siz her bir değişkeni ayrı grafiklerde
# gösterebilirsiniz. Python'da görselleştirme için ayrı bir yazı ele alacağız.

# In[12]:


fig = plt.figure(figsize=(20,12))

plt.subplot(3,3,1)   
plt.plot(nüfus["Year"],nüfus["Values"],"red")
plt.title("Toplam Nüfus")
plt.tight_layout()

plt.subplot(3,3,2)
plt.plot(nüfusoran["Year"],nüfusoran["Values"],"blue")
plt.title("Yıllık Nüfus Artış Oranı")
plt.tight_layout()

plt.subplot(3,3,3)
plt.plot(doğurganlıkoranı["Year"],doğurganlıkoranı["Values"],"black")
plt.title("Doğurganlık oranı")
plt.tight_layout()

plt.subplot(3,3,4)
plt.plot(beklenenyasam["Year"],beklenenyasam["Values"],"yellow")
plt.title("Doğumda beklenen yaşam süresi")
plt.tight_layout()

plt.subplot(3,3,5)
plt.plot(ölümoranı["Year"],ölümoranı["Values"],"g")
plt.title("Ölüm Oranı")
plt.tight_layout()


# ***Grafiklere bakılarak kısaca şu yorumlar yapılabilinir; Türkiye'nin 2002 yılından 2018 yılına kadar nüfusu sürekli olarak artış göstermiştir. Fakat nüfus artış oranı 2013 yılından itibaren azalmaya başlamıştır. Bunun yanında doğurganlık oranı ise 2002 yılından 2018 yılına kadar sürekli olarak azalmıştır. Sağlık alanında yaşanan gelişmelerle birlikte doğumda beklenen yaşam süresi artmış, ölüm oranları ise azalmıştır.***

# ### 2.2.Enerji Göstergeleri 
# <a id="optparam"></a>
# 
# Enerji göstergelerinden farklı örnek olması açısından sadece elektrik tüketimi görselleştirilmiştir.Diğer değişkenleri
# bu örnekten yola çıkarak istediğiniz şekilde görselleştirebilirsiniz.

# In[137]:


#coemisyon=turkiye[(turkiye["Indicator Code"]=='EN.ATM.CO2E.PC') & (turkiye["Year"]>2000)]

elektriktüketim=turkiye[(turkiye["Indicator Code"]=='EG.USE.ELEC.KH.PC') & (turkiye["Year"]>2000)]

#enerjikullanım=turkiye[(turkiye["Indicator Code"]=='EG.USE.PCAP.KG.OE') & (turkiye["Year"]>2000)]

f, (ax1) = plt.subplots(figsize=(16,8), sharex=True)

g=sns.barplot(x="Year",y="Values",data=elektriktüketim,palette="RdBu_r")
plt.tight_layout()

figure = g.get_figure()  


# ***Türkiye'nin elektrik tüketimi 2001 yılından 2008 küresel kriz yılına kadar artmaktayken, 2009 yılda azalmıştır. 2009 yılından 2014 yılına kadar ise 2013 yılı hariç sürekli olarak artmıştır.***
# 

# ### 2.3.Makro Ekonomik Göstergeler 
# <a id="optparam"></a>
# Bu datasetinde makro ekonomik göstergeler arasında eflasyon, kişibaşına düşen milli gelir ve toplam gayrisafi yurtiçi hasıla yer almaktadır.

# In[143]:


enflasyon=turkiye[(turkiye["Indicator Code"]=='FP.CPI.TOTL.ZG') & (turkiye.Year>2000)]

kbdgsyh=turkiye[(turkiye["Indicator Code"]=='NY.GDP.PCAP.CD') & (turkiye.Year>2000)]

gsyh=turkiye[(turkiye["Indicator Code"]=='NY.GDP.MKTP.CD') & (turkiye.Year>2000)]


# Yukarıdaki filtrelemeler yapıldıktan sonra farklı bir grafik türü ile görselleştirme yapmak ve iki değişken arasındaki
# ilişkiyi görebilmek için değişkenler **`.merge()`** metodu ile** birleştirilmiştir.(kbdgsyh ve enflasyon)

# In[146]:


birlesik=pd.merge(kbdgsyh,enflasyon,on="Year",how="outer")


# In[147]:


birlesik.head()


# In[145]:


sns.lmplot(x="Values_x",y="Values_y",data=birlesik)


# ***Grafiğe bakıldığında kabaca şu yorum yapılabilinir.Enflasyon oranı arttıkça kbdgsyh azalmaktadır.Burada grafiğe göre yorumlama yapıyoruz.Yorumun isabetli olması için teoriye bakılması gerekmektedir.***

# ### 2.4.Dış Ticaret Göstergeleri 
# <a id="optparam"></a>
# Burada da dış ticaret göstergeleri olan ithalat ve ihracatın gsyh'a oranını görselleştireceğiz.

# In[15]:


malvehizmetihracat=turkiye[(turkiye["Indicator Code"]=='NE.EXP.GNFS.ZS') & (turkiye["Year"]>2000)]

malvehizmetitalat=turkiye[(turkiye["Indicator Code"]=='NE.IMP.GNFS.ZS') & (turkiye["Year"]>2000)]

malitihr=turkiye[(turkiye["Indicator Code"]=='TG.VAL.TOTL.GD.ZS') & (turkiye["Year"]>2000)]

birlesik2=pd.concat([malvehizmetihracat,malvehizmetitalat])


# In[123]:


birlesik2.head()


# In[173]:


g = sns.catplot(x="Year", y="Values",hue="Indicator Name", data=birlesik2,kind="bar",palette="Set2",legend=False, height=8,
                aspect=18/9)

g.set_ylabels("İthalat ve İhracat Oranları")

plt.legend(loc='upper left')

plt.tight_layout()

plt.show()


# **2001 yılından sonra Türkiye'nin ihtalat oranı, ihracat oranından fazla olmuştur.Yani Türkiye ithalata bağlı hale gelmiş ve cari açık vermiştir.**

# ***Diğer göstergeleri istediğiniz grafik türüyle,yukarıdaki örneklere bakarak kolay bir şekilde görselleştirebilirsiniz.***

# In[ ]:


#KALKINMA
kalkınmayardım=turkiye[(turkiye["Indicator Code"]=='DT.ODA.ODAT.CD') & (turkiye["Year"]>2000)]
#TARIM
tarım=turkiye[(turkiye["Indicator Code"]=='NV.AGR.TOTL.ZS') & (turkiye["Year"]>2000)]

#SANAYİ
endüstri=turkiye[(turkiye["Indicator Code"]=='NV.IND.TOTL.ZS') & (turkiye["Year"]>2000)]

#ASKERİ
askeriharcamalar=turkiye[(turkiye["Indicator Code"]=='MS.MIL.XPND.GD.ZS') & (turkiye["Year"]>2000)]

#TEKNOLOJİK
mobil=turkiye[(turkiye["Indicator Code"]=='IT.CEL.SETS.P2') & (turkiye["Year"]>2000)]

