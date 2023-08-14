### Soru 1: Palindrom Kontrolü
# Bir palindrom kelime veya cümle, tersten okunduğunda da aynı olan kelimeler veya cümlelerdir. 
#Bir palindrom kontrolü fonksiyonu yazarak, kullanıcının girdiği metnin palindrom olup olmadığını belirleyen bir program yazınız.
# def Palindrom(kelime):
#     for harf in range(len(kelime)//2):
#         if kelime[harf]!=kelime[(-harf-1)]:
#             print("Palindrom değildir.")
#             break
#     else:
#         print("Palindromdur.")
# Palindrom(input("Lütfen palindromluğu kontrol edilecek kelimeyi giriniz: "))



### Soru 2: Liste Sıkıştırma
#Verilen bir liste içerisindeki tekrar eden ardışık elemanları tek bir eleman haline getiren bir fonksiyon yazın.
#Örneğin, [1, 1, 2, 3, 3, 4, 4, 4, 5] listesini [1, 2, 3, 4, 5] şeklinde sıkıştıran bir program yazınız.

# def ListeTekrar(veri):
#     donusturSet=set(veri)
#     donusturListe=list(donusturSet)
#     return donusturListe

# def ListeOlustur():
#     liste=list()
#     secenek=1
#     while secenek==1:
#         secenek=int(input(f"Lütfen Seçiniz:\n1-Listeye eklemek için\n2-Listeyi bitirmek için\n"))
#         if secenek==1:
#             veri=int(input("Listeye eklenecek sayıyı giriniz: "))
#             liste.append(veri)
#     liste.sort()
#     print(liste)
#     print(ListeTekrar(liste))

# ListeOlustur()



###Soru 3: Çarpım Tablosu
#Kullanıcıdan bir sayı alan ve bu sayıya göre çarpım tablosunu oluşturan bir fonksiyon yazın.
# def CarpimTablosu(sayi):
#     print(f"Sayının çarpım tablosu:\n"
#           f"1*{sayi}={sayi*1}\n"
#           f"2*{sayi}={sayi*2}\n"
#           f"3*{sayi}={sayi*3}\n"
#           f"4*{sayi}={sayi*4}\n"
#           f"5*{sayi}={sayi*5}\n"
#           f"6*{sayi}={sayi*6}\n"
#           f"7*{sayi}={sayi*7}\n"
#           f"8*{sayi}={sayi*8}\n"
#           f"9*{sayi}={sayi*9}\n"
#           f"10*{sayi}={sayi*10}\n")
# sayi=int(input("Lütfen çarpım tablosu istenen sayıyı giriniz: "))
# CarpimTablosu(sayi)




### Soru 4: Tekrarlayan Harfleri Bulma
#Bir metin içerisinde hangi harflerin kaç kez tekrarlandığını bulan bir fonksiyon yazın. 
#Örneğin, "merhaba dünya" metni için çıktı şu şekilde olmalıdır: {'m': 1, 'e': 1, 'r': 1, 'h': 1, 'a': 2, 'b': 1, ' ': 1, 'd': 1, 'ü': 1, 'n': 1}

# def TekrarBul(metin):
#     sayim=list()
#     sozluk=dict()
#     for harf in metin:
#         sayi=metin.count(harf)
#         sozluk[f"{harf}"]=sayi
#     print(sozluk)
# metin=input("Lütfen bir yazı giriniz:\n")
# #print(tekrarsiz)
# TekrarBul(metin)


### Soru 5: Çift ve Tek Sayıları Ayırma
# Verilen bir liste içerisindeki çift ve tek sayıları ayıran iki ayrı liste döndüren bir fonksiyon yazın. 
#Örneğin, [1, 2, 3, 4, 5, 6] listesini çift ve tek sayıları ayrı ayrı [2, 4, 6] ve [1, 3, 5] listeleri olarak elde eden bir program yazınız.

# liste=list()
# tercih=1
# def TekCift(liste):
#     tek=list()
#     çift=list()
#     for sayi in liste:
#         if sayi==0:
#             çift.append(sayi)
#         elif sayi%2==0:
#             çift.append(sayi)
#         elif sayi%2==1:
#             tek.append(sayi)
#     return tek,çift


# print("Tek ve çift ayırıcıya hoş geldiniz")
# while tercih==1:
#     sayi=int(input("Lütfen bir sayı giriniz: "))
#     liste.append(sayi)
#     tercih=int(input("1-Sayı eklemeye devam et\n2-Sayıları ayır\n"))

# ayrim=TekCift(liste)
# print(f"Tek sayılar: {ayrim[0]}, Çift Sayılar: {ayrim[1]}")



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

