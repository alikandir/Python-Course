### ** üzeri alma, % mod, // tam sayı bölme, / float bölme
### boolean ifade yazarken baş harfler büyük ex. True, False.
### interpriter dil olduğu için int için gerekli alan ihtiyaca göre belirleniyor. C gibi double yok.

#ilk program

#sayi1= int(input("1. sayiyi gir: "))
#sayi2= int(input("2. sayiyi gir: "))
#sonuc = sayi1 + sayi2
#print(sonuc)

#tek satırlık hali: 
##print (int(input("1. sayiyi gir: ")) + int(input("2. sayiyi gir: ")))

#"" ve '' iç içe kullanımı:
#print("Atatürk der ki'İstikbal göklerdedir...'")
#print('''Atatürk'ün dediği gibi "İstikbal göklerdedir..."''')

## print fonksiyonu sep (separate with ...) ve end (komutu bitirince şunu yap: ... "\n" default) kullanımı:
#print("Merhaba", "Dünya")
#print("Nasılsın?")
#print("Merhaba","Dünya", sep=",")
#print("Merhaba","Dünya", end=" ")
#print("Nasılsın?")

### format yöntemi ve f yöntemi:
sayi1=12
sayi2=21
#print(sayi1, "+", sayi2, "=", sayi1+sayi2) #klasik yöntem
#print("{} + {} = {}".format(sayi1,sayi2, sayi1+sayi2)) # format yöntemi
#print("{0} + {1} = {2} \n {0}*{1} = {3}".format(sayi1,sayi2, sayi1+sayi2, sayi1*sayi2)) # format yöntemi ##indeksini parantez içine yaz

print(f"{sayi1}+{sayi2} = {sayi1+sayi2}") ## f yöntemi