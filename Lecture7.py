#### Kombinasyon formülünü hesaplayan programı fonksiyon yardımıyla hesaplayın:
### C(n,r)=n!/(r!(n-r)!)

# def faktor(n):
#     faktoriyel=1
#     for i in range(1,n+1):
#         faktoriyel*=i
#     return faktoriyel
# n=int(input("Kombinasyon alınacak sayıyı giriniz: "))
# r=int(input("Kaçlı kombinasyonu alınacak: "))

# comb=faktor(n)/(faktor(r)*faktor(n-r))
# print(comb)

### Kendi yazdığımız fonksiyonu başka bir scripte import edebiliriz. Aynı klasörde olmaları yeterli, sonrasında örneğin:
### from kombinasyon import faktor şeklinde faktor fonksiyonunu kombinasyon dosyasından import edebiliriz.
### eğer ana scriptten bir fonksiyon çağırıldığında tüm fonksiyonun çalışmasını istemiyorsak:
### çalışmasını istemediğim kısmın başına if __name__=="__main__":(


#### Kod HATA DENETİMİ:

### (try) bloğu ile hata denetimi
# try:
#     a=int(input("a: "))
#     b=int(input("b: "))
#     print(a/b)
# except ZeroDivisionError: #### özel except durumları kullanılabilir.
#     print("Sıfıra bölünme hatası...")
# except ValueError:
#     print("Lütfen sadece sayı girin.")
# except:  ### hata oluşursa except çalışır
#     print("Hata oluştu...")  ### 0 a bölmeye çalışırsak hata oluşur.
# else:   ### try ile else kullanılabilir. hata oluşmazsa çalışır. 
#     print("İşleminiz tamamlandı.")
# finally: ### try ve finally her durumda çalışır.
#     print("Program kapanıyor.")


### Dosya, verilerin disk üzerinde saklanması için oluşturulan veri tipleri.
## xml,json,mysql,csv,dat,txt,xls(excel) verileri

### register-->işlemcide cache--->işlemcide (L1,L2,L3) registerdan bi alt hız, boyutu daha büyük.
### RAM---> Secondary memory(HDD,SSD)--> En altta (Tape,CD,Disket,Flash bellek.)



### dosya okuma
# dosya=open("D:\\Deneme1\\not.txt","rt")
# print(dosya.read())


## satır satır okuma:
# print(dosya.readline())
# print(dosya.readline())

### tüm satırları bir liste içine yazma:
# print(dosya.readlines())

# for satir in dosya:
#     print(satir)
# dosya.close()  ### başka birisi dosyaya ulaşmak isterse diye her zaman dosyayı kapatmamız gerek

### ikinci yol 
# for satir in open("D:\\Deneme1\\not.txt","rt"):
#     print(satir)   ### close kullanmamıza gerek kalmadı çünkü open yapmadık.

# ### üçüncü yol
# with open("D:\\Deneme1\\not.txt","rt") as dosya:  ### with ile açtığımızda kapatmamıza gerek yok
#     for satir in dosya:
#         print(satir)

## "w" --> yeni metin belgesi oluştur ya da varolan belgeyi temizleyerek yeni metin ekler.
# dosya=open("D:\\Deneme1\\oluştur.txt","wt")
# dosya.write("ilk dosyam")
# dosya.close 
## "a" --> arrange, varolan belgeye değişiklik yapmak için
# dosya=open("D:\\Deneme1\\oluştur.txt","at")
# dosya.write("\nilk dosyam ekleme")
# dosya.close

# dosya=open("D:\\Deneme1\\oluştur2.txt","wt")
# ekle=["merhaba\n","python kursu\n","nasilsiniz"]
# dosya.writelines(ekle) ### writelines ile dosyaya istenilenleri bir liste olarak ekleyebiliriz 
# dosya.close



#### os kullanma:
# import os
# os.remove("d:\\Deneme1\\oluştur2.txt") ## remove dosyayı siler.
# os.rmdir("d:\\Deneme1") ## klasör boş ise siler

# dosya=open("D:\\Deneme1\\oluştur2.txt","wt",encoding="utf-8") ### encoding i değiştirerek karakter setlerini uyumlu hale getiriyoruz. utf-8 türkçe karakterleri barındırıyor.
# ekle=["merhaba\n","python kursu\n","Nasılsınız"]
# dosya.writelines(ekle) ### writelines ile dosyaya istenilenleri bir liste olarak ekleyebiliriz 
# dosya.close
# os.system("calc") ### hesap makinesi açabilirsin
# os.chdir("D:\\Film")  ## klasör değiştirme
# print(os.getcwd())  ### directory bilgisini öğrenme
# os.listdir() ### konumdaki tüm dosyaları görme




#### çocuk sayısı beyaz ya da mavi yaka olma durumuna göre maaş hesaplama programı.
def maasBul():
    maas=0
    if beyaz_mavi==1:
        maas+=4000
    elif beyaz_mavi==2:
        maas+=3000
    
    maas=cocuk*150+maas
    maas=tecrube*100+maas

    if yuksek==1:
        maas+=300
    
    return maas
    
    
calısan_sayisi=int(input("Kaç çalışan verisi girilecek: "))
i=0
while i<calısan_sayisi:
    beyaz_mavi=int(input("Seçiniz:\n1-Beyaz yaka\n2-Mavi yaka\n"))
    cocuk=int(input("Lütfen çalışanın çocuk sayısını giriniz:"))
    tecrube=int(input("Lütfen çalışanın şirkette kaç yıl çalıştığını girin: "))
    yuksek=int(input("1-Yüksek lisans var\n2-Yüksek lisans yok\n"))
    i+=1
    maas=maasBul()
    print(maas)
    

