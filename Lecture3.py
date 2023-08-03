### for ve while için de else vardır.
## kökünü almak daha verimli

#sayi = int(input("Sayı giriniz: "))
#for i in range (2, int(sayi**0.5)+1):
#    if sayi%i==0:
#       print("Asal değildir")
#       break
#else:
#    print("Asaldır")


###continue adım atlatır:

#for i in range(1,11,1):
#    if i == 5:
#        continue
#    print(i)

###pass placeholder
#def empty():
#    pass


## for string için kullanımı:
#isim= "Ali"
#for harf in isim:
#    print(harf)


#start = int(input("Başlangıç: "))
#end = int(input("Bitiş: "))
#toplam = 0
#for i in range(start, end+1):
#    toplam += i
#print(toplam)

### while döngüleri:

#i=0
#while i<=5:
#    print("ali")
#    i+=1
## for in range(0,6,1) e denktir.


### soru: kullanıcının girdiği başlangıç ve bitiş değeri aralığındaki çift sayıları topla

#start=int(input("Başlangıç: "))
#end = int(input("Bitiş: "))
#toplam=0
#i=start
#while i<=end:
#    if i%2==0:
#        toplam+=i
#    i+=1
#print(toplam)


#pozitif bölenlerin toplamı kendisine eşitse mükemmel sayıdır. bir sayının mükemmel olup olmadığını kontrol et.
###ödev: girilen sayıya kadar olan tüm mükemmel sayıları bul

#sayi=int(input("Sayı: "))
#i=1
#toplam=0


#for j in range(0,sayi+1):
#    i=1
#    toplam=0
#    while i<j:
#       if sayi%i==0:
#          toplam+=i
#       i+=1
#    if toplam==sayi:
#       print("Mükemmel Sayi! :)")
#       print(j)
#    else:
#       print("Mükemmel Değil :(")
#       print(j)


#### FIFO First in first out, LIFO last in first out, QUEUE (Kuyruk) Fifo kullanır, Ağaç veri Yapısı (Tree)
#### Array oluşturma []
#array=[1,1.2,True,"Ali"]
#print(array[0:4])
#print(array[0:4:2]) ## 2 kaçar kaçar atlayacağını belirtir
#print(array[2:])
#print(array[:2])
#print(array[::-1])

#liste=[]
#print(liste)
#liste.append("elma") ##listeye ekleme
#print(liste)

#liste=list() #ikinci yöntem
#liste =["Armut"] #3.yöntem

#liste = [i for i in range(1,101)] ## for loop kullanma
#print(liste)

### stringi karakterleriyle listeleme
#kelime="Ali Kandır"
#liste=list(kelime)
#print(liste)