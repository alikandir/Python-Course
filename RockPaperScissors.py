import random
import time
liste=["taş","kağıt","makas"]
tur=3
skor_pc=0
skor=0
print("Taş, kağıt, makas oyununa hoş geldin! :):) ")
time.sleep(0.5)
print("Oyunda lütfen sadece küçük harf kullan.")
time.sleep(0.5)
while tur>0:
    print(f"{tur} tur kaldı")
    time.sleep(0.5)
    print(f"Oyuncu: {skor}, Bilgisayar: {skor_pc}")
    time.sleep(0.5)
    secilen=input("Taş, kağıt, makas?: ")
    time.sleep(1)
    secilen_pc=random.choice(liste)
    if secilen=="taş" and secilen_pc=="kağıt":
        print("Kaybettin")
        time.sleep(0.5)
        print(f"Bilgisayarın tuttuğu:{secilen_pc},oyuncunun tuttuğu:{secilen}")
        time.sleep(0.5)
        tur-=1
        skor_pc+=1
    elif secilen=="taş" and secilen_pc=="makas":
        print("Kazandın")
        time.sleep(0.5)
        print(f"Bilgisayarın tuttuğu:{secilen_pc},oyuncunun tuttuğu:{secilen}")
        time.sleep(0.5)
        tur-=1
        skor+=1
    elif secilen=="taş" and secilen_pc=="taş":
        print("Berabere")
        time.sleep(0.5)
        print(f"Bilgisayarın tuttuğu:{secilen_pc},oyuncunun tuttuğu:{secilen}")
        time.sleep(0.5)
    
    elif secilen=="kağıt" and secilen_pc=="taş":
        print("Kazandın")
        time.sleep(0.5)
        print(f"Bilgisayarın tuttuğu:{secilen_pc},oyuncunun tuttuğu:{secilen}")
        time.sleep(0.5)
        tur-=1
        skor+=1
    elif secilen=="kağıt" and secilen_pc=="kağıt":
        print("Berabere")
        time.sleep(0.5)
        print(f"Bilgisayarın tuttuğu:{secilen_pc},oyuncunun tuttuğu:{secilen}")
        time.sleep(0.5)

    elif secilen=="kağıt" and secilen_pc=="makas":
        print("Kaybettin")
        time.sleep(0.5)
        print(f"Bilgisayarın tuttuğu:{secilen_pc},oyuncunun tuttuğu:{secilen}")
        time.sleep(0.5)
        tur-=1
        skor_pc+=1

    elif secilen=="makas" and secilen_pc=="taş":
        print("Kaybettin")
        time.sleep(0.5)
        print(f"Bilgisayarın tuttuğu:{secilen_pc},oyuncunun tuttuğu:{secilen}")
        time.sleep(0.5)
        tur-=1
        skor_pc+=1
    elif secilen=="makas" and secilen_pc=="kağıt":
        print("Kazandın")
        time.sleep(0.5)
        print(f"Bilgisayarın tuttuğu:{secilen_pc},oyuncunun tuttuğu:{secilen}")
        time.sleep(0.5)
        tur-=1
        skor+=1
    elif secilen=="makas" and secilen_pc=="makas":
        print("Berabere")
        time.sleep(0.5)
        print(f"Bilgisayarın tuttuğu:{secilen_pc},oyuncunun tuttuğu:{secilen}")
        time.sleep(0.5)
print("Oyun bitti... Veee:")
time.sleep(1)
if skor<skor_pc:
    print("Kaybettin... :(")
    print(f"Oyuncu: {skor}, Bilgisayar: {skor_pc}")
    time.sleep(3)
else:
    print("Kazandın!!! :)")
    print(f"Oyuncu: {skor}, Bilgisayar: {skor_pc}")
    time.sleep(3)
        