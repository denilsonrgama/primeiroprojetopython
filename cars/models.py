from django.db import models

#Criando uma tabela e ligando por chave_estrangeira
class Brand(models.Model):
    idBrand = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Criado uma classe para o modelo de dados
class Car(models.Model): #a classe models é nativa, e ser herdado pela classe Car
    idCar = models.AutoField(primary_key=True) #autoincremento
    model = models.CharField(max_length=200) #tipo string max 200 caracteres
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True) #ano de fabricação tipo inteiro, aceita campo nulo ou vazio
    model_year = models.IntegerField(blank=True, null=True) #ano modelo tipo inteiro
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True) #Valor tipo flutuante
    photo = models.ImageField(upload_to='cars/',  blank=True, null=True)#local para armazenar as imagens upload


    def __str__(self):
        return self.model



