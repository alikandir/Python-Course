###  Object Oriented Soruları:
### Soru 1: Sınıf Oluşturma - Hayvan Sınıfı
#Bir "Hayvan" sınıfı oluşturun. 
#Bu sınıfın özellikleri olarak ad, yaş ve tür olsun. Bu sınıfa ait bir nesne oluşturup özelliklerini
#görüntüleyen bir program yazın.

# class Hayvan():
#     ad=" "
#     yas=" "
#     tur=" "
# def HayvanOlustur(ad,tur,yas):
#     yeni_hayvan=Hayvan()
#     yeni_hayvan.ad=ad
#     yeni_hayvan.tur=tur
#     yeni_hayvan.yas=yas
#     return yeni_hayvan

# hayvanlar=[]  ### Objeler liste içine kayıt edilebilir.
# secim=1
# while secim==1 or 2:
#     if secim==1:
#         # nesne=input("Oluşturulacak hayvan nesnesinin adı: ")
#         adi=input("Hayvanın adını girin: ")
#         turu=input("Hayvanın türünü girin: ")
#         yas=int(input("Hayvanın yaşını girin: "))
#         yeni_hayvan=HayvanOlustur(adi,turu,yas)
#         hayvanlar.append(yeni_hayvan)
#         secim=int(input("1-Hayvan ekle\n2-Hayvanları gör\n3-Çıkış\n"))
#     elif secim==2:
#         for hayvan in hayvanlar:
#             print("Adı:", hayvan.ad)
#             print("Türü:", hayvan.tur)
#             print("Yaşı:", hayvan.yas)
#             print("-" * 20)
#         secim=int(input("1-Hayvan ekle\n2-Hayvanları gör\n3-Çıkış\n"))




###Soru 2: Nesne Metodları - Banka Hesapları
#Bir "BankaHesabı" sınıfı oluşturun. Bu sınıfın özellikleri olarak hesap sahibinin adı, hesap numarası
# ve hesap bakiyesi olsun. Bu sınıfa ait "para çekme" ve "para yatırma" metodlarını ekleyin.
# Bir banka hesabı oluşturarak para çekme ve para yatırma işlemleri yapabilen bir program yazın.
# from random import randint
# class BankaHesabi():
#     def __init__(self):
#         self.isim=""
#         self.hesapNo=""
#         self.hesapBakiye=0

#     def ParaCek(self,miktar):
#         yeni_kullanıcı.hesapBakiye-=miktar
#     def ParaYatir(self,miktar):
#         yeni_kullanıcı.hesapBakiye+=miktar
        


# isim=input("Kullanıcı adı giriniz: ")
# yeni_kullanıcı=BankaHesabi()
# yeni_kullanıcı.isim=isim
# yeni_kullanıcı.hesapNo=randint(10**11,10**12-1)
# tercih=1
# kullanicilar=[]
# while 0<tercih<3:
#     if tercih==1:
#         artis=int(input("Yatırmak istenen miktarı girin: "))
#         yeni_kullanıcı.ParaYatir(artis)
#         print("Adı:", yeni_kullanıcı.isim)
#         print("Banka Numarası:", yeni_kullanıcı.hesapNo)
#         print("Bakiye:", yeni_kullanıcı.hesapBakiye)
#         tercih=int(input("Lütfen Seçiniz:\n1-Para Yatır\n2-Para Çek\n3-Çıkış\n"))
    
#     elif tercih==2:
#         eksi=int(input("Çekmek istediğiniz para miktarı:"))
#         yeni_kullanıcı.ParaCek(eksi)
#         print("Adı:", yeni_kullanıcı.isim)
#         print("Banka Numarası:", yeni_kullanıcı.hesapNo)
#         print("Bakiye:", yeni_kullanıcı.hesapBakiye)
#         tercih=int(input("Lütfen Seçiniz:\n1-Para Yatır\n2-Para Çek\n3-Çıkış\n"))


        
    