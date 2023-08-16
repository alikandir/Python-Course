# import sqlite3 as sql
# baglanti=sql.connect("D:\\veri\\personel.sqlite")
# imlec=baglanti.cursor()
# personel=[("Ozan Alptekin","Öğretmen",30000),("Toprak Alptekin","NONE",0),("Ege Tunç","Bilgisayar",20000),("Ayşenur Ok","Müdür",50000)]
# imlec.execute("CREATE TABLE IF NOT EXISTS personel(id INTEGER, Ad_Soyad TEXT NOT NULL, Ünvan TEXT DEFAULT 'Belirtilmemiş', Maaş NOT NULL, PRIMARY KEY(id AUTOINCREMENT))")
# komut="INSERT INTO personel(Ad_Soyad,Ünvan,Maaş) VALUES(?,?,?)"
# for kayit in personel:
#     imlec.execute(komut,kayit)
# baglanti.commit()
# baglanti.close()


### Object oriented ile çözmek:
# class Tablo():
#     def __init__(self) -> None:
#         import sqlite3 as sql
#         self.vt=sql.connect("D:\\veri\\personel.sqlite")
#         self.im=self.vt.cursor()
#         self.im.execute("CREATE TABLE IF NOT EXISTS personel2(ID INTEGER, Isim TEXT NOT NULL, Ünvan, Maaş NOT NULL,PRIMARY KEY(ID AUTOINCREMENT))")
    
#     def Kaydet(self,bilgi):
#         for kayit in bilgi:
#             self.im.execute("INSERT INTO personel2(Isim,Ünvan,Maaş) VALUES(?,?,?)",kayit)
#         self.vt.commit()
#     def Listele(self):
#         self.im.execute("SELECT * FROM personel2")
#         for veri in self.im:
#             print(veri)
    
#     def Kapat(self):
#         self.vt.close()

# personel=[("Ali Kandır","Biyolog",20000),("Mahmut Mehmet","Doktor",50000)]
# tablo1=Tablo()
# tablo1.Kaydet(personel)
# tablo1.Listele()
# tablo1.Kapat()




# for döngüsü ile sqlite ta verileri almak

import sqlite3 as sql
baglanti=sql.connect("D:\\veri\\personel.sqlite")
imlec=baglanti.cursor()
imlec.execute("SELECT * FROM personel") ### Veriyi kendi içinde kayıt ediyor. "*" hepsini almak için kullanılır.
# for satir in imlec:
#     print(satir)
### Sadece belli bir veriyi aramak için:
# for satir in imlec:
#     if satir[2]=="Öğretmen":
#         print(satir)

### Belli bir tagi için verileri alma
# imlec.execute("SELECT Ad_Soyad,Ünvan FROM personel")
# for satir in imlec:
#     print(satir)

# veriler=imlec.execute("SELECT Ad_Soyad,Ünvan FROM personel").fetchall
# print(veriler)
# print(type(veriler))

# print(imlec.fetchone())
# print(imlec.fetchone()) ### tek tek alır

# print(imlec.fetchmany(2)) 


### Veri Süzme (WHERE komutu)

# imlec.execute("SELECT * FROM personel WHERE Ad_Soyad='Ozan Alptekin'")
# veri=imlec.fetchall()
# print(veri)

# imlec.execute("SELECT * FROM personel WHERE Maaş>40000")
# veri=imlec.fetchall()
# print(veri)


### LIKE % ve _ Komutları

# print(imlec.execute("SELECT * FROM personel WHERE Ad_Soyad LIKE '__an%'").fetchall())  ### _ tek bir harf için joker, % ise birden fazla harf için
# print(imlec.execute("SELECT * FROM personel WHERE Ad_Soyad LIKE '%o_'").fetchall()) ## --> Ayşenur oku getirir


