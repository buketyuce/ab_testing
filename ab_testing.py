########### İŞ PROBLEMİ ##############
# Facebook kısa süre önce mevcut "maximumbidding" adı verilen teklif verme türüne alternatif olarak yeni bir teklif türü olan "averagebidding"’i tanıttı.
# Müşterilerimizden biri olan xyz.com, bu yeni özelliği test etmeye karar verdi ve
# averagebidding'in maximumbidding'den daha fazla dönüşüm getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.
# A/B testi 1 aydır devam ediyor ve xyz.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.


######### VERİ SETİ HİKAYESİ###########
# Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları reklam sayıları gibi bilgilerin yanı sıra
# buradan gelen kazanç bilgileri yer almaktadır.
# Kontrol ve Test grubu olmak üzere iki ayrı veri seti vardır.
# Bu veri setleri ab_testing.xlsx excel’inin ayrı sayfalarında yer almaktadır.
# Kontrol grubuna Maximum Bidding, test grubuna AverageBidding uygulanmıştır.
# DEĞİŞKENLER
# Impression : Reklam görüntüleme sayısı
# Click : Görüntülenen reklama tıklama sayısı
# Purchase : Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, ttest_ind

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Veriyi Hazırlama ve Analiz Etme
dataframe_control = pd.read_excel("öçümleme/ab_testing.xlsx", sheet_name="Control Group") #MaximumBidding
dataframe_test = pd.read_excel("öçümleme/ab_testing.xlsx", sheet_name="Test Group") #AverageBidding

df_control = dataframe_control.copy()
df_test = dataframe_test.copy()

# Analiz işlemlerini yapan bir fonksiyon tanımladım.

def check_df(dataframe, head=5):
    print("********************** Shape ********************** ")
    print(dataframe.shape)
    print("********************** Types ********************** ")
    print(dataframe.dtypes)
    print("********************** Head ********************** ")
    print(dataframe.head())
    print("********************** Tail ********************** ")
    print(dataframe.tail())
    print("********************** NA ********************** ")
    print(dataframe.isnull().sum())
    print("********************** Quantiles ********************** ")
    print(dataframe.quantile([0, 0.05, 0.5, 0.95, 0.99, 1]).T)

check_df(df_control)
check_df(df_test)


#Her iki grubu tek dataframe'de birleştirdim.
df_control["group"] = "control"
df_test["group"] = "test"

df = pd.concat([df_control, df_test], axis=0, ignore_index=False)
df.head()

#A/B Testinin Hipotezinin Tanımlanması
# H0 : M1 = M2 (kontrol grubu ve test grubu satın alma ortalamaları arasında anlamlı bir fark yoktur)
# H1 : M1!= M2 (kontrol grubu ve test grubu satın alma ortalamaları arasında anlamlı bir fark vardır)

#kontrol ve test grubu için kazanç ortalamalarını analiz ettim.
df.groupby("group").agg({"Purchase": "mean"})

#HİPOTEZ TESTİNİN GERÇEKLEŞTİRİLMESİ

# Varsayım Kontrolleri

# Normallik Varsayımı :
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.
# p < 0.05 H0 RED
# p > 0.05 H0 REDDEDİLEMEZ

test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])
print("Test Stat = %.4f, p-value= %.4f" % (test_stat, pvalue))
#p-value= 0.5891
#H0 REDDEDİLEMEZ
#Normal Dağılım Varsayımını sağlamaktadır.

test_stat, pvalue = shapiro(df.loc[df["group"] == "test", "Purchase"])
print("Test Stat = %.4f, p-value= %.4f" % (test_stat, pvalue))
#p-value= 0.1541
#H0 REDDEDİLEMEZ
#Normal Dağılım Varsayımını sağlamaktadır.


# Varyans Homojenliği :
# H0: Varyanslar homojendir.
# H1: Varyanslar homojen Değildir.
# p < 0.05 H0 RED
# p > 0.05 H0 REDDEDİLEMEZ

test_stat, pvalue = levene(df.loc[df["group"] == "control", "Purchase"],
                           df.loc[df["group"] == "test", "Purchase"])
print("Test Stat = %.4f, p-value= %.4f" % (test_stat, pvalue))
#p-value= 0.1083
#H0 REDDEDİLEMEZ
#Control ve test grubunun değerleri varyans homejenliği Varsayımını sağlamaktadır.
#Varyanslar Homejendir.


# Hipotez Testi
test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                              df.loc[df["group"] == "test", "Purchase"],
                              equal_var=True)
print("Test Stat = %.4f, p-value= %.4f" % (test_stat, pvalue))
#Test Stat = -0.9416, p-value= 0.3493
#H0 REDDEDİLEMEZ


# Test sonuçlarına göre Test Stat = -0.9416, p-value= 0.3493 çıkmıştır. Yani H0 REDDEDİLEMEZ.
# kontrol grubu ve test grubu satın alma ortalamaları arasında istatistiksel olarak anlamlı bir fark yoktur.


#Sonuçların Analizi
# kontrol grubu ve test grubunun getirdiği gelirde 1 aylık sonuçlar bakımından istatistiksel olarak anlamlı bir fark görülmedi.
# Ancak bunun sebebi ölçüm yapılan zamanın kısıtlı tutulmuş olması olabilir, dolayısıyla daha uzun vadede testin tekrarlanmasında fayda vardır