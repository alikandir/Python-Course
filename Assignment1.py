sayi=int(input("Sayı: "))
i=1
toplam=0
for j in range(0,sayi+1):
    i=1
    toplam=0
    while i<j//2+1:
       if j%i==0:
          toplam+=i
       i+=1
    if toplam==j:
       print(f"{j} Mükemmel Sayi!")
   