from django.contrib import admin
from .models import Chofer, Micro, Repuesto, Mantenimiento

# Register your models here.
class ChoferAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'creado')
    search_fields = ('nombre', 'apellido')
class MicroAdmin(admin.ModelAdmin):
    list_display = ('patente', 'modelo', 'numero', 'creado')
    search_fields = ('patente', 'modelo')
class RepuestoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'creado')
    search_fields = ('nombre',)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('micro', 'repuesto', 'fecha', 'costo')
    search_fields = ('micro__patente', 'repuesto__nombre')

admin.site.register(Chofer, ChoferAdmin)
admin.site.register(Micro, MicroAdmin)
admin.site.register(Repuesto, RepuestoAdmin)
admin.site.register(Mantenimiento, MantenimientoAdmin)