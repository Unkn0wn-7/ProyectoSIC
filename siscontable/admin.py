from django.contrib import admin
from .models import Cuenta, Transaccion
# Register your models here.
admin.site.register(Cuenta)
admin.site.register(Transaccion)