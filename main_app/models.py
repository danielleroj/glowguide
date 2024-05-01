from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skin_type = models.CharField(max_length=100, blank=True, default='Undefined')
    quiz_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class SkinType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

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
    ingredients = models.TextField(blank=True, null=True)
    suitable_for = models.ManyToManyField(SkinType, blank=True, help_text='What skin type is this product suitable for?')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'pk': self.id})

class Routine(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'routine_id': self.id})
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for product_id: {self.product_id} @{self.url}"