###örnek: 1'den 1000'e kadar tüm asal sayıları yazdıran program:

#for i in range(2,1001):
#    for j in range(2,int(i**0.5)+1):
#        if i%j == 0:
#            break
#    else:
#      print(f"{i} asaldır")

###

# liste=["Elma","Portakal","Erik","Muz"]
# kume={"Elma","Portakal","Erik","Muz"}
# for eleman in liste:
#     print(eleman)

# for i in range(0, len(liste)):  ### index numarası kullanarak listeleme
#     print(liste[i])
# for index,deger in (enumerate(kume)): 
#   print(index,deger)

# liste.append("Mango") ## ekleme
# print(liste)

# liste.insert(1,"Mango")  ### insert belli bir yere ekleme
# print(liste)

# liste[1]="Mandalina" ### eleman değiştirme
# print(liste)


# liste.pop()  ###Sondan çıkarır ## parantez içine indeks numarası yazılırsa o değeri çıkarır
# print(liste)


# liste.remove("Elma")  #### Hangi değeri sileceğini değer vererek belirtiriz.
# print(liste)

# liste.clear()  ### liste içini temizleme
# print(liste)
# del liste   ### değişkeni tamamen silmek için

# liste.sort()  ###sıralama str ise alfabetik, int ise küçükten büyüğe
# print(liste)

# liste2=[-3,-5,8,8,8,6]  
# liste2.sort()
# print(liste2)
#  
# liste2.sort(reverse=True) ## Ters çevirme
# print(liste2)

# print(liste2.count(8))  ### kaç tane olduğunu bulmak için (string de kullanılabilir)

# print(8 in liste2) ### liste içinde bir şeyin olup olmadığını bulmak
# print(8 in liste) 

# liste1=["Ahmet", "Mehmet"]
# liste.extend(liste1) ### extend ile toplu halde liste ekleme (append bir eleman olarak ekler)
# print(liste)

### Liste eşitleme ve kopyalama:
# a=[3,5,7,8,1,2]
# b=a ###referans gösterir, kopyalamaz
# a.append(9)  ### yapılan değişiklik b'yi de etkiler
# print(b)

# b=a.copy() ### kopyasını oluşturur.
# a.append(9) ##kopya olduğu için a'daki değişiklik b'yi etkilemez
# print(b)

### kullanıcı tarafından girilen listenin her değerleri bir sayı ile çarpma problemi:

# list_uzun=int(input("liste uzunluğunu giriniz: "))
# liste=[]
# for i in range(1,list_uzun+1):
#     deger=int(input(f"{i}. değeri girin: "))
#     liste.append(deger)
# print(liste)
# multiple=int(input("Çarpılmak istenen sayıyı girin: "))
# for i in range(0,len(liste)):
#     yeni_deger=int(liste[i])*multiple
#     liste[i]=yeni_deger
# print(liste)
    
# for i in liste:  ###2.yöntem(listeye eklemez)
#     print(i*multiple)

# print([sayi*multiple for sayi in liste]) ### diğer yazım şekli

### matrix kullanma:
# şehir=[["izmir","manisa","aydın"],["ankara,konya"],["ağrı,kars"]]  ###liste içi listeye ulaşmak için iki köşeli parantez:
# print(şehir[0][2])


import random  ###rastgele sayı için random kütüphanesi kullanma
# liste=[]
# for i in range(100):
#     liste.append(random.randint(1,100))
# print(liste)

# print([random.randint(1,100) for i in range(100)])  ###2.yöntem


###Bilgisayar rastgele bir sayı tutacak (1,100) arasında, sen tahmin et, bilgisayar yukarı veya aşağı diye yönlendirir
# rastgele=random.randint(1,100)
# for i in range(0,3):
#     tahmin=int(input(f"{rastgele}Tahminde bulun: "))
#     if tahmin<rastgele:
#         print("Yukarı")
#     elif tahmin>rastgele:
#         print("Aşağı")
#     else:
#         print("Başarılı")
#         break
# else:
#     print("Başarısız")



