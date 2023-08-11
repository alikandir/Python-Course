### Sıra no, ürün adı, adet, fiyat
### menü 1--- ürün ekle, 2--- ürün sil, 3---ürün listele, 4---ara,5---çıkış

 
### menü

sira=[]
urun=[]
adet=[]
fiyat=[]
siraNo=0
toplam2=0

def urunEkle():
    global siraNo
    urun.append(input("Ürün adını girin: "))
    adet.append(int(input("Ürün adedi girin: ")))
    fiyat.append(int(input("Ürün fiyatı girin: ")))
    sira.append(siraNo)
    siraNo+=1
    

def urunSil():
    silinecek=int(input("Silinecek ürünün sıra numarasını giriniz: "))
    sira.pop(silinecek)
    adet.pop(silinecek)
    fiyat.pop(silinecek)
    urun.pop(silinecek)

def urunListele():
    for i in range(len(sira)):
        print(f"Sıra numarası: {sira[i]}, Ürün adı: {urun[i]}, Ürün Adedi: {adet[i]}, Ürün Fiyatı: {fiyat[i]} ")

def arama():
    veri=int(input("Aranacak sıra numarasını giriniz: "))
    print(f"Sıra no: {sira[veri]}, Ürün adı: {urun[veri]}, Ürün Fiyatı: {fiyat[veri]}, Ürün adedi: {adet[veri]}")

def cariToplam():
    global toplam2
    for i in range(len(sira)):
        toplam=(adet[i]*fiyat[i])
        toplam2=toplam2+toplam
      
secenek=0
sayac=0
while secenek !=6:
    secenek=int(input(f"{1} Ürün ekle\n{2} Ürün sil\n{3} Ürün listele\n{4} Ara\n{5} Cari toplam\n{6} Çıkış\n"))
    if secenek==1:
        urunEkle()
             
        print(f"Ürün eklendi. Ürün Sırası: {sira[sayac]}, Ürün adı: {urun[sayac]}, Ürün adedi: {adet[sayac]}, Ürün fiyatı {fiyat[sayac]}\n")
        sayac+=1
    elif secenek==2:
        urunSil()
        sayac-=1
        siraNo-=1
    elif secenek==3:
        urunListele()
    elif secenek==4:
        arama()
    elif secenek==5:
        cariToplam()
        print(toplam2)

print("Görüşürüz")

