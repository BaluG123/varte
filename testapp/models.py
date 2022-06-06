from django.db import models
from djrichtextfield.models import RichTextField
from taggit.managers import TaggableManager
from django.urls import reverse
from django.utils import timezone

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")

# Create your models here.
class News(models.Model):
    STATUS_CHOICE=(('post','POST'),('draft','DRAFT'))
    title=models.CharField(max_length=1000,null=True,blank=True)
    titleo=models.CharField(max_length=1000,null=True,blank=True)
    link=models.CharField(max_length=1000,null=True,blank=True)
    image=models.FileField(null=True,blank=True,upload_to='images/')
    imageo=models.FileField(null=True,blank=True,upload_to='images/')
    video=models.FileField(null=True,blank=True,upload_to='videos/')
    youtube=models.CharField(max_length=2000,null=True,blank=True)
    twitter=models.CharField(max_length=1000000,null=True,blank=True)
    body=RichTextField()
    tags=TaggableManager()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    source=models.CharField(max_length=64,null=True,blank=True)
    credit_link=models.CharField(max_length=2000,null=True,blank=True)
    status=models.CharField(max_length=6,choices=STATUS_CHOICE)

    def __str__(self):
        return self.body

    class Meta:
        ordering=['-created']   

    def get_absolute_url(self):
        return reverse('newslist') 

class Product(models.Model):
    status_choices=(('published','Published'),('draft','Draft'))
    company_choices=(('flipkart','FlipKart'),('amazon','Amazon'),('ajio','Ajio'),('myntra','Myntra'),('ebay','Ebay'),('puma','Puma'),('adidas','Adidas'),('tatacliq','TataCliq'))
    product_choices=(('fashion','Fashion'),('electronics','Electronics'),('others','Others'),('sports','Sports'))
    product_name=models.CharField(max_length=64)
    slug=models.SlugField(max_length=64,unique_for_date="publish")
    name1=models.CharField(max_length=580,null=False,blank=False)
    image1=models.FileField(null=False,blank=False,upload_to='images/')
    link1=models.CharField(max_length=256,null=False,blank=False)
    rprice1=models.IntegerField(null=False,blank=False)
    oprice1=models.IntegerField(null=False,blank=False)
    off1=models.IntegerField(null=False,blank=False)
    company1=models.CharField(max_length=64,choices=company_choices,default="amazon",null=False,blank=False)
    product1=models.CharField(max_length=64,choices=product_choices,default="fashion",null=False,blank=False)
    name2=models.CharField(max_length=580,null=True,blank=True)
    image2=models.FileField(null=True,blank=True,upload_to='images/')
    link2=models.CharField(max_length=256,null=True,blank=True)
    rprice2=models.IntegerField(null=True,blank=True)
    oprice2=models.IntegerField(null=True,blank=True)
    off2=models.IntegerField(null=True,blank=True)
    company2=models.CharField(max_length=64,choices=company_choices,default="amazon",null=True,blank=True)
    product2=models.CharField(max_length=64,choices=product_choices,default="fashion",null=True,blank=True)
    name3=models.CharField(max_length=580,null=True,blank=True)
    image3=models.FileField(null=True,blank=True,upload_to='images/')
    link3=models.CharField(max_length=256,null=True,blank=True)
    rprice3=models.IntegerField(null=True,blank=True)
    oprice3=models.IntegerField(null=True,blank=True)
    off3=models.IntegerField(null=True,blank=True)
    company3=models.CharField(max_length=64,choices=company_choices,default="amazon",null=True,blank=True)
    product3=models.CharField(max_length=64,choices=product_choices,default="fashion",null=True,blank=True)
    name4=models.CharField(max_length=500,null=True,blank=True)
    image4=models.FileField(null=True,blank=True,upload_to='images/')
    link4=models.CharField(max_length=256,null=True,blank=True)
    rprice4=models.IntegerField(null=True,blank=True)
    oprice4=models.IntegerField(null=True,blank=True)
    off4=models.IntegerField(null=True,blank=True)
    company4=models.CharField(max_length=64,choices=company_choices,default="amazon",null=True,blank=True)
    product4=models.CharField(max_length=64,choices=product_choices,default="fashion",null=True,blank=True)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    objects=CustomManager()
    tags=TaggableManager()
    status=models.CharField(max_length=28,choices=status_choices,default='draft')

    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('home') 




