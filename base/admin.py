from django.contrib import admin


from base.models import Item,Flaticon,Blog,Chef,Order,OrderItem


admin.site.register(Item)
admin.site.register(Blog)
admin.site.register(Flaticon)
admin.site.register(Chef)

admin.site.register(Order)
admin.site.register(OrderItem)