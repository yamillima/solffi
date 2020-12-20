from django.contrib import admin
from .models import Cliente, Inversionista
import csv
from django.http import HttpResponse


class Fecha(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Exportar seleccionados como CSV"


admin.site.register(Cliente, Fecha)
admin.site.register(Inversionista, Fecha)
