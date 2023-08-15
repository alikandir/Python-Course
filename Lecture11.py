### Veri Tabanı Yönetim Sistemi --> Veriler için server oluşturup, yetkisi olan herkesin serverdan ulaşabilmesi.

## SQlite, veri tabanı yönetim sistemindeki server oluşturmak kadar geniş çaplı bir şey değil ama maliyeti de daha düşük.
# Ama sql sorgu yapabiliyorsun ve aynı zamanda veriyi lokalde tutabiliyoruz.
# Orta çaplı bir proje için.

# Data-->Information-->Knowledge-->Wisdom

# import sqlite3 as sql  ### sql ismi ile import etme

# vt=sql.connect("D:\\veri\\veritabani.sqlite")  ### Böyle bir dosya varsa ulaşır, yoksa önce oluşturur.

# im=vt.cursor() ## imleç oluştur

# im.execute("CREATE TABLE ogrenci(isim, soyisim, numara)")  ### Tablo oluştur
# vt.commit() ### İşlemleri kaydet
# vt.close()  ## kapat



# import sqlite3 as sql 

# vt=sql.connect("D:\\veri\\veritabani.sqlite")

# im=vt.cursor() 

# im.execute("CREATE TABLE ogrenci1(isim TEXT, soyisim TEXT, numara INTEGER)") ### veri tiplerini belirterek oluşturma
# vt.commit()
# vt.close()  



# im.execute("CREATE TABLE IF NOT EXISTS ogrenci1(isim TEXT, soyisim TEXT, numara INTEGER)")  #### Dosya var ise hata almamak için


# im.execute("CREATE TABLE IF NOT EXISTS ogrenci1(isim TEXT, soyisim TEXT, numara INTEGER NOT NULL)") not null diye eklersek boş bırakılmasına izin vermez. Örneğin yemek sepetine üyelikte telefon numarasının zorunlu istenmesi gibi

# im.execute("CREATE TABLE IF NOT EXISTS ogrenci1(isim TEXT, soyisim TEXT, numara INTEGER NOT NULL, PRIMARY KEY(numara))") ### primary key ekleme (aratmak için kullanılır)


# import sqlite3 as sql 

# vt=sql.connect("D:\\veri\\veritabani.sqlite")

# im=vt.cursor() 
# im.execute("CREATE TABLE IF NOT EXISTS musteri(no INTEGER, isim_soyisim TEXT NOT NULL, tel TEXT UNIQUE NOT NULL, eposta TEXT UNIQUE NOT NULL, posta_kodu TEXT DEFAULT 'Belirtilmemiş', PRIMARY KEY(no AUTOINCREMENT))")
# vt.commit()
# vt.close() 

# im.execute("""INSERT INTO musteri(isim_soyisim,tel,eposta) VALUES("Mehmet KANDIR", 5052613163, "mehmetkandir@gmail.com")""")

# vt.commit()
# vt.close() 


### joker eleman kullanma "?" "?"

import sqlite3 as sql 
vt=sql.connect("D:\\veri\\veritabani.sqlite")
im=vt.cursor() 
liste=[("ahmet mehmet","123","a@a.com"),("ali veli","456","b@b.com")]
komut="""INSERT INTO musteri(isim_soyisim,tel,eposta) VALUES(?,?,?)"""
for kayit in liste:
    im.execute(komut,kayit)
vt.commit()
vt.close