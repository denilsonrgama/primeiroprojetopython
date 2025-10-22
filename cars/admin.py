from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.(registre seus modelos aqui)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',) #Listar quais campos voce quer que apareça na grid do admin
    search_fields = ('name',) #Fazer busca no campo na tabela car no admin


class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value','plate','photo') #Listar quais campos voce quer que apareça na grid do admin
    search_fields = ('model','brand') #Fazer busca no campo na tabela car no admin



admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)


