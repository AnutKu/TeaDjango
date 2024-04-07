from django.db import models

class Tea(models.Model):
    title = models.CharField('Категория чая', max_length=20)
    country = models.CharField('Cтрана происхождения', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Чай'
        verbose_name_plural = 'Чаи'

class City(models.Model):
    ct = models.CharField('Город', max_length=40)
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.ct


class Sellers(models.Model):
    seller = models.CharField('Поставщик', max_length=50)
    discount_small = models.IntegerField('Наибольший процент скидки при покупке до 1 кг')
    discount_large = models.IntegerField('Наибольший процент скидки при покупке более 1 кг')
    manager = models.CharField('Менеджер',max_length=50)
    mail = models.EmailField('Почта')
    paymentaccount = models.IntegerField('Номер счёта')
    bank = models.CharField('Обслуживающий банк', max_length=50)

    def __str__(self):
        return self.seller

    class Meta:
        verbose_name = 'Постащик'
        verbose_name_plural = 'Поставщики'



class Names(models.Model):
    name = models.CharField('Название', max_length=50)
    category = models.ForeignKey(Tea, on_delete=models.CASCADE, verbose_name = 'Категория')
    price = models.IntegerField('Цена за 100 грамм')
   # town = models.ForeignKey(City, on_delete=models.CASCADE,  verbose_name = 'Город')
    articul = models.IntegerField('Артикул')
    town =  models.ForeignKey(City, on_delete=models.CASCADE,  verbose_name = 'Город')
    seller = models.ForeignKey(Sellers, on_delete=models.CASCADE,  verbose_name = 'Поставщик')
    discount = models.IntegerField('Наличие скидки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'



class Promo(models.Model):
    kod = models.CharField('Промокод', max_length=100)
    name = models.ForeignKey(Names, on_delete=models.CASCADE, verbose_name = 'Наименование')
    category = models.ForeignKey(Tea, on_delete=models.CASCADE, verbose_name = 'Категория')
    time = models.DateField('Окончание действия промокода')

    def __str__(self):
        return self.kod

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'
# Create your models here.
