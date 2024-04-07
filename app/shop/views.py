from django.shortcuts import render
from django.http import HttpResponse
from .models import Names, Sellers, City
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'shop/index.html')

def catalog(request):
    return render(request, 'shop/catalog.html')


'''def black(request):
    return inf(request, 1)

def green(request):
    return inf(request, 2)

def herb(request):
    return inf(request, 3)'''


def city(request, page_num, city_id):
    #cits = City.objects.filter(id = city_id)
    #cs = cits[0].ct
    return inf(request, page_num, city_id)



def inf(request, page_num, city_id = 0):
    id = page_num
    if city_id == 0:
        teas = Names.objects.filter(category__id=id).order_by("-price")
    else:
        teas = Names.objects.filter(Q(category__id=id) & Q(town =city_id)).order_by("-price")
    prices = []
    name_list =[]
    prod = []
    bool_sale = []
    cities_sp = []
    for elem in teas:
        cits = City.objects.filter(ct=elem.town)
        for el in cits:
            cities_sp.append(el.ct)
        bool_sale.append(elem.discount)
    skidka = []
    for i in range(len(teas)):
        prices.append(teas[i].price)
        name_list.append(teas[i].name)
        p = (Sellers.objects.filter(seller=(teas[i].seller)))
        for elem in p:
            prod.append(elem.seller)
            skidka.append(elem.discount_small)
    final_price = []
    for i in range(len(bool_sale)):
        if bool_sale[i] == 0:
            final_price.append(prices[i])
        else:
            final_price.append(int(prices[i] - prices[i] * (skidka[i] / 100)))

    if len(prices) == 0:
        flag = 0
    else:
        flag = 1

    data = {"prices": prices,
            "flag": flag,
            "final_price": final_price,
            "bool_sale": bool_sale,
            "name_list": name_list,
            "teas": teas,
            "prod": prod,
            "cities_sp": cities_sp,
            "header": "Страница каталога номер"}
    return render(request, "shop/try.html", data)
# Create your views here.
