## örnek problem 1: %18 KDV hesaplayıcı program:
#urun = input("Ürün adı: ")
#fiyat = int(input("Ürün fiyatı: "))
#adet = int(input("Ürün adedi: "))
#print(f"{urun} ürünün toplam tutarı {(adet*fiyat)*1.18}")

## örnek problem 2: kısa ve uzun kenarları verilen dikdörtgenin çevre ve alanını hesapla.

#kısa_kenar = int(input("Kısa kenar (m)?: "))
#uzun_kenar = int(input("Uzun kenar (m)?: "))
#print(f"Dikdörtgenin çevresi: {(kısa_kenar + uzun_kenar)*2}'dır \nDikdörtgenin alanı: {kısa_kenar*uzun_kenar}'dır")
#print("Dikdörtgen alanı: {0}, Dikdörtgen çevresi: {1}".format((kısa_kenar*uzun_kenar),((kısa_kenar+uzun_kenar)*2)))



#### print("{:#<20}".format('deneme')) ## yazının sağına soluna metin eklemek

## örnek: girilen iki sayının toplamını, farkını, çarpımı, bölümü, modunu, üssünü hesaplayın.

#sayi1 = int(input("İlk sayıyı giriniz: "))
#sayi2 = int(input("İkinci sayıyı giriniz: "))
#print(f"Sayıların Toplamı: {sayi1+sayi2}\nSayıların Farkı: {sayi1-sayi2}\nSayıların Çarpımı: {sayi1*sayi2}\nSayıların Bölümü:{sayi1/sayi2}\nSayıların Modu:{sayi1%sayi2}\nSayıların Üssü:{sayi1**sayi2}")


### değişken değeri yer değiştirme:
#a=10
#b=15
#a,b = b,a ### bu şekilde yer değişikliği yapılır
#print(a)
#print(b)

### mantıksal ifadeler & | ! and or not. <>=
#sayi1=1
#sayi2=2
#print((sayi1==sayi2) & (sayi1<sayi2))



### if else elif koşulları

#ort=int(input("Öğrenci ortalamasını giriniz: "))

#if (ort>=60):
#    print("Geçtin!")

#elif (ort>=50):
#    print("Koşullu geçtin")

#else:
#    print("Kaldın :(")


### BMI hesaplama örnek: kilo(kg)/boy*boy(m)

#kilo= int(input("Kilonuzu girin: "))
#boy= float(input("Boyunuzu girin(m): "))

#bmi= kilo / (boy*boy)
#if bmi<18:
#    print("zayıf")
#elif bmi<25:
#    print("normal")
#else :
#    print("kilolusun")

### Örnek: Girilen sayı tek mi çift mi hesapla?:

#sayi= int(input("Bir sayı girin: "))

#if sayi%2==1:
#    print("Sayınız tek")
#else:
#    print("Sayınız çift")


### Örnek: üçgenin kenarlarını kıyasla. eşkenar, ikizkenar, çeşit kenar

#kenar1= float(input("Kenar biri girin: "))
#kenar2= float(input("Kenar ikiyi girin: "))
#kenar3= float(input("Kenar üçü girin: "))

#if kenar1==kenar2==kenar3:
#    print("Eşkenar üçgen")
#elif kenar1!=kenar2!=kenar3 and kenar1!=kenar3:
#    print("Çeşitkenar üçgen")
#else:
#   print("ikizkenar üçgen")



## for ve while loopları
#uzunluk=15
#for i in range (1, uzunluk):
#    print(f"{i}. kez Ali")

#### örnek girilen bir sayının tüm bölenlerini ekrana yazdır
#sayi = int(input("Bölenlerine ayrılacak sayı giriniz: "))

#for i in range (1, sayi+1, 1):
#    if sayi%i == 0:
#        print(i)

### örnek girilen sayının asal sayılığını kontrol et:
check = 0
sayi = int(input("Sayı giriniz: "))
for i in range (2, sayi):
    if sayi%i==0:
       print("asal değildir")
       break
    else:
        print("asaldır")
        break

