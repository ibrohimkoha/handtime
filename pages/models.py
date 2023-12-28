from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class WatchModel(models.Model):
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='watch/')
    name = models.CharField(max_length=20)
    price = models.IntegerField(null=True, blank=True)
    aksiya_price = models.IntegerField(null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True,null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'watch'
        verbose_name_plural = 'watchs'
