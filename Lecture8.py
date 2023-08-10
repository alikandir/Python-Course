### önceki dersin sorusu hocanın çözümü:

# def MaasHesapla(yaka,cocukSayisi,kidem,yuksekLisans):
#     tabanMaas=4000
#     if yaka==2:tabanMaas=3000
#     maas=tabanMaas+cocukSayisi*150+kidem*100+yuksekLisans*300
#     print(maas)

# def VerileriAl():
#     yaka=int(input("Beyaz yaka için 1, Mavi yaka için 2 girin: "))
#     cocukSayisi=int(input("Çocuk sayısı: "))
#     kidem=int(input("Kıdem yılı: "))
#     yuksekLisans=int(input("Yüksek varsa 1, yoksa 2'yi girin: "))
#     return yaka,cocukSayisi,kidem,yuksekLisans
# devamMi="e"
# while devamMi=="e":
#     y,c,k,yl=VerileriAl()
#     MaasHesapla(y,c,k,yl)
#     devamMi=input("Devam etmek ister misin? [e/h]: ")

#### ikinci yöntem
# import os ### dosyaya yazdırmak için os kütüphanesi
# def MaasHesapla(yaka,cocukSayisi,kidem,yuksekLisans): ### maaş hesaplama
#     tabanMaas=4000
#     if yaka==2:tabanMaas=3000
#     maas=tabanMaas+cocukSayisi*150+kidem*100+yuksekLisans*300
#     VerileriYaz(yaka,cocukSayisi,kidem,yuksekLisans,maas)

# def VerileriAl(): ### çalışan verisini al
#     yaka=int(input("Beyaz yaka için 1, Mavi yaka için 2 girin: "))
#     cocukSayisi=int(input("Çocuk sayısı: "))
#     kidem=int(input("Kıdem yılı: "))
#     yuksekLisans=int(input("Yüksek varsa 1, yoksa 2'yi girin: "))
#     MaasHesapla(yaka,cocukSayisi,kidem,yuksekLisans)

# def VerileriYaz(yaka,cocukSayisi,kidem,yuksekLisans,maas): 
#     sonuc=f"{yaka} {cocukSayisi} {kidem} {yuksekLisans} {maas}\n"  ###verileri stringe dönüştür 
#     dosya.write(sonuc) ### dönüşen string i bilgisayara kaydet

# dosya=open("d:\\veri\\veri.txt","at") ### dosyayı aç ve düzenlenebilir olarak belirle "a" ile

# devamMi="e"
# while devamMi=="e":  ### devam etmek istediği sürece program çalışır.
#     VerileriAl()
#     devamMi=input("Devam etmek ister misin? [e/h]: ")

# dosya.close  ### dosya kapatmayı unutma.


#### XML ve JSON verileri okuma
### XML --> Genişletilebilir İşaretleme Dili. Hem insan hem bilgi işlem sistemleri tarafından kolayca okunabilir.
#### Örnek XML:
# <kitaplar>
#     <kitap>
#         <baslik>Dönüşüm</baslik>
#         <yazar>Franz Kafka</yazar>
#         <yayinevi>Martı Yayınları</yayinevi>
#         <yayinYili>1915</yayinYili>
#         <sayfaSayisi>120</sayfaSayisi>
#         <isbn>9758080931</isbn>
#     </kitap>
#     <kitap>
#         <baslik>Kuyucaklı Yusuf</baslik>
#         <yazar>Sabahattin Ali</yazar>
#         <yayinevi>İletişim Yayınları</yayinevi>
#         <yayinYili>1937</yayinYili>
#         <sayfaSayisi>200</sayfaSayisi>
#         <isbn>9754700886</isbn>
#     </kitap>
# </kitaplar>

### XML çalışma şekli --> Root(Kök), Düğümlerden oluşur. Düğümler ise Elemanlardan. Elemanlar verileri saklar.
## XML kullanım alanları-->Bir çok dil için evrensel veri transferi sağlar. Bir yazılımdan diğerine veri aktarırken iki tarafın da anlayacağı bir veri formatıdır.
### örneğin Microsoft'un .NET teknolojilerinde kullanılan datasetler XML formatındadır. Ofis uygulamalarının da alt yapısı XML formatındadır.
### XML bir programlama değil, bir işaretleme dilidir(HTML gibi).
# DOM ve SAX, XML'de biçimlenmiş verilerin çözümlesini(parser) sağlar.
#a) DOM (standart)--> verilerin tamamı belleğe atılır ve orada çalışır. Hızlı çalışır, ama düşük kaynaklı sistemlerde bellek yetersiz kalabilir.
#b) SAX --> verileri parça parça belleğe alır ve çalışır. Düşük sistemlerde daha iyi çalışır ama genel olarak daha yavaştır.

# import xml.etree.cElementTree as et  ### xml elementtree kütüphanesini import etme ve kullanım kolaylığı için bir lakap atama (as et).
# nesne=et.parse("d:\\veri\\veri.xml")
# kok=nesne.getroot()
# print(kok)
# print(kok[0].tag)
# print(kok[1].attrib)
# for dugum in kok:
#     print(dugum.attrib)   ### birden fazla attribute ekleyebiliriz, id den sonra örneğin grup="Roman" diyerek

# for eleman in kok.iter(): ### tümünü getirmek için. # iter içinde süzme işlemi yapılabilir. örnek: kok.iter("fiyat")
#     print(eleman.tag)

# for eleman in kok.iter("yazar"):
#     print(eleman.text) ### .text, taglerin karşılığını verir.
# print(kok[0].find("yazar").text)


#### JSON (JavaScript Object Notation). XML ile farkları: JS tabanlıdır. Aynı verileri daha küçük boyutta tutar. Daha hızlı çalışır. XML genişletilebilir, JSON'da öyle bir olanak yoktur.

## JSON, Pythondaki dictionary yapısına benzemektedir. key:value şeklinde yazılır. boolean kayıt ederken "true" diye girilir ("True" değil küçük harf ile)
# import json
# sozluk={"ad":"Ahmet","soyad":"Mehmet","yas":"30","evliMi":True}
# # with open("d:\\veri\\sozluk.json","wt") as dosya:
# #     dosya.writelines(json.dumps(sozluk)) ### json a dönüştürüp kaydet

# with open("d:\\veri\\sozluk.json","r") as dosya:
#     veriler=json.load(dosya)   ### json dosyasını sözlük olarak yükle
# print(veriler)
# print(type(veriler))

