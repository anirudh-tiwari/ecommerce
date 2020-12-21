from django.contrib import admin
from management.models import * 

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Cart)
admin.site.register(Tags)
admin.site.register(Product_Tags)
admin.site.register(Address)
admin.site.register(Order)