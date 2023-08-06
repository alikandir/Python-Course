###Bilgisayar rastgele bir sayı tutacak (1,100) arasında, sen tahmin et, bilgisayar yukarı veya aşağı diye yönlendirir
###İki kişilik hale getir!
# import random
# rastgele=random.randint(1,50)
# for i in range(0,5):
#     tahmin=int(input(f"Tahminde bulun: "))
#     if tahmin<rastgele:
#         print("Yukarı")
#     elif tahmin>rastgele:
#         print("Aşağı")
#     else:
#         print("Kazandın, yaşaşın! :))")
#         break
# else:
#     print("Kaybettin :((")


import random
import time
rastgele=random.randint(1,100)
yazi_tura=["yazı","tura"]

print("Oyuna hoşgeldiniz!")
time.sleep(1)

print("Kimin başlayacağını belirlemek için yazı tura atalım: ")
time.sleep(1)

yazi_tura_tahmin=input("yazı mı, tura mı?")
if yazi_tura_tahmin==random.choice(yazi_tura):
    print("Doğru bildiniz. İlk siz başlayın.")
else:
    print("Diğer oyuncu doğru bildi. İlk o başlayacak.")
time.sleep(2)
player1=input("1. Oyuncu adı giriniz: ")
player2=input("2. Oyuncu adı giriniz: ")
for i in range(1,9):
    if i%2==1:
        tahmin1=int(input(f"{player1}, tahminde bulun ({i}/8 deneme): ")) 
        if tahmin1<rastgele:
           print("Yukarı")
           continue
        elif tahmin1>rastgele:
           print("Aşağı")
           continue
        else:
           print(f"{player1} Tebrikler!! Kazandın! :))")
        break
    else:
         tahmin2=int(input(f"{player2}, tahminde bulun ({i}/8 deneme): "))
         if tahmin2<rastgele:
           print("Yukarı")
           continue
         elif tahmin2>rastgele:
           print("Aşağı")
           continue
         else:
           print(f"{player2} Tebrikler!! Kazandın! :))")
         break
else:
    print(f"{player1},{player2} Kaybettiniz :(( Doğru cevap: {rastgele}")   