#### Procedural APP.
# Faktoriyel alma ### Imperactive(Emirli) Programlama
# n=5
# toplam=1
# for i in range(1,n+1):
#     toplam*=i
# print(toplam)

# ###Fonksiyonel Programlama  ### Recursive
# def Faktor(n):
#     if n==1:
#         return 1
#     else:
#         return n*Faktor(n-1)
# print(Faktor(5))


#### OOP --> Object Oriented Programming
## 60'larda ortaya çıkmış, daha az karmaşıklık, daha hızlı çalışma
# Encapsulation, #Inheritance, Polymorphism, Abstraction ---> OOP sayılması için dördünün de olması lazım


#### Nesneleri ortak özellikleri ile birbirine bağlayan şey SINIF'tır.
### Örneğin: Toyota ile Renault, arabalar sınıfına dahil olur.

## Sınıf Tanımlama:
# class Arac():
#     marka=""
#     model=""
#     renk=""

# sedan=Arac() ### Nesne sınıftan oluşturuldu.
# sedan.marka="Toyota"
# sedan.model="Corolla"
# sedan.renk="Beyaz"
# print(sedan.renk)  ## istenilen özelliği sorgulama

# minivan=Arac() 
# print(minivan.marka) ### Sedanda olduğu gibi ayrıca bir özellik eklemezsek, class içinde tanımladığımız varsayılan özellik kullanılır.

# class Kullanicilar():
#     kimlikNo=""
#     isim=""
#     soyisim=""
#     bolum=""
# ogrenci=Kullanicilar()
# ogrenci.bolum="Bilgisayar Mühendisliği"
# ogretmen=Kullanicilar()
# Kullanicilar.bolum="Elektronik"
# print(ogrenci.bolum)
# print(ogretmen.bolum)

# class Kullanicilar():
#     kimlikNo=""
#     isim=""
#     no=""
#     def Yazdir(self): ### Self bu nesnedeki özelliği kullan
#         print(f"{self.kimlikNo} numaralı {self.isim} isimli öğrencinin okul numarası {self.no}")
#     def YazdirIsim(self):
#         print(f"Öğrencinin ismi {self.isim}")

# ogrenci=Kullanicilar()
# ogrenci.kimlikNo=12345678901
# ogrenci.isim="Ali KANDIR"
# ogrenci.no=102
# ogrenci.Yazdir()
# ogrenci.YazdirIsim()

# ogrenci1=Kullanicilar()
# ogrenci1.kimlikNo=456151315313513
# ogrenci1.isim="Mahmut Hoca"
# ogrenci1.no=456
# ogrenci1.Yazdir()
# ogrenci1.YazdirIsim()


#### Hayvan class ında  tavuk, beyaz,4kg Kuş. Balık("100kg,Ton balığı, gri") 

# class Hayvan():
#     kilo=""
#     isim=""
#     renk=""
    
#     def Yazdirİsim(self):
#         print(f"Bu hayvanın ismi {self.isim}")

#     def YazdirKilo(self):
#         print(f"Bu hayvanın kilosu: {self.kilo}")
#     def YazdirRenk(self):
#         print(f"Bu hayvanın rengi {self.renk}")

# kus=Hayvan()
# kus.isim="Tavuk"
# kus.kilo="4 kg"
# kus.renk="Beyaz"


# balık=Hayvan()
# balık.isim="Ton Balığı"
# balık.kilo="100 kg"
# balık.renk="Gri"

# kus.Yazdirİsim()
# kus.YazdirKilo()
# kus.YazdirRenk()

# balık.Yazdirİsim()
# balık.YazdirRenk()
# balık.YazdirKilo()


###__init__() fonksiyonu: yapılandırıcı

# class Kullanici():
#     def __init__(self,no,isim,tel):
#         self.no=no
#         self.isim=isim
#         self.tel=tel
#     def __str__(self) -> str:
#         return "Bu kullanıcı sınıfına ait bir nesnedir."
#     def __del__(self):
#         print("Nesne silindi...")
# ogrenci=Kullanici(1,isim="Ali",tel=36465456)

# # for deger,value in vars(ogrenci).items():
# #     print(f"{deger}:{value}")
# print(ogrenci)

###Inheritance (Miras)

# class Anne():
#     sacRengi="Sarı"
#     gozRengi="Mavi"
# class Baba():
#     sacRengi="Sarı"
#     gozRengi="Ela"
# class Cocuk(Anne,Baba):  ### Çocuk sınıfı boş olsa bile, Anne sınıfından özellik alır. ### İki sınıftandan da özellik alabiliriz.
#     sacRengi="Kahverengi" ### eğer bir değer atarsak, kendi özelliğini kullanır.
#     gozRengi="Yeşil"
# ozan=Cocuk()
# print(ozan.sacRengi)
# print(ozan.gozRengi)

# class Babaanne():
#     sacRengi="Sarı"
#     gozRengi="Mavi"
# class Baba(Babaanne):
#     sacRengi="Sarı"
#     gozRengi="Ela"
# class Cocuk(Baba): ### iki nesil üstten alıyorsak, en son aldığından gelir.
#     pass
# ozan=Cocuk()
# print(ozan.sacRengi)
# print(ozan.gozRengi)

# class Baba():
#     def __init__(self,boy,kilo) -> None:
#         self.boy=boy
#         self.kilo=kilo
# class Cocuk(Baba):
#     pass
# ahmet=Cocuk(1.80,75) ### init ile de çalışır.
# print(ahmet.boy)

# class Baba():
#     def __init__(self,sac,goz) -> None:
#         self.sac=sac
#         self.goz=goz
# class Cocuk(Baba):
#     def __init__(self, boy, kilo) -> None:
#         self.kilo=kilo
#         self.boy=boy

    
# ahmet=Cocuk(1.80,75) 
# print(ahmet.boy)
# print(ahmet.sac) ### Cocuk class ı içindeki init i alır, baba initini reddeder.
class Baba():
    def __init__(self,sac,goz) -> None:
        self.sac=sac
        self.goz=goz
class Cocuk(Baba):
    def __init__(self, boy, kilo,sac,goz) -> None:
        self.kilo=kilo
        self.boy=boy
        super().__init__(sac,goz) ### Super init kullanarak üstteki saç ve göz verisini almaya zorlayabiliriz.
        
    
ahmet=Cocuk(1.80,75,"Sarı","Yeşil") 
print(ahmet.boy)
print(ahmet.sac)