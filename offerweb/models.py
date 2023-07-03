from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField



class Kontrahent(models.Model):
    Nazwa= models.CharField(max_length=32, unique=True, null = False)
    miejscowosc = models.CharField(max_length=32, blank=True)
    ulica = AddressField(on_delete=models.CASCADE, blank=True,null = True)
    email = models.EmailField(null=False)
    tel = PhoneNumberField(blank=True, default = "+48 ")
    
    

    def __str__(self):
        return self.Nazwa + ' (' + self.email+')'
    

class Oferty(models.Model):

    Uwagi = models.TextField(default='')
    kontrahenci=models.ForeignKey(Kontrahent,on_delete=models.CASCADE)
    nr_zew = models.CharField(max_length=32)
    data = models.DateField(auto_now_add = True)
    
class Indeksy(models.Model):
    mat={
        (0, "Tak"),
        (1, "Nie")
    }
    indeks= models.CharField(max_length=32)
    ilosc = models.IntegerField()
    Oferta=models.ForeignKey(Oferty,on_delete=models.CASCADE)
    czy_mat = models.PositiveBigIntegerField(default=1, choices=mat)

class Operacje(models.Model):
    typ = {
        (0, "Zwykła"),
        (1, "Kooperacja")
    }
    operacja = models.CharField(max_length=32)
    stawka=  models.CharField(max_length=32)
    typ_operacji = models.PositiveBigIntegerField(default=0, choices=typ)

class Technologia(models.Model):
    operacja=models.ForeignKey(Operacje,on_delete=models.CASCADE)