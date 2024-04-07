from django.shortcuts import render
from django.http import HttpResponse
from .models import Names, Sellers
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
    pass



def inf(request, page_num):
    id = page_num
    teas = Names.objects.filter(category__id=id).order_by("-price")
    prices = []
    name_list =[]
    prod = []
    bool_sale = []
    for elem in teas:
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

    data = {"prices": prices,
            "final_price": final_price,
            "bool_sale": bool_sale,
            "name_list": name_list,
            "teas": teas,
            "prod": prod,
            "header": "Страница каталога номер"}
    return render(request, "shop/try.html", data)
# Create your views here.
