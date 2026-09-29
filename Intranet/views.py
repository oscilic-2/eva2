from django.shortcuts import render
from django.http import Http404
from django.db.models import Q
from django.db.models import CharField, TextField

from .models import Chofer, Mantenimiento, Micro, Repuesto

# Create your views here.

MODELOS = {
	'chofer': ('Choferes', Chofer),
	'choferes': ('Choferes', Chofer),
	'micro': ('Micros', Micro),
	'micros': ('Micros', Micro),
	'repuesto': ('Repuestos', Repuesto),
	'repuestos': ('Repuestos', Repuesto),
	'mantenimiento': ('Mantenimientos', Mantenimiento),
	'mantenimientos': ('Mantenimientos', Mantenimiento),
}
def inicio(request):
	return render(request, 'Intranet/inicio.html')
def lista_modelo(request, modelo):
	if modelo not in MODELOS:
		raise Http404("Modelo no encontrado")
	nombre_modelo, modelo_clase = MODELOS[modelo]
	objetos = modelo_clase.objects.all()
	campos_modelo = [
		campo for campo in modelo_clase._meta.fields
		if not campo.primary_key
	]
	buscar = request.GET.get('buscar', '').strip()
	if buscar:
		filtro = Q()
		for campo in campos_modelo:
			if isinstance(campo, (CharField, TextField)):
				filtro |= Q(**{f'{campo.name}__icontains': buscar})
		objetos = objetos.filter(filtro)

	filas = [
		{'valores': [getattr(objeto, campo.name) for campo in campos_modelo]}
		for objeto in objetos
	]
	contexto = {
		'titulo': nombre_modelo,
		'campos': [campo.verbose_name.title() for campo in campos_modelo],
		'objetos': filas,
	}
	return render(request, 'Intranet/lista_modelo.html', contexto)