# class Kisi():
#     def __init__(self,ad,soyad):
#         self.ad=ad
#         self.soyad=soyad
#     def YazIsim(self):
#         print(f"Adı Soyadı: {self.ad} {self.soyad}")

# ogrenci1=Kisi("Ali","Kandır")
# ogrenci1.YazIsim()


# class Kisi():
#     def __init__(self,ad,soyad):
#         self.ad=ad
#         self.soyad=soyad
#     def YazIsim(self):
#         print(f"Adı Soyadı: {self.ad} {self.soyad}")
# class Memur(Kisi):
#     def __init__(self, memurID,ad,soyad):
#         self.memurID=memurID
#         super().__init__(ad,soyad) ### super kullanarak miras olarak üst sınıftan alabiliriz.

# ahmet=Memur("a5463","Ali","Kandır")
# ahmet.YazIsim()


#### Örnek Problem: 

# class Kisi():
#     def __init__(self,ad,soyad):
#         self.ad=ad
#         self.soyad=soyad
#     def IsmiVer(self):
#         print(f"Kişinin Adı Soyadı: {self.ad} {self.soyad}")

# class Calisan(Kisi):
#     def __init__(self, ad, soyad,calisanID):
#         self.calisanID=calisanID
#         self.maas=0
#         super().__init__(ad, soyad)
    
#     def MaasiAyarla(self):
#         self.maas=int(input(f"{self.ad} {self.soyad} için yeni maaşı girin: "))
    
#     def PersonelBilgisi(self):
#         print(f"Çalışan adı soyadı: {self.ad} {self.soyad}"
#               f"Çalışan ID: {self.calisanID}"
#               f"Çalışan maaşı: {self.maas}")

# class Yonetici(Calisan):
#     def __init__(self, ad, soyad, calisanID,departman):
#         self.departman=departman
#         self.bagliCalisanlar=[]
#         super().__init__(ad, soyad, calisanID)
    
#     def BagliCalisanEkle(self,calisan):
#         self.bagliCalisanlar.append(calisan)
    
#     def BagliCalisanVer(self):
#         print(f"Yöneticiye bağlı çalışanlar: {self.bagliCalisanlar}")

# calisan1=Calisan("Ozan","Alptekin",calisanID=101)
# calisan1_bilgi=[calisan1.ad,calisan1.soyad,calisan1.calisanID]
# calisan2=Calisan("Toprak","Alptekin",calisanID=102)
# calisan2_bilgi=[calisan2.ad,calisan2.soyad,calisan2.calisanID]
# yonetici=Yonetici("Ahmet","Mehmet",calisanID=201,departman="Arge")

# calisan1.MaasiAyarla()
# calisan2.MaasiAyarla()
# yonetici.MaasiAyarla()
# calisan1.PersonelBilgisi()
# calisan2.PersonelBilgisi()
# yonetici.PersonelBilgisi()
# yonetici.BagliCalisanEkle([calisan1.ad,calisan1.soyad,calisan1.calisanID,calisan1.maas])
# yonetici.BagliCalisanEkle([calisan2.ad,calisan2.soyad,calisan2.calisanID,calisan2.maas])
# yonetici.BagliCalisanVer()



##### Encapsulation (Kapsülleme)
## Bir fonksiyonun class'ın kendi içinde çalışmasını sağlar. Dışarıdan ulaşılmaz.

# class Kisi():
#     def __init__(self,isim,tcKimlik):
#         self.isim=isim
#         self.__tcKimlik=tcKimlik  ### __ koyulunca kapsüllenmiş olur, class dışında kullanılmaz.
# ogrenci1=Kisi("Ali Kandır",1234567892)
# print(ogrenci1.isim)
# print(ogrenci1.__tcKimlik) ### Hata verir çünkü bulamaz 


# class Kisi():
#     def __init__(self,isim,ekders):
#         self.isim=isim
#         self.__ekders=ekders 
#     def EkDersHesapla(self):
#         print(80*self.__ekders)  #### Class içerisinde kullanılabilir.
# ogrenci1=Kisi("Ali Kandır",10)
# ogrenci1.EkDersHesapla() ### Class içindeki fonksiyonlarda kullanılan kapsüllenmiş veri hata vermez.


