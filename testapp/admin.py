from django.contrib import admin
from . models import News , Product

class News_Admin(admin.ModelAdmin):
    list_display=['id','title','source','titleo']
    list_filter=('title','created','updated')

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','company1','product1','created','updated']
    list_filter=('company1','product1','company2','product2','company3','product3','company4','product4','product_name')
    prepopulated_fields={'slug':('product_name',)}
    search_fields=('product_name','company1','product1','company2','product2','company3','product3','company4','product4','detail1','detail2','detail3','detail4','name1','name2','name3','name4')    

# Register your models here.
admin.site.register(News,News_Admin)
admin.site.register(Product,ProductAdmin)
