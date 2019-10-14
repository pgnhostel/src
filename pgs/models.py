from django.db import models
from mysite.utils import unique_slug_generator
from django.db.models.signals import pre_save


class Pgs(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='pics', default='default.png')
    image1 = models.ImageField(upload_to='pics', default='default.png')
    image2 = models.ImageField(upload_to='pics', default='default.png')
    image3 = models.ImageField(upload_to='pics', default='default.png')
    desc = models.TextField(max_length=500)
    amen = models.TextField(max_length=500)
    address = models.CharField(max_length=255)
    area = models.ForeignKey('Area', on_delete=models.CASCADE)
    ph_no = models.CharField(max_length=40)
    category = models.ForeignKey('Gender', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Pgs)


class Area(models.Model):
    place = models.CharField(max_length=20)

    def __str__(self):
        return self.place


class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender
