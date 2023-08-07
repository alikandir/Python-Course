#### Bir dizi içinde en büyük sayıyı bulup index'ini öğrenme problem:
# import random
# #Liste oluşturma
# liste=[random.randint(1,100) for i in range(10)]
# print(liste)
# enb=liste[0]
# enb_index=0
# for i in range(1,len(liste)):
#     if liste[i]>enb:
#         enb=liste[i]
#         enb_index=i
# print(f"En büyük sayı= {enb}, Index' i ise = {enb_index}")


#### TUPLE!!  Sembol: (), Indexleme var, Değiştirme yok, Tekrar etme var, index numaralandırma: 0...n

#demet=(1,2,3,35,8)
#print(demet)
#demet.count(1)  # veri manipülasyonu değil o yüzden çalışır.
#print(99 in demet)  #arama yapabiliriz

### Bir nesne ile oluşturulacaksa elemandan sonra virgül koyulmalı:
# demet=("Bilgisayar",)
# print(demet)
### Demet içinde liste koyabiliriz:
# demet=("Ankara","Rize", ["İzmir","Aydın","Manisa"])
# print(demet[2][1])
### İstisna! Tuple içinde liste olursa o listeye değişiklik yapabiliriz.
# demet[2][1]="Muğla"
# print(demet[2][1])


#### Set=Kümeleme Sembol: {}, Değiştirme: Var, Tekrar: Yok, indexleme yok
# kelime="ananas"
# liste=list(kelime)
# print(liste)
# demet=tuple(kelime)
# print(demet)

# kume=set(kelime)
# print(kume)

### Kümeleri birleştirmek: union() fonksiyonu

# a={1,2,3}
# b={3,4,5,6}
# print(a.union(b))   ### a|b aynı işi yapar
## a&b --> kesişim kümesini verir
## a-b --> a'nın b'den farkını verir.
## a^b --> kesişim dışında kalanları verir.

### frozenset((1,2,3)) # değiştirilemez.


#### Dictionary (Sözlük) Oluşturma--> Sembol: {}, indexleme manual, değiştirme var, tekrar(value bazında var).
# sozluk={key:value, key:value} ##syntax ı bu şekilde
# sozluk={"Hi":"Merhaba","Red":"Kırmızı"}
# print(sozluk)
# print(sozluk["Hi"])

# for key in sozluk:
#     print(f"Key değeri {key}, value {sozluk[key]}")  ### sozluk içinden value değerini ve key değeri alma

# for key,value in sozluk.items():
#     print(f"Key değeri {key}, value {value}") 

# for i in sozluk.items():
#     print(i) ## tuple olarak çağırır.

# sozluk["Hi"]="Buenos Dias" # Modifiye etme

# sozluk["Blue"]=3  ##eleman ekleme
# print(sozluk)
# sozluk.pop("Hi")
# print(sozluk)


#### Fal programı tasarlama ödevi:
# import random
# liste=["Bugünün Aydınlık Olacak","Gülümseme Dolu Bir Gün Olacak","Şans Sizden Yana Olacak","Olumlu Düşünceler Sizi Sarmalayacak","İyi Haberlerle Dolu Bir Gün Olacak", "Sevdiklerinizle Keyif Dolu Anlar Geçireceksiniz","Yeni Deneyimlere Açık Olun"]
# isim=input("Adınızı girin: ")
# yas=int(input("Yaşınızı girin: "))
# isim_uzun=len(isim)
# random=random.randint(0,isim_uzun*yas%8)
# print(liste[random])

### Bir ile 10 arasındaki sayılardan oluşan ve 50 verilik random listeyi, sözlüğe dönüştür. Sözlükteki her bir key:kaç defa o sayının kullanıldığını versin.

# import random
# liste=[random.randint(1,10) for sayi in range(50)]
# liste.sort()
# print(liste)
# dict={}
# for item in liste:
#     dict[item]=liste.count(item)
# print(dict)

#### count kullanmadan çözme:
# for sayi in liste:
#     if sayi in dict:
#         dict[sayi]+=1
#     else:
#         dict[sayi]=1
# print(dict)



#### Fonksiyonlar
#### from random import randint ### bir kütüphaneden spesifik bir fonksiyon çekme

# ## tanımlama
# def mesajYaz():
#     print("Merhaba")
# mesajYaz()

# ### Parametre ekleme
# def mesajYaz(mesaj):
#     print(mesaj)
# mesajYaz("Hoş geldin")

# def topla(parameter1,parameter2):
#     print(parameter1+parameter2)
# topla(15,25)

# def topla(*sayilar): ## * kullanmak gelebilecek argüman sayısını açık uçlu bırakır:
#     topla=0
#     for sayi in sayilar:
#         topla+=sayi
#     print(topla)
# topla(3,99,52)
# topla(2.2,3.7)
# topla(1,80,65,15,100)

def topla(x,y):
    print(x+y)
def çarpim(x,y):
    print(x*y)
def çikarma(x,y):
    print(x-y)
def bolme(x,y):
    print(x/y)

sayi1=int(input("Sayı biri girin: "))
sayi2=int(input("Sayı ikiyi girin: "))

islem=input("Ne yapmak istersiniz (topla,çıkar,çarp,böl): ").upper()

if islem=="TOPLA":
    topla(sayi1,sayi2)
elif islem=="ÇIKAR":
    çikarma(sayi1,sayi2)
elif islem == "ÇARP":
    çarpim(sayi1,sayi2)
elif islem=="BÖL":
    bolme(sayi1,sayi2)

