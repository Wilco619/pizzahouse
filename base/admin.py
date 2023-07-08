from django.contrib import admin
from base.models import Product,Flaticon,Blog,Chef,Order,OrderItem,Customer

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','description','composition','price','discounted_price','category','on_offer','image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','mobile','zipcode','county']

admin.site.register(Blog)
admin.site.register(Flaticon)
admin.site.register(Chef)
admin.site.register(Order)
admin.site.register(OrderItem)