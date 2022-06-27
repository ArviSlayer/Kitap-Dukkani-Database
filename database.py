import sqlite3

class Kitap:
    def __init__(self,_kitapid,_fiyat,_ismi,_yazar,_tur):
        self.KitapID = _kitapid
        self.İsmi = _ismi
        self.Fiyat = _fiyat
        self.Tur = _tur
        self.Yazar = _yazar
        
    def __str__(self):
        return "Kitap İsmi {}, Yazarı {}, Türü {}".format(self.İsmi,self.Yazar,self.Tur)

class Tur:
    def __init__(self,_turadi,_turID=None):
        self.TurAdi = _turadi
        self.TurID = _turID

class Kullanici:
    def __init__(self,_kullaniciadi,_password,role,_kullaniciID=None):
        self.KullaniciAdi = _kullaniciadi
        self.Password = _password
        self.Role = role
        self.KullaniciID = _kullaniciID
    
    def __str__(self):
        return "{} {} {}".format(self.KullaniciAdi,self.Password,self.Role)

class Profil:
    def __init__(self,_profilid,_isim,_soyisim):
        self.İsim = _isim
        self.Soyİsim = _soyisim
        self.ProfilID = _profilid
    
    def __str__(self):
        return self.İsim,self.Soyİsim

class Siparis:
    def __init__(self,_siparisadresi,_siparisid):
        self.SiparisAdresi = _siparisadresi
        self.SiparisID = _siparisid

    def __str__(self):
        return self.SiparisAdresi

class SiparisDetayi:
    def __init__(self,_siparisid,_kitapid):
        self.SiparisDetayID = _siparisid
        self.KitapID = _kitapid
    

class Nezih:

    


    def __CreateConnection(self):
        self.__Connection = sqlite3.connect("ArviS.db")
        self.__Cursor = self.__Connection.cursor()
        türler = "create table if not exists Türler(TurID integer primary key autoincrement,TurAdı text)"

        kitaplar = "create table if not exists Kitaplar(KitapID integer primary key autoincrement,Kitapİsmi text,KitapFiyat number,Tur integer,Yazar integer,TurID integer, foreign key(TurID) references Tür (TurID))"

        kullanıcılar = "create table if not exists Kullanicilar(KullaniciID integer primary key autoincrement,KullaniciAdi text, Password text,Role text)"

        profiller = "create table if not exists KullanıcıProfilleri(ProfilID integer primary key autoincrement, İsmi text, Soyİsmi text, foreign key (ProfilID) references Kullanici(KullaniciID))"

        siparisler = "create table if not exists Siparisler(SiparisID integer primary key autoincrement, SiparisAdresi text,KullaniciID integer,foreign key(KullaniciID) references Kullanici(KullaniciID))"

        satislar = "create table if not exists SiparisDetayi(SiparisID integer,KitapID integer, foreign key(SiparisID) references Siparis(SiparisID),foreign key(KitapID) references Kitap(KitapID))"

        islemler = [türler,kitaplar,kullanıcılar,profiller,siparisler,satislar]
        for x in islemler:
            self.__Cursor.execute(x)
        self.__Connection.commit()

    def EndConnection(self):
        self.__Connection.close()
    def __init__(self):
        self.__CreateConnection()


    def KitapEkle(self,kitap:Kitap):
        kitapEkle = "insert into Kitaplar(Kitapİsmi,Yazar,KitapFiyat) values (?,?,?)"
        self.__Cursor.execute(kitapEkle,(kitap.İsmi,kitap.Yazar,kitap.Fiyat))
        self.__Connection.commit()
    
    def KitapGuncelle(self,_eskiİsim,_yeniİsim,_yeniFiyat,_yeniturID):
        kitapGuncelle = "update Kitap set İsmi = ?, Fiyat = ?, TurID = ? where KitapID = ?"
        self.__Cursor.execute(kitapGuncelle,(_yeniİsim,_yeniFiyat,_yeniturID))
        self.__Connection.commit()

  
    def KitapSil(self,_kitapİsmi):
        
        kitapSil = "delete from Kitaplar where KitapID = ?"
        self.__Cursor.execute(kitapSil)
        self.__Connection.commit()

    def KitaplarıGöster(self):
                        #           0  ,  1   ,      2       ,  3    , 4   
        kitaplarıGoster = "select KitapID,Kitapİsmi,KitapFiyat,Yazar,Tur from Kitaplar"
        self.__Cursor.execute(kitaplarıGoster)
        kitaplar = self.__Cursor.fetchall()
        if (len(kitaplar)==0):
            print("Gösterilecek Kitap Bulunmamakta")
        else:
            for x in kitaplar:
                kitapDetayi = Kitap(x[1],x[0],x[2],x[3],x[4])
                print(kitapDetayi)

    def KullaniciEkle(self,kullanici:Kullanici):
        kullaniciEkle = "insert into Kullanicilar (KullaniciAdi,Password,Role) values (?,?,?)"
        self.__Cursor.execute(kullaniciEkle,(kullanici.KullaniciAdi,kullanici.Password,kullanici.Role))
        self.__Connection.commit()

    def KullaniciGoster(self,_isim,_password,_role):
        kullaniciBul = "select KullaniciAdi,Password,Role from Kullanicilar"
        self.__Cursor.execute(kullaniciBul)
        kullanicilar = self.__Cursor.fetchall()
        if (len(kullanicilar)==0):
            print("Kullanıcı Bulunamadı")
        else:
            for x in kullanicilar:
                detay = Kullanici(x[0],x[1],x[2])
                print(detay)

    def KullaniciBul(self,_name,_password):
        kullaniciBul = "select role from Kullanicilar where KullaniciAdi = ? and password = ?"
        self.__Cursor.execute(kullaniciBul,(_name,_password))
        kullanici = self.__Cursor.fetchall()
        if len(kullanici)==0:
            print("Kullanıcı Bulunamadı")
        else:
            return kullanici[0][0]
a = Nezih()


