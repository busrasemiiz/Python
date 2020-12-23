# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:18:13 2020

@author: Büşra Semiz
"""

class Account:
    def __init__(self,isim,numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def hesapbilgileri(self):   #şimdi ben bu classıma yani her bir objeme birer tane metod vermek istiyorum hesap bilg...yazılır.
        print("isim:", self.isim)
        print("numara:",self.numara)
        print("bakiye:",self.bakiye) #bu sayede 3 özelliğimizi bir metod yardımıyla ekrana yazdırmış olacağız.
    def paracek(self,miktar):
           
        if (self.bakiye-miktar<0):
            print("bakiye yetersiz")
        else:
            self.bakiye-=miktar
            print("yenibakiye:",self.bakiye)
    def parayatir(self,miktar):
        self.bakiye+=miktar
        print("yeni bakiye", self.bakiye)

account= Account("busra",123456,1000)
account.hesapbilgileri()
account.paracek(800)
account.parayatir(600)