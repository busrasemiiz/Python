# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:06:04 2021

@author: Büşra Semiz
"""
siniflistesi= ["ayşe yılmaz", "ahmet öz", "engin demirog"]
derslistesi= ["java","c#", "ml", "deep learning","python"]

nameSurname= input("isim soyisim giriniz: ")
def dersAlma():
  if nameSurname in siniflistesi:
    print("ders listesinden ders seçebilirsiniz!!") 
    for i in derslistesi:
      print(i)
    dersSec=input("ders ismi girin: ")
    if dersSec in derslistesi:
      print("derse hoşgeldiniz")
    else:
      print("yanlış ders seçimi yaptınız")
  else:
    print("sınıf listesinde böyle biri yok")

dersAlma()
dersAlma()