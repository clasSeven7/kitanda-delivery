from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Resource)
admin.site.register(Product)
admin.site.register(Categorie)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Register)
