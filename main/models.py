from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    image= models.ImageField(upload_to='category/%y/%m/%d',blank=True, null=True)
    logo_image =  models.ImageField(upload_to='category/%y/%m/%d',blank=True, null=True)  
    
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    product = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='product_imgs/%y/%m/%d')
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.product
