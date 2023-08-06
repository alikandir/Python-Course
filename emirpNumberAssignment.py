asal=[]
lasa=[]
tersler=[]
### Asal sayıları bul:
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
           asal.append(i)

### Asal sayıları tersine çevir:
for sayi in asal:
    ters=0   
    while sayi!=0:
        son_basamak=sayi%10
        ters=ters*10+son_basamak
        sayi= sayi//10
    tersler.append(ters)
### tek sayıları ve basamakları birbirine eşit sayıları terslerden çıkar:
tersler_copy=tersler.copy()
for sayi in tersler_copy:
     if sayi//10==0 or sayi//10==sayi%10:
          tersler.remove(sayi)
### Lasa olup olmadığını kontrol et:
for sayi in tersler:
     for j in range(2,sayi):
          if sayi%j==0:
               break
     else:
          lasa.append(int(sayi))
### Lasa listesini düzenle ve görüntüle
lasa.sort()
print(f"Lasa sayılar: {lasa}")
