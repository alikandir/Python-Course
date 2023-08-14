# ### Başarı notuna göre kaç öğrenci başarılı:
# liste=[55,75,95,25,40,60,35,75]
# for puan in liste:
#     if puan>=50:
#         print("Geçtin")
#     else:
#         print("Kaldın")

### 10 elemanlı bir sayı dizisinin ortalaması tam sayı ise bu sayıdan dizide kaç tane olduğunu bulun:

# liste=[]
# for i in range(1,11):
#     liste.append(int(input(f"{i}. sayıyı giriniz: ")))
# toplam=0
# for i in liste:
#     toplam+=i
# ort=toplam/10
# print(f"{liste.count(ort)} kez ortalamadan dizi içinde var.")

### İstenildiği kadar elemandan oluşan sayı dizisinde pozitif ve negatif eleman sayısını bulan program:
# liste=[]
# sayi= int(input("Kaç tane değer girilecek?: "))
# for i in range(sayi):
#     liste.append(int(input("Sayı girin: ")))
# negatif=0
# pozitif=0
# for sayi in liste:
#     if sayi<0:
#         negatif+=1
#     elif sayi>0:
#         pozitif+=1
# print(f"Pozitif sayı miktarı: {pozitif}, Negatif sayı miktarı: {negatif}")

### Polindrom check
## Kelimeyi al.
# kelime=input("Polindrom durumunu kontrol etmek için kelime giriniz: ")
# kelime_ters=[]
# kelime_düz=[]
# i=1
# for harf in kelime:
#     kelime_düz.insert(i,harf)
#     i+=1
# ## Tersine çevir.

# for harf in kelime:
    
#     kelime_ters.insert(0,harf)
    
# # # Aynı olup olmadığını kontrol et.
# if kelime_ters==kelime_düz:
#     print("Kelime Polindrom!")
# else:
#     print("Kelime polindrom değil")

# ### 5 elemanlı dizinin elemanlarını toplayan uygulama:
# # Dizi elemanlarını al.
# dizi=[]
# for i in range(1,6):
#     dizi.append(int(input(f"Toplanmasını istediğin {i}. sayıyı girin: ")))
# #Topla.
# print(f"Sayıların toplamı: {dizi[0]+dizi[1]+dizi[2]+dizi[3]+dizi[4]}")
### Girilen sayı dizideki kaç elemandan küçüktür? Bunu hesaplayan programı yaz:
# Sayı girişi
# kontrol=int(input("Kontrol edilecek sayıyı giriniz: "))
# # Dizi elemanlarını kontrol et.
# dizi=[3,5,7,12,15,19]
# sayac=0
# for sayi in dizi:
#     if kontrol<sayi:
#         sayac+=1
# # Output
# print(f"Girilen sayı şu kadar sayıdan küçüktür: {sayac}")
### Bir dizide dizi elemanlarının sondan başa doğru düzenlenmesini sağlayacak program:
# dizi=[12,19,27,35,49,55,67]
# dizi.sort(reverse=True)
# print(dizi)