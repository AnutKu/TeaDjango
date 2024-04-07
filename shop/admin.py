from django.contrib import admin
from .models import Tea, Names, Sellers, Promo


class SellersAdmin(admin.ModelAdmin):
    list_display = ['seller', 'discount_small','manager', 'mail']

class TeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'country']

class NamesAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'articul', 'seller']

class PromoAdmin(admin.ModelAdmin):
    list_display = ['kod', 'name', 'time']



admin.site.register(Tea, TeaAdmin)
admin.site.register(Names, NamesAdmin)
admin.site.register(Sellers, SellersAdmin)
admin.site.register(Promo, PromoAdmin)

# Register your models here.
