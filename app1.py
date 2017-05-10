#!/usr/bin/env python3 
#-*- coding:utf-8 -*-
import sqlite3
with sqlite3.connect('plate.sqlite3') as app1:
  im=app1.cursor()
  def secim():
    print("Şehir Eklemek İçin (1)")
    print("Şehir Silmek İçin (2)")
    print("Listelemek için (3)")
    secim=int(input("Seçim yapınız : "))
    if secim==1:
      add_city()
    elif secim==2:
      delete_city()
    elif secim==3:
      listele()
    else:
      print("Lütfen Doğru Tuşlama Yapınız.")
  #Tablo oluşturma fonksiyonu
  def create_table():
    im.execute("CREATE TABLE IF NOT EXISTS plate (city,plate)")
  #Şehir ekleme fonksiyonu
  def add_city():
    city=input("Enter city name:")
    plate=int(input("Enter plate:"))
    im.execute("SELECT * FROM plate")
    #Tüm plaka değelerini cities adlı değişkende tutma
    cities=im.fetchall()
    #0'dan başlayıp cities değişkeninin eleman sayısına kadar
    for i in range(0,len(cities)):
        if plate==cities[i][1]:
          print("Bu şehir zaten kayıtlı !")
          break
        else:
          im.execute("INSERT INTO plate VALUES (?,?)",(city,plate))
          print("Başarılı bir şekilde ekleme yaptınız.")
          break
    app1.commit()
  def delete_city():
    delete_city=int(input("Silmek istediğin şehrin plakasını gir : "))
    im.execute("DELETE FROM plate WHERE plate=(?)",(delete_city,))
    print("Başarılı bir şekilde şehir sildiniz !")
    app1.commit()
  def listele():
    im.execute("SELECT * FROM plate")
    liste=im.fetchall()
    app1.commit()
    print(liste)
  secim()
