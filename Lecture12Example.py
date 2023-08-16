### Kişi sınıfına ait Öğrenci sınıfı ve Sql e kaydeden sql sınıfı oluştur:

class Kisi():
    def __init__(self,tel,eposta) -> None:
        self.tel=tel
        self.eposta=eposta

    def info(self):
        print(self.isim)
        print(self.tel)
        print(self.eposta)

class Ogrenci(Kisi):
    def __init__(self,isim,tel,eposta,vize,final):
        self.isim=isim
        self.tel=tel
        self.eposta=eposta
        self.__vize=vize
        self.__final=final
        self.__ortalama=self.__OrtalamaHesapla
        super().__init__(tel,eposta)
    
    def __OrtalamaHesapla(self):
        ortalama=(self.__vize+self.__final)/2
        return ortalama
    def GetterVizeFinal(self):
        print(f"Vize {self.__vize}, Final {self.__final}")
    def SetterVizeFinal(self):
        self.__vize=int(input("Vize notunu giriniz: "))
        self.__final=int(input("Final notunu giriniz: "))
    
    def TupleVeri(self):
        veri=(self.isim,self.tel,self.eposta,self.__vize,self.__final,self.__OrtalamaHesapla())
        return veri
class Tablo():
    def __init__(self):
        import sqlite3 as sql
        self.baglanti=sql.connect("D:\\veri\\exampleTable.sqlite")
        self.imlec=self.baglanti.cursor()
        self.imlec.execute("CREATE TABLE IF NOT EXISTS OgrenciTablo(ID INTEGER, isim TEXT NOT NULL, tel, eposta , vize INTEGER, final INTEGER,ortalama INTEGER, PRIMARY KEY(ID AUTOINCREMENT))")
    
    def Kaydet(self,bilgi): ### bilgi--->tuple() değer gelecek
        self.imlec.execute("INSERT INTO OgrenciTablo(isim,tel,eposta,vize,final,ortalama) VALUES(?,?,?,?,?,?)",bilgi)
        self.baglanti.commit()
    
    def VerileriListele(self):
        self.imlec.execute("SELECT * FROM OgrenciTablo")
        for satir in self.imlec:
            print(satir)
    
    def Sil(self,ID):
        komut=f"DELETE FROM OgrenciTablo WHERE ID={ID}"
        self.imlec.execute(komut)
        self.baglanti.commit()
    def Guncelle(self,ID):
        self.imlec.execute("UPDATE OgrenciTablo Set tel='4564654654' WHERE ID=?",(ID,))
    def Kapat(self):
        self.baglanti.close()

ogrenci1=Ogrenci("Ali Kandır","2456456","a@b.com",50,60)


ogrenci2=Ogrenci("Ahmet Mehmet","564546","ab@sdf.com",70,80)


ogrenci3=Ogrenci("Ahmet Mehmet","564546","ab@sdf.com",90,100)

tablo=Tablo()
tablo.Kaydet(ogrenci1.TupleVeri())
tablo.Kaydet(ogrenci2.TupleVeri())
tablo.Kaydet(ogrenci3.TupleVeri())

tablo.Sil(1)
tablo.Sil(2)