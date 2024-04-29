from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    CATEGORIES = (
    ('AT', 'Acne Treatments'),
    ('C', 'Cleansers'),
    ('E', 'Exfoliants'),
    ('EC', 'Eye Care'),
    ('FM', 'Face Masks'),
    ('FO', 'Face Oils'),
    ('FP', 'Facial Peels'),
    ('L', 'Lip Care'),
    ('M', 'Moisturizers'),
    ('S', 'Serums'),
    ('SS', 'Sunscreen'),
    ('T', 'Toners')
)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='AT')
    directions = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.get_category_display()}'

class Routine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'routine_id': self.id})
    