from django.contrib import admin
from .models import Tea, Names, Sellers, Promo, City


class SellersAdmin(admin.ModelAdmin):
    list_display = ['seller', 'discount_small','manager', 'mail']

class TeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'country']

class NamesAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'articul', 'seller', 'town']

class PromoAdmin(admin.ModelAdmin):
    list_display = ['kod', 'name', 'time']

class CityAdmin(admin.ModelAdmin):
    list_display = ['ct']


admin.site.register(Tea, TeaAdmin)
admin.site.register(Names, NamesAdmin)
admin.site.register(Sellers, SellersAdmin)
admin.site.register(Promo, PromoAdmin)
admin.site.register(City, CityAdmin)

# Register your models here.
