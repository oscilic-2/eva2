from django.test import TestCase

from .models import Chofer, Mantenimiento, Micro, Repuesto


class ListadosModelosTests(TestCase):
	def setUp(self):
		chofer = Chofer.objects.create(nombre='Ana', apellido='Pérez')
		micro = Micro.objects.create(patente='AA123BB', modelo='Urbano', numero=12)
		repuesto = Repuesto.objects.create(nombre='Filtro', descripcion='Filtro de aceite')
		Mantenimiento.objects.create(micro=micro, repuesto=repuesto, costo=1500)

	def test_portada_enlaza_los_cuatro_modelos(self):
		response = self.client.get('/')

		self.assertEqual(response.status_code, 200)
		for titulo in ('Choferes', 'Micros', 'Repuestos', 'Mantenimientos'):
			with self.subTest(titulo=titulo):
				self.assertContains(response, titulo)

	def test_listados_muestran_registros_y_controles_de_seleccion(self):
		listados = {
			'/choferes/': 'Ana Pérez',
			'/micros/': 'AA123BB - Urbano',
			'/repuestos/': 'Filtro',
			'/mantenimientos/': 'Mantenimiento de AA123BB - Urbano con Filtro',
		}
		for ruta, registro in listados.items():
			with self.subTest(ruta=ruta):
				response = self.client.get(ruta)
				self.assertEqual(response.status_code, 200)
				self.assertContains(response, registro)
				self.assertContains(response, 'selector-elemento')
				self.assertContains(response, 'data-accion="eliminar"')

	def test_modelo_desconocido_devuelve_404(self):
		response = self.client.get('/desconocido/')

		self.assertEqual(response.status_code, 404)
