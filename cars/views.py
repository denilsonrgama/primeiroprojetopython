from django.shortcuts import render
from cars.models import Car

#Suas views ficarão aqui.
def cars_view(request):
    cars = Car.objects.all() #sintaxe para o select no django, retorna uma queryset
    search = request.GET.get('search')

    #se o usuario nao digitou nada na busca, traz tudo object.all
    if search:
        cars = Car.objects.filter(model__contains=search)

    return render(
        request,
        'cars.html',
        {'cars': cars}
    )
