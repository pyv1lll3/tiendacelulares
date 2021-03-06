from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.template import RequestContext
import json
from .models import Consignacion, Consignacion_detalle
from django.http import HttpResponse
from clientes.models import Cliente
from productos.models import Producto


# Create your views here.
@method_decorator(login_required,name='dispatch')
class agregarconsignacion(TemplateView):
	template_name= 'ventas/consignacion/agregar.html'

method_decorator(login_required,name='dispatch')
class agregarventa(TemplateView):
	template_name= 'ventas/agregar.html'

@login_required(login_url='/')
def agregarconsignaciones(request):
	if request.method == 'POST':
		try:
			campo = 'Debe ingresar cliente'
			ccliente = int(request.POST.get('cliente'))
			cliente = Cliente.objects.get(id = ccliente)
			consignacion = Consignacion(cliente = cliente)
			lista = request.POST.getlist('lista[]')
			consignacion.save()
			for li in lista:
				l = li.split(",")
				cn = int(consignacion.pk)
				p = Producto.objects.get(id = int(l[0]))
				c=int(l[1])
				cd = Consignacion_detalle(consignacion=consignacion, producto=p, cantidad=c)
				cd.save()
			respuesta = "Consignacion registrada correctamente."
		except ValueError as e:
			#respuesta = "Error: "
			#respuesta =respuesta + campo
			respuesta = str(e.message)
		except Exception as ex:
			respuesta = str(ex.message)
		finally:
			return HttpResponse(
				json.dumps(respuesta), 
				content_type="application/json"
			)

@login_required(login_url='/')
def listarconsignaciones(request):
	consig = Consignacion.objects.filter(estado = True).order_by('-fecha')
	detalle = Consignacion_detalle.objects.all()
	user = request.user
	return render_to_response('ventas/consignacion/buscar.html', {'consigs': consig, 'detalle':detalle}, context_instance=RequestContext(request))
