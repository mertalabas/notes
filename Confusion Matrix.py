#ilgili kütüphanelerin yüklenmesi
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix

#gerçek ve tahmin değerlerinin dataframe'e atanması
d = {'gercek': [1,1,0,1,0,1,1,0,1,0], 'tahmin': [1,0,0,1,0,1,0,0,1,0]}
df = pd.DataFrame(data=d)
df

#matrix'in oluşturulması
confusion_matrix(df.gercek, df.tahmin)

#seaborn ile görselleştirme

confusion_matrix = pd.crosstab(df['gercek'], df['tahmin'], rownames=['Gerçek'], colnames=['Tahmin'])
sns.heatmap(confusion_matrix, annot=True)

#True Positive,False Negative,False Positive  ve True Negative değerlerinin atanması
TP=4
FP=0
FN=2
TN=4


#sensitivity ve specifity değerlerini hesaplamak için formülün oluşturulması

sensitivity= TP/(TP+FN)
specifity=TN/(TN+FP)

sensitivity
specifity
