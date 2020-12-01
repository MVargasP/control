from django.shortcuts import render,redirect, get_object_or_404 
from django.views.generic import ListView, DetailView, View,TemplateView
from .models import Chofer,Empresa,Distrito
from datetime import datetime, timedelta,date

class ConsultaView(ListView):
	model=Chofer
	
	def post(self,request,*args,**kwargs):
		buscar= request.POST['buscalo']
		placa= Chofer.objects.filter(placa__exact=buscar)
		dni=Chofer.objects.filter(dni__exact=buscar)
		if dni:
			placa=dni
		if placa:
			dni=placa
			
		now=date.today()
		dni=placa
		print(dni,placa)
		contexto = {
			'fecha_actual':now,
			'dni':dni,
	
			'busqueda':buscar,
			'placa':placa,
		}
		
		return render(request,'cliente/chofer_list.html',contexto)