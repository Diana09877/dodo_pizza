from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(help_text='указывать в сомах')
    consist = models.TextField()
    image = models.ImageField(upload_to='pizza_images')
    size = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Пиццы'
        verbose_name = 'Пицца'

    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(help_text='указывать в сомах')
    volume = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='drink_images')


    class Meta:
        verbose_name_plural = 'Напитки'
        verbose_name = 'Напиток'

    def str(self):
        return self.name