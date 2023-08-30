#### Thread en küçük yürütme birimidir. Bir process'i threadlere bölmek iş verimliliğini arttırır.

# def MesajYaz(mesaj):
#     i=1
#     while i<=5:
#         print(mesaj, end=" ")
#         i+=1
# MesajYaz("1.mesaj")  ### ayrı ayrı çalışırlar normalde
# MesajYaz("2.mesaj")

import threading  ### threading modülü kullanılır.
# def MesajYaz(mesaj):
#     i=1
#     while i<=5:
#         print(mesaj)
#         i+=1
# ### threading kullanımı: paralel çalışırlar
# t1=threading.Thread(target=MesajYaz,args=("1.mesaj",)) 
# t1.start()
# t2=threading.Thread(target=MesajYaz,args=("2.mesaj",))
# t2.start()


# threading.active_count() ###aktif çalışan threadlerin sayısı
# threading.enumerate()  ###aktif çalışan threadlerin listesi
# threading.main_thread()  ###ana threadi gösterir


#### Queue --> kuyruk
## Kuyruk elemanları sıra içinde toplanır FIFO yöntemi ile ilk giren ilk çıkar.
### sıradan iş çıkarmak dequeue, sıraya iş ekleme enqueue.

# import queue
# q=queue.Queue()

# for harf in "Merhaba":
#     q.put(harf)
#     while not q.empty():  ## kuyruk boşalana kadar devam eder.
#         print(q.get(),end=",") ### get ile kuyruktan sırayla harfleri alır

# import queue
# q=queue.Queue()
# q.put("1. İş")
# q.put("2. İş")
# q.put("3. İş")
# while not q.empty():
#     print(q.get())

### LifoQueue() methodu tersten yapar. (Last in First out), stack yapısı gibidir.

### PriorityQueue --> önceliklendirme

# import queue
# q=queue.PriorityQueue()
# q.put((2,"1. İş"))
# q.put((3,"2. İş"))
# q.put((1,"3. İş"))
# while not q.empty():
#     print(q.get())


# ### map kullanımı
# def KaresiniAL(sayi):
#     return sayi**2
# liste=[i for i in range(1,10)]
# yeniListe=list(map(KaresiniAL,liste)) ### listeyi fonksiyon içerisine argüman olarak gönderir.
# print(yeniListe)

# print([i**2 for i in range(1,10)])  ### tek satırda da yazılabilir

# def CiftSayi(sayi):
#     return sayi%2==0
# liste=range(1,20)
# print(list(filter(CiftSayi,liste))) ### filter yalnızca True değerleri gönderir.

#### Reduce fonksiyonu:

# from functools import reduce
# def Faktoriyel(sayi1,sayi2):
#     return sayi1*sayi2
# liste=range(1,10)
# print(reduce(Faktoriyel,liste)) ### adım adım gider, liste en küçük hale gelinceye kadar devam eder.


### Zip fonksiyonu iki listeyi birleştirmek için kullanılır.

# liste1=range(1,5)
# liste2=range(4,9)  ### eleman sayısı daha fazla
# liste3=zip(liste1,liste2)  ### birleştirebildiği kadar birleştirebilir. Küçük olanın eleman sayısı biterse fonksiyon sonlanır.
# print(list(liste3))

#### Lambda fonksiyonu: tek bir ifade içinde çok sayıda argüman alabilen bir fonksiyondur.

# KaresiniAl=lambda a: a**2

# print(KaresiniAl(5))

# Topla= lambda a,b: a+b
# print(Topla(16,8))


# map ile lambda kullanımı

# vizeler=[10,20,50,70,10,100]
# finaller=[60,30,90,30,100,90]

# print(list(map(lambda vize,final:vize*0.4+final*0.6,vizeler,finaller)))

### filter ile lambda kullanımı
# liste=range(1,10)
# print(list(filter(lambda x:x%2==1,liste)))


# from functools import reduce
# liste=range(1,11)
# print(reduce(lambda sayi1,sayi2:sayi1+sayi2,liste))