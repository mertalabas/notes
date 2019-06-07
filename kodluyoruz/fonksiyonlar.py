#SSL Hatası Almamak İçin
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd

class merkezbankasi:
    def __init__(self,series="TP.KKO2.IS.TOP",series_name="İmalat Sanayi Kapasite Kullanım Oranı",startDate="01-01-%202018",endDate="31-12-%202018",typee="csv",key="INbLrZNyJq",aggregationTypes="avg",formulas="0",frequency="5",float="2"):
        self.series = series
        self.series_name = series_name
        self.startDate = startDate
        self.endDate = endDate
        self.float=int(float)

        """
        typee
        csv, xml ya da json 

        """
        self.typee = typee

        self.key = key

        """
        aggregationTypes
        Ortalama: avg,
        En düşük: min,
        En yüksek: max
        Başlangıç: first,
        Bitiş: last,
        Kümülatif: sum
        """
        self.aggregationTypes = aggregationTypes

        """
        formulas
        Düzey: 0
        Yüzde Değişim: 1
        Fark: 2
        Yıllık Yüzde Değişim: 3
        Yıllık Fark: 4
        Bir Önceki Yılın Sonuna Göre Yüzde Değişim: 5
        Bir Önceki Yılın Sonuna Göre Fark: 6
        Hareketli Ortalama: 7
        Hareketli Toplam: 8
        """
        self.formulas = formulas

        """
        frequency
        Günlük: 1
        İşgünü: 2
        Haftalık: 3
        Ayda 2 Kez: 4
        Aylık: 5
        3 Aylık: 6
        6 Aylık: 7
        Yıllık: 8
        """
        self.frequency = frequency

        self.url = 'https://evds2.tcmb.gov.tr/service/evds/series={}&startDate={}&endDate={}&type={}&key={}&aggregationTypes={}&formulas={}&frequency={}'.format(
            self.series, self.startDate, self.endDate, self.typee, self.key, self.aggregationTypes, self.formulas, self.frequency)


    def dataframe(self):

        #DataFrame Oluşturur.
        self.df=pd.read_csv(self.url)

        #UNIXTIME Sütununu Kaldırır.
        self.df.drop("UNIXTIME", axis=1, inplace=True)

        #Virgülden Sonrasını 2 hanede bırakır.
        self.df[self.df.iloc[:,1].name] = self.df[self.df.iloc[:,1].name].apply(lambda x: round(x, self.float))



        #Formülas Değerine Göre İsim Değiştirir
        if self.formulas=="0":
            self.df.rename(columns={self.series.replace(".", "_"): self.series_name}, inplace=True)
        elif self.formulas=="1":
            self.df.rename(columns={(self.series.replace(".", "_")+"-"+self.formulas): (self.series_name+"-Yüzde Değişim")}, inplace=True)
            self.df.drop(self.series.replace(".", "_"), axis=1, inplace=True)
        elif self.formulas=="2":
            self.df.rename(columns={(self.series.replace(".", "_")+"-"+self.formulas): (self.series_name+"-Fark")}, inplace=True)
            self.df.drop(self.series.replace(".", "_"), axis=1, inplace=True)
        elif self.formulas=="3":
            self.df.rename(columns={(self.series.replace(".", "_")+"-"+self.formulas): (self.series_name+"-Yıllık Yüzde Değişim")}, inplace=True)
            self.df.drop(self.series.replace(".", "_"), axis=1, inplace=True)
        elif self.formulas=="4":
           #
           #
           #
           #
           #
           #
           #Burası Önemli isim şey etme. burayı hatırlarsın aslanım.
           #
           #
           #
           #
            self.series_name= self.series_name+"-Yıllık Fark"
           #
            self.df.rename(columns={(self.series.replace(".", "_")+"-"+self.formulas): self.series_name}, inplace=True)
            self.df.drop(self.series.replace(".", "_"), axis=1, inplace=True)
        elif self.formulas=="5":
            self.df.rename(columns={(self.series.replace(".", "_")+"-"+self.formulas): (self.series_name+"-Bir Önceki Yılın Sonuna Göre Yüzde Değişim")}, inplace=True)
            self.df.drop(self.series.replace(".", "_"), axis=1, inplace=True)
        elif self.formulas=="6":
            self.df.rename(columns={(self.series.replace(".", "_")+"-"+self.formulas): (self.series_name+"-Bir Önceki Yılın Sonuna Göre Fark")}, inplace=True)
            self.df.drop(self.series.replace(".", "_"), axis=1, inplace=True)
        elif self.formulas=="7":
            self.df.rename(columns={(self.series.replace(".", "_")+"-"+self.formulas): (self.series_name+"-Hareketli Ortalama")}, inplace=True)
            self.df.drop(self.series.replace(".", "_"), axis=1, inplace=True)
        elif self.formulas=="8":
            self.df.rename(columns={(self.series.replace(".", "_")+"-"+self.formulas): (self.series_name+"-Hareketli Toplam")}, inplace=True)
            self.df.drop(self.series.replace(".", "_"), axis=1, inplace=True)

        #Tarih Düzeltme
        #Boş Liste
        self.date_list=list()
        for self.date in self.df["Tarih"]:
            #int olan değerleri string'e çevirir.
            self.date = str(self.date)

            if self.date[5:] == "1":
                self.newdate = "Ocak " + self.date[2:4]
            elif self.date[5:] == "2":
                self.newdate = "Şubat " + self.date[2:4]
            elif self.date[5:] == "3":
                self.newdate = "Mart " + self.date[2:4]
            elif self.date[5:] == "4":
                self.newdate = "Nisan " + self.date[2:4]
            elif self.date[5:] == "5":
                self.newdate = "Mayıs " + self.date[2:4]
            elif self.date[5:] == "6":
                self.newdate = "Haziran " + self.date[2:4]
            elif self.date[5:] == "7":
                self.newdate = "Temmuz " + self.date[2:4]
            elif self.date[5:] == "8":
                self.newdate = "Ağustos " + self.date[2:4]
            elif self.date[5:] == "9":
                self.newdate = "Eylül " + self.date[2:4]
            elif self.date[5:] == "10":
                self.newdate = "Ekim " + self.date[2:4]
            elif self.date[5:] == "11":
                self.newdate = "Kasım " + self.date[2:4]
            elif self.date[5:] == "12":
                self.newdate = "Aralık " + self.date[2:4]

            elif self.date[5:] == "Q1":
                self.newdate = "İlk Çeyrek " + self.date[2:4]
            elif self.date[5:] == "Q2":
                self.newdate = "İkinci Çeyrek " + self.date[2:4]
            elif self.date[5:] == "Q3":
                self.newdate = "Üçüncü Çeyrek " + self.date[2:4]
            elif self.date[5:] == "Q4":
                self.newdate = "Son Çeyrek " + self.date[2:4]

            elif self.date[5:] == "S1":
                self.newdate = "İlk 6 Ay " + self.date[2:4]
            elif self.date[5:] == "S2":
                self.newdate = "İkinci 6 Ay " + self.date[2:4]
            else:
                self.newdate=self.date

            #Listeye Ekler
            self.date_list.append(self.newdate)

        #Listedeki Değerleri Sütun Olarak ekler.
        self.df["Tarih_D"]=pd.Series(self.date_list)

        #Değiştirilmiş Tarihleri İndex Yapar
        self.df.set_index("Tarih_D", inplace=True)

        #Tarih Sütununu Kaldırır.
        self.df.drop("Tarih", axis=1, inplace=True)
        return self.df

    def birlestir(self,df1,*args):
        self.df1 = df1
        for arg in args:
            self.df1 = pd.concat([self.df1, arg], axis=1)
        return self.df1
