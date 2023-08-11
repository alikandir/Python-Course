metin=input("Okunması istenen metin dosyasının adını giriniz: ")

dosya=open(f"d:\\veri\\{metin}.txt","rt",encoding="utf-8")
satirlar=dosya.readlines()

def karakterSayici():
    karakterSayacı=0
    for satir in satirlar:
        for harf in satir:
            karakterSayacı+=1
    print(karakterSayacı)
def kelimeSayici():
    kelimeSayaci=0
    for i in range(len(satirlar)):
        kelimeSayaci+=satirlar[i].count(" ")
        kelimeSayaci+=1
    print(kelimeSayaci)

def satirSayici():
    print(len(satirlar))

print(f"Girilen veri içerisindeki satır sayısı:")
satirSayici()
print(f"Girilen veri içerisindeki kelime sayısı:")
kelimeSayici()      
print(f"Girilen veri içerisindeki karakter sayısı:")
karakterSayici()
