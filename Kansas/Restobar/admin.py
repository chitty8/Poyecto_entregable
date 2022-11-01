from django.contrib import admin

from .models import Clientes, Mesas, Meseros

# Register your models here.



admin.site.register(Clientes)
admin.site.register(Meseros)
admin.site.register(Mesas)