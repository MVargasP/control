from django.shortcuts import render,redirect, get_object_or_404 
from django.views.generic import ListView, DetailView, View,TemplateView
from .models import Chofer,Empresa,Distrito
from datetime import datetime, timedelta,date


class ConsultaView(ListView):
	model=Chofer
	
	def post(self,request,*args,**kwargs):
		buscar= request.POST['busca_placa']
		civ=request.POST['buscalo_civ']
		apellido= request.POST['ape']
		nombre= request.POST['nombre']

		

		if buscar:
			placa= Chofer.objects.filter(placa__exact=buscar)


		elif civ:
			placa= Chofer.objects.filter(civ__exact=civ)
		

		elif apellido and nombre:
			placa= Chofer.objects.filter(apellido__exact=apellido,nombre__exact=nombre)
		else:
			placa=0
			
			


		now=date.today()
	
	
		contexto = {
			'fecha_actual':now,
			'dni':placa,
	
			'busqueda':buscar,

		}
		
		return render(request,'cliente/chofer_list.html',contexto)

