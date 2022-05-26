##  AB Testi ile Bidding Yöntemlerinin Dönüşümünün Karşılaştırılması ## 


########### İŞ PROBLEMİ ##############

Facebook kısa süre önce mevcut "maximumbidding" adı verilen teklif verme türüne alternatif olarak yeni bir teklif türü olan "averagebidding"’i tanıttı.

Müşterilerimizden biri olan xyz.com, bu yeni özelliği test etmeye karar verdi ve averagebidding'in maximumbidding'den daha fazla dönüşüm getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.

A/B testi 1 aydır devam ediyor ve xyz.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.


######### VERİ SETİ HİKAYESİ###########

Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları reklam sayıları gibi bilgilerin yanı sıra
buradan gelen kazanç bilgileri yer almaktadır.

Kontrol ve Test grubu olmak üzere iki ayrı veri seti vardır.

Bu veri setleri ab_testing.xlsx excel’inin ayrı sayfalarında yer almaktadır.

Kontrol grubuna Maximum Bidding, test grubuna AverageBidding uygulanmıştır.


# DEĞİŞKENLER

Impression : Reklam görüntüleme sayısı

Click : Görüntülenen reklama tıklama sayısı

Purchase : Tıklanan reklamlar sonrası satın alınan ürün sayısı

Earning: Satın alınan ürünler sonrası elde edilen kazanç


##  Veriyi Hazırlama ve Analiz Etme 

veriyi okutup kopyaladıktan sonra analiz işlemlerini yapan bir fonksiyon tanımladım.

![1](https://user-images.githubusercontent.com/101973346/170588465-c3badce2-cf10-46a2-8754-517e9ff5b4e5.png)

#Bu fonksiyon ile kontrol gurubuna göz atalım.

![1](https://user-images.githubusercontent.com/101973346/170588650-6192b007-e95a-451c-9ee4-9eaec84df235.png)

![2](https://user-images.githubusercontent.com/101973346/170588664-523606e2-bfb5-4f95-9bb0-cdc15f50c479.png)


#Bu fonksiyon ile test gurubuna göz atalım.

![aa](https://user-images.githubusercontent.com/101973346/170588775-0c9906b4-67c0-456e-9d48-f106d9faee4d.png)

![aaa](https://user-images.githubusercontent.com/101973346/170588780-3f670e79-6fee-479d-893a-cd489819718d.png)


## Her iki grubu tek dataframe'de birleştirdim.

![ffgf](https://user-images.githubusercontent.com/101973346/170588883-e10ea5b9-a50c-4a31-b925-d03960c407e0.png)


## A/B Testinin Hipotezinin Tanımlanması

H0 : M1 = M2 (kontrol grubu ve test grubu satın alma ortalamaları arasında anlamlı bir fark yoktur)

H1 : M1!= M2 (kontrol grubu ve test grubu satın alma ortalamaları arasında anlamlı bir fark vardır)


# kontrol ve test grubu için kazanç ortalamalarını analiz ettim.

![erererere](https://user-images.githubusercontent.com/101973346/170588990-be9a65ce-ab87-4c2c-bf2d-2b9bf033745a.png)


## HİPOTEZ TESTİNİN GERÇEKLEŞTİRİLMESİ 

# Varsayım Kontrolleri

Normallik Varsayımı :

H0: Normal dağılım varsayımı sağlanmaktadır.

H1: Normal dağılım varsayımı sağlanmamaktadır.

p < 0.05 H0 RED

p > 0.05 H0 REDDEDİLEMEZ

![b](https://user-images.githubusercontent.com/101973346/170589084-9bc3f4f7-f84c-4b6a-9f68-b4e762427223.png)

H0 REDDEDİLEMEZ

Normal Dağılım Varsayımını sağlamaktadır.

![gf](https://user-images.githubusercontent.com/101973346/170589148-a18e074c-2623-4cc5-8d4a-d544d6fe51bd.png)

H0 REDDEDİLEMEZ

Normal Dağılım Varsayımını sağlamaktadır.

### Varyans Homojenliği :

H0: Varyanslar homojendir.

H1: Varyanslar homojen Değildir.

p < 0.05 H0 RED

p > 0.05 H0 REDDEDİLEMEZ

![e](https://user-images.githubusercontent.com/101973346/170589254-e3426ca4-9c6f-49de-81cf-51e395ebffa7.png)

H0 REDDEDİLEMEZ

Control ve test grubunun değerleri varyans homejenliği Varsayımını sağlamaktadır.

Varyanslar Homejendir.

## HİPOTEZ TESTİ 

![1212](https://user-images.githubusercontent.com/101973346/170589320-d012dede-0299-4111-a096-56b462acd131.png)

H0 REDDEDİLEMEZ

Test sonuçlarına göre Test Stat = -0.9416, p-value= 0.3493 çıkmıştır. Yani H0 REDDEDİLEMEZ.

kontrol grubu ve test grubu satın alma ortalamaları arasında istatistiksel olarak anlamlı bir fark yoktur.

## Sonuçların Analizi 

kontrol grubu ve test grubunun getirdiği gelirde 1 aylık sonuçlar bakımından istatistiksel olarak anlamlı bir fark görülmedi.

Ancak bunun sebebi ölçüm yapılan zamanın kısıtlı tutulmuş olması olabilir, dolayısıyla daha uzun vadede testin tekrarlanmasında fayda vardır