### Getter Setter methodu. Kapsüllenmiş veriye ulaşma ve değiştirme

# class Kisi():
#     def __init__(self,isim,ekders):
#         self.isim=isim
#         self.__ekders=ekders 
#     def EkDersHesapla(self):
#         print(80*self.__ekders)
#     def GetterEkDers(self):   ### Böyle bir fonksiyon kullanarak kapsüllü veriye ulaşımı sağlayabiliriz
#         sifre=input("lütfen şifre giriniz: ")
#         if sifre=="12345":   ### Kullanma sebebi olarak örnek, bir şifreleme koyabiliriz, güvenlik katmanı oluşturmak için.
#             print(self.__ekders)
#         else:
#             print("Şifre Hatalı")

#     def SetterEkDers(self,ekders):   ### Böyle bir fonksiyon kullanarak kapsüllü veriyi değiştirebiliriz.
#         sifre=input("lütfen şifre giriniz: ")
#         if sifre=="12345":   
#             self.__ekders=ekders
#         else:
#             print("Şifre Hatalı")
# ogrenci1=Kisi("Ali Kandır",10)
# ogrenci1.EkDersHesapla() 
# ogrenci1.GetterEkDers()
# ogrenci1.SetterEkDers(15)
# ogrenci1.EkDersHesapla()

### Polymorphism özelliği
# class Araba():
#     def Tekerlek(self):
#         return "Arabanın tekerlek sayısı 4'tür"
#     def Kontrol(self):
#         return "Araba kontrolü direksiyon ile sağlanır."
#     def Yakit(self):
#         return  "Arabanın yakıtı fosil yakıttır"
    
# class Bisiklet:
#     def Tekerlek(self):
#         return "Bisikletin tekerlek sayısı 2'dir"
#     def Kontrol(self):
#         return "Bisikletin kontrolü gidon ile sağlanır."
#     def Yakit(self):
#         return "Bisikletin çalışması insan gücüdür"

# bisiklet=Bisiklet()
# araba=Araba()
# for tasit in (bisiklet,araba):  ### Polymorphism
#     print(tasit.Kontrol())
#     print(tasit.Tekerlek())
#     print(tasit.Yakit())


#### Örnek Memur ve Öğrenci Kişileri, Öğrencinin yetkileri kısıtlı: 

# class Kisi():
#     def __init__(self,isim,kisiID,yetki):
#         self.isim=isim
#         self.kisiID=kisiID
#         self.yetki=yetki
        
#     def BilgiVer(self):
#         print(f"{self.isim} isimli kişinin ID: {self.kisiID}, yetki: {self.yetki}")

# class Ogrenci(Kisi):
#     def __init__(self,isim,kisiID,yetki,vize,final):
#         super().__init__(isim,kisiID,yetki)
#         self.__vize=vize
#         self.__final=final
#         self.__ortalama=self.OrtalamaHesapla()
    
#     def OrtalamaHesapla(self):
#         return (self.__vize+self.__final)/2
    
#     def GetterVizeFinal(self):
#         print(f"Öğrenci vize notu: {self.__vize}, final notu: {self.__final}")
    
#     def SetterVizeFinal(self,vize,final):
#         self.__vize=vize
#         self.__final=final
#         self.__ortalama=self.OrtalamaHesapla()

#     def GetterOrtalama(self,yetki=1):
#         if yetki==2:
#             print(f"Ortalama: {self.__ortalama}")
#         else:
#             print("Yetkiniz yok")      
# class Memur(Kisi):
#     def __init__(self, isim, kisiID, yetki,departman):
#         super().__init__(isim, kisiID, yetki)
#         self.departman=departman
    
#     def GetterOrtalama(self,ogrenci,yetki):
#         ogrenci.GetterOrtalama(yetki)
# ogrenci1=Ogrenci("Ali Kandır",12345,1,50,70)
# ogrenci1.GetterOrtalama(ogrenci1.yetki)
# ogrenci1.SetterVizeFinal(70,100)
# ogrenci1.GetterOrtalama(ogrenci1.yetki)

# memur1=Memur("Ahmet Mehmet",456,2,"Bilgisayar Mühendisliği")
# memur1.GetterOrtalama(ogrenci1,memur1.yetki)