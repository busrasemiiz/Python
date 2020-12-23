class Account:
    def __init__(self,isim,numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def hesapbilgileri(self):  
        print("isim:", self.isim)
        print("numara:",self.numara)
        print("bakiye:",self.bakiye) 
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
