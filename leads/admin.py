from django.contrib import admin
from .models import Cliente, Inversionista


class Fecha(admin.ModelAdmin):
    readonly_fields = ('fecha',)


admin.site.register(Cliente, Fecha)
admin.site.register(Inversionista, Fecha)
