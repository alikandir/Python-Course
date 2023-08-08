### Fonksiyonlar devam:
# def departman(arge,muhasebe,uretim):
#     print(f"""Arge'deki elemean sayısı= {arge}, Muhasebedeki eleman sayısı= {muhasebe}, Üretimdeki eleman sayısı= {uretim}, Toplam eleman sayısı= {arge+muhasebe+uretim}""")
    

# departman(muhasebe=8,arge=6,uretim=7)    ### Dictionary olarak gönderir, key ve value kısmı olduğu için

# def departman(**param):  ### Çift yıldız koyulduğunda dictionary gönderir.
#     for key,value in param.items():
#         print(key,value)

# departman(arge=12, uretim=25, muhasebe=50)

## Default (varsayılan) değer:

# def departman(muhasebe,uretim,arge=0):  ### default değer atanacaksa en sona koyulur.
#     print(f"""Arge'deki elemean sayısı= {arge}
# Muhasebedeki eleman sayısı= {muhasebe}
# Üretimdeki eleman sayısı= {uretim}
# Toplam eleman sayısı= {arge+muhasebe+uretim}""")
# departman(10,35)

### Farklı tipte argümanlar gönderebiliriz:

# def ornek(param):
#     print(type(param))

# ornek(1) #int
# ornek("merhaba") #str
# ornek(3.14)  #float
# ornek([1,2,3]) #list
# ornek((1,2,3))  #tuple
# ornek({1:"bir",2:"iki"})   #dict

#### Fonksiyon sonucu üretilenin ana programda kullanılması:

def listeOlustur(elemanSayisi,bas,bitis):
    from random import randint
    liste=[randint(bas,bitis) for i in range(elemanSayisi)]
    #print(liste) ### burada "liste" değişkeni sadece fonksiyon içinde kalır. 
    return liste  ## return edersek değişken global hale gelir, local olmaktan çıkar.
# liste1=listeOlustur(50,1,100)
# print(liste1)

# def buyukSayiBul(liste2): ### liste2 yerine liste yazsam da çalışır, çünkü return edilen şey "liste" değil "liste"nin tuttuğu değer
#     enb=liste2[0]
#     for sayi in liste2:
#         if sayi>enb:
#             enb=sayi
#     print(enb)

# # liste1=listeOlustur(50,15,70)
# # buyukSayiBul(liste1)

# # buyukSayiBul(listeOlustur(50,10,60)) ## fonksiyonları iç içe de kullanabiliriz.

# def listeOlusturVeEnbBul(elemanSayisi,bas,bitis): ### fonksiyonları birleştirebiliriz ama normalde yapılmaz. Her fonksiyon tek işlevi görür.
#     from random import randint
#     liste=[randint(bas,bitis) for i in range(elemanSayisi)]

#     enb=liste[0]
#     for sayi in liste:
#         if sayi>enb:
#             enb=sayi
#     return liste,enb ## ikisini return edebiliriz.
# liste1,enb1=listeOlusturVeEnbBul(10,15,50) ### ikisini ayrı ayrı kayıt etmek için
# print(liste1)
# print(enb1)

# sonuclar=listeOlusturVeEnbBul(10,1,50) ### tek değere atarsak, tuple içinde verir. listeyi bir eleman olacak şekilde içine ekler.
# print(sonuclar)


### Global değişkenler yapmak
# def isim(): ### localdeki "a" ile globaldeki "a" farklı
#     a=0
#     a=a+1
#     print(a)
# a=5
# isim()
# print(a)

# def isim():
#     global a   ### global "a"yı fonksiyonun içinde kullanmak için, global keyword'ü kullanarak global hale getirebiliriz.
#     a=a+1
#     print(a)
# a=5
# isim()
# print(a)



