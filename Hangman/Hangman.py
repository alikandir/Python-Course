## Adam asmaca oyunu:
import time
import random

kelimeler=['elma', 'kalem', 'kitap', 'bilgisayar', 'masa', 'sandalye', 'ev', 'telefon', 'okul', 'araba',
             'ananas', 'karpuz', 'çanta', 'kilometre', 'yazılım', 'televizyon', 'heyecan', 'futbol', 'istanbul', 'çikolata']
print("Adam asmaca oyununa hoş geldin!")
time.sleep(1)
print("Uyarı: Lütfen her şeyi küçük harflerle yazın")


kelime=random.choice(kelimeler)
oyun_kelimesi=[]
for i in range(len(kelime)):
    oyun_kelimesi.append("_")


for i in range(6):
    print(oyun_kelimesi)
    tahmin=input("Bir harf tahmin ediniz: ")
    
    for i in range(len(kelime)):
        if tahmin==kelime[i]:
            oyun_kelimesi.pop(i)
            oyun_kelimesi.insert(i,tahmin)
if tahmin==kelime[i]:
    oyun_kelimesi.pop(i)
    oyun_kelimesi.insert(i,tahmin)
print(oyun_kelimesi)
time.sleep(1)
            
sonuc=input("kelimeyi tahmin edebildiniz mi?: ")
print("Acabaaa doğru mu?")
time.sleep(1)

if sonuc==kelime:
    print("Doğru bildin!! :)")
    time.sleep(1)
else:
    print(f"Kaybettiniz :(( Tuttuğum kelime: {kelime} idi")
    time.sleep(1)

