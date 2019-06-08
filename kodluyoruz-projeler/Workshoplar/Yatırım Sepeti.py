#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Kütüphanelerimizi ekledik
import pandas as pd
import numpy as np
import time

# Boş bir dataframe oluşturduk.
toplananveri= pd.DataFrame()

for i in range(60): # 60'a kadar saydık.
    # Finansal verileri html formunda çektik.
    veriler = pd.read_html('http://finans.mynet.com/')
    
    # Bizim dolar, euro ve altın ihtiyacımız olduğu için 9 ve 11. indeksdeki dataframeler işimizi görecektir.
    sepet = veriler[9] # dolar ve euro
    altin = veriler[11] # altın
    
    # Sütun isimleri değiştirildi.
    sepet.rename({"Son":"cinsi","Son.1":"fiyat","Saat":"saat"},axis=1,inplace=True)
    altin.rename({"Son":"cinsi","Son.1":"fiyat","Saat":"saat"},axis=1,inplace=True)    
    
    # Fark çıkartıldı.
    sepet.drop("Fark %",axis=1,inplace=True)
    
    # Fark çıkartıldı.
    altin.drop("Fark %",axis=1,inplace=True)
    
    # Dolar ve euro haricindekiler çıkartıldı.
    sepet = sepet.iloc[:2,:] 
    
    # Çeyrek Çekildi.
    altin = altin.iloc[[2],:]
    
    # Dolar, euro ve altini birleştirelim.
    sepet = pd.concat([sepet,altin], axis = 0,ignore_index=True)
    
    # Birleştirdiğimiz sepet dataframeini toplananveri içerisinde biriktirelim.
    toplananveri = pd.concat([toplananveri,sepet], axis = 0,ignore_index=True)

    time.sleep(60) # Dakika başı işlem yapmak için 60 saniye bekletiyoruz.

# Fiyat virgül düzeltme
toplananveri["fiyat"] = toplananveri["fiyat"] / 10000    

# 33 bin tl ne kadar döviz yada altın alınacağı
toplananveri["kasa"] = 33000 / toplananveri["fiyat"]

# Virgül sonrası 2 hane gösterme.
toplananveri['kasa'] = toplananveri['kasa'].map('{:,.2f}'.format)

print(toplananveri)

